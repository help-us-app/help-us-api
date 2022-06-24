import requests
from flask import Flask, request, json

from controller.square_auth_controller import SquareAuthController
from services.square_services import SquareService

app = Flask(__name__)
square_service = SquareService(requests)
auth_controller = SquareAuthController(square_service)


@app.route('/')
def index():
    return json.dumps(request.args)


@app.route('/authorization', methods=['GET'])
def authorization():
    code = request.args.get('code')
    state = request.args.get('state')
    result = auth_controller.set_merchant_information({
        'code': code,
        'user_id': state
    })
    return {
        'result': result
    }


@app.route('/authorization_url', methods=['POST'])
def authorization_url():
    user_id = request.json['user_id']

    return {
        'url': auth_controller.get_auth_link(user_id)
    }


if __name__ == "__main__":
    app.run()
