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

    # print generator to list of dicts
    locations = [location.to_dict() for location in result]
    return {
        'result': locations
    }


if __name__ == "__main__":
    app.run()
