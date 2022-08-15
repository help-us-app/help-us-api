import http
import requests
from flask import Flask, request, json
from werkzeug.utils import redirect
from flask_cors import CORS

from constants.variables import Variables
from controller.square_auth_controller import SquareAuthController
from controller.square_location_controller import SquareLocationController
from controller.square_payment_controller import SquarePaymentController
from middleware.middleware import middleware
from services.square_services import SquareService

app = Flask(__name__)
CORS(app, allow_headers=['Authorization'], expose_headers=['Authorization'], supports_credentials=True,
     resources={r'/*': {'origins': '*'}})
variables = Variables()
app.wsgi_app = middleware(app.wsgi_app, variables.middleware_token)
square_service = SquareService(requests)
auth_controller = SquareAuthController(square_service)
location_controller = SquareLocationController(square_service)
square_payment_controller = SquarePaymentController(square_service)


@app.route('/')
def index():
    return json.dumps(request.args)


@app.route('/oauth', methods=['GET'])
def authorization():
    code = request.args.get('code')
    state = request.args.get('state')
    grant_type = 'authorization_code'

    auth_controller.update_merchant_information({
        'code': code,
        'user_id': state,
        'grant_type': grant_type,
    })
    return "Authorization successful, you can close this window."


@app.route('/oauth/url', methods=['GET'])
def get_authorization_url():
    user_id = request.args.get('user_id')

    result = auth_controller.get_auth_link(user_id)

    return redirect(result)


@app.route('/location/<location_id>', methods=['GET'])
def get_location(location_id):
    result = location_controller.get_location_information({
        'location_id': location_id,
        'user_id': request.args.get('user_id'),
    })

    response = json.jsonify(result.to_dict())
    response.headers.add('Access-Control-Allow-Origin', 'https://help-us-app.com/')
    return response


@app.route('/location', methods=['GET'])
def list_locations():
    result = location_controller.list_locations({
        'user_id': request.args.get('user_id'),
    })

    return json.jsonify({
        'result': [location.to_dict() for location in result]
    })


@app.route('/payment', methods=['POST'])
def create_payment():
    request_json = request.get_json()

    line_items = []
    num = 0
    payment_note = {
        'buyer_email': request_json['buyer_email'],
        'line_items': [],
    }

    for line_item in request_json['line_items']:
        num += 1
        line_items.append({
            "name": "Item #{}".format(num),
            "quantity": "1",
            "item_type": "ITEM",
            "base_price_money": {
                "amount": int(line_item['price'].replace('$', '').replace('.', '')),
                "currency": "USD"
            }
        })

        payment_note['line_items'].append(line_item['id'])

    payment_note = json.dumps(payment_note)

    json_parsed = {
        'user_id': request_json.get('user_id'),
        'location_id': request_json.get('location_id'),
        "buyer_email": request_json.get('buyer_email'),
        "payment_note": payment_note,
        "line_items": line_items
    }
    result = square_payment_controller.create(json_parsed)

    return json.jsonify(result.to_dict())


@app.route('/payment/webhook', methods=['POST'])
def payment_webhook():
    request_json = request.get_json()['data']['object']['payment']['note']

    request_json = json.loads(request_json)

    square_payment_controller.webhook({
        'item_ids': request_json['line_items'],
        'buyer_email': request_json['buyer_email'],
    })

    return '', http.HTTPStatus.NO_CONTENT


if __name__ == "__main__":
    app.run(port=8081, debug=True)
