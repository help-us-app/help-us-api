import requests
from flask import Flask, request, json

from constants.variables import Variables
from controller.square_auth_controller import SquareAuthController
from services.square_services import SquareService

app = Flask(__name__)
square_service = SquareService(requests)
auth_controller = SquareAuthController(square_service)
variables = Variables()


@app.route('/')
def index():
    return json.dumps(request.args)


@app.route('/square_url')
def variables_index():
    return variables.square_url


if __name__ == "__main__":
    app.run()
