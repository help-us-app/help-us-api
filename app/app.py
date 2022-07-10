import requests
from flask import Flask, request, json

from controller.square_auth_controller import SquareAuthController
from controller.square_location_controller import SquareLocationController
from services.square_services import SquareService

app = Flask(__name__)
square_service = SquareService(requests)
auth_controller = SquareAuthController(square_service)
location_controller = SquareLocationController(square_service)


@app.route('/')
def index():
    return json.dumps(request.args)


@app.route('/oauth', methods=['GET'])
def authorization():
    code = request.args.get('code')
    state = request.args.get('state')
    refresh_token = request.args.get('refresh_token')
    result = auth_controller.update_merchant_information({
        'code': code,
        'user_id': state,
        'refresh_token': refresh_token
    })
    return {
        'result': result
    }


@app.route('/location/<location_id>', methods=['GET'])
def get_location(location_id):
    result = location_controller.get_location_information({
        'location_id': location_id,
        'access_token': request.args.get('access_token')
    })
    return {
        'result': result.to_dict()
    }


@app.route('/location', methods=['GET'])
def list_locations():
    result = location_controller.list_locations({
        'access_token': request.args.get('access_token')
    })

    return {
        'result': [location.to_dict() for location in result]
    }


if __name__ == "__main__":
    app.run(port=8080, debug=True)
