import requests
from flask import Flask, request, json

from controller.serp_controller import SerpController
from controller.square_auth_controller import SquareAuthController
from controller.square_location_controller import SquareLocationController
from services.serp_service import SerpService
from services.square_services import SquareService

app = Flask(__name__)
square_service = SquareService(requests)
serp_service = SerpService(requests)
auth_controller = SquareAuthController(square_service)
location_controller = SquareLocationController(square_service)
serp_controller = SerpController(serp_service)


@app.route('/')
def index():
    return json.dumps(request.args)


@app.route('/oauth', methods=['GET'])
def authorization():
    code = request.args.get('code')
    state = request.args.get('state')
    grant_type = 'authorization_code'

    result = auth_controller.update_merchant_information({
        'code': code,
        'user_id': state,
        'grant_type': grant_type,
    })
    return {
        'result': result
    }


@app.route('/location/<location_id>', methods=['GET'])
def get_location(location_id):
    result = location_controller.get_location_information({
        'location_id': location_id,
        'user_id': request.args.get('user_id'),
    })
    return {
        'result': result.to_dict()
    }


@app.route('/location', methods=['GET'])
def list_locations():
    result = location_controller.list_locations({
        'user_id': request.args.get('user_id'),
    })

    return {
        'result': [location.to_dict() for location in result]
    }


@app.route('/search', methods=['GET'])
def search():
    result = serp_controller.search({
        'query': request.args.get('query'),
    })
    return {
        'result': [serp.to_dict() for serp in result]
    }


if __name__ == "__main__":
    app.run(port=8080, debug=True)
