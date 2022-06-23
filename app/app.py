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


if __name__ == "__main__":
    app.run()
