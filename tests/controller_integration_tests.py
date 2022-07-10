import unittest

import requests

from controller.square_auth_controller import SquareAuthController
from controller.square_location_controller import SquareLocationController
from controller.square_payment_controller import SquarePaymentController
from models.responses.checkout_response import CheckoutResponse
from models.responses.location_response import LocationResponse
from services.square_services import SquareService


class MyTestCase(unittest.TestCase):
    square_service = SquareService(requests)
    auth_controller = SquareAuthController(square_service)
    location_controller = SquareLocationController(square_service)
    payment_controller = SquarePaymentController(square_service)
    user_id = 'ad195d18-da32-4000-a3d5-b5826b501016'
    location_id = 'L8CCETXTQPQVV'
    payment_link_id = None

    def test_list_locations(self):
        result = self.location_controller.list_locations({
            'user_id': self.user_id,
        })

        for location in result:
            self.assertTrue(location.id is not None)

    def test_get_location(self):
        result: LocationResponse = self.location_controller.get_location_information({
            'location_id': self.location_id,
            'user_id': self.user_id,
        })
        self.assertTrue(result.location.id is not None)

    def test_payment(self):
        result: CheckoutResponse = self.payment_controller.create({
            'user_id': self.user_id,
            'location_id': self.location_id,
            "buyer_email": "carlduncanja@gmail.com",
            "buyer_phone_number": "+1-202-555-0125",
            "customer_id": "VY7D5580R93SDDNPB6B5S78FHW",
            "payment_note": "Test Note",
            "line_items": [
                {
                    "name": "Test Name",
                    "quantity": "1",
                    "item_type": "ITEM",
                    "base_price_money": {
                        "amount": 10000,
                        "currency": "AUD"
                    }
                }
            ]
        }
        )
        self.assertTrue(result.payment_link.url is not None)
        self.list_payment(result.payment_link.id)
        self.update_payment(result.payment_link.id)
        self.delete_payment(result.payment_link.id)

    def list_payment(self, payment_link_id):
        result = self.payment_controller.read({
            'user_id': self.user_id,
            'id': payment_link_id,
        })
        self.assertTrue(result.payment_link.url is not None)

    def update_payment(self, payment_link_id):
        result = self.payment_controller.update({
            'user_id': self.user_id,
            'id': payment_link_id,
            "payment_note": "Test Note from Carl Duncan"})
        self.assertTrue(result)

    def delete_payment(self, payment_link_id):
        result = self.payment_controller.delete({
            'user_id': self.user_id,
            'id': payment_link_id,
        })
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
