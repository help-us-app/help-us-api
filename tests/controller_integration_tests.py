import unittest

import requests

from controller.square_auth_controller import SquareAuthController
from controller.square_location_controller import SquareLocationController
from controller.square_payment_controller import SquarePaymentController
from models.responses.checkout_response import CheckoutResponse
from models.responses.location_response import LocationResponse
from services.square_services import SquareService
from utils.scraper import Scraper


class MyTestCase(unittest.TestCase):
    square_service = SquareService(requests)
    auth_controller = SquareAuthController(square_service)
    location_controller = SquareLocationController(square_service)
    payment_controller = SquarePaymentController(square_service)
    file = open('amazon_cart.html', 'r')
    scraper = Scraper(file.read(), 'amazon')
    file.close()
    user_id = '27b47c9a-dfaf-4a60-b2de-ef6744ff27d0'
    location_id = 'LV7C5754RDGTN'
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
            "payment_note": "Test Note",
            "line_items": [
                {
                    "name": "Test Name",
                    "quantity": "1",
                    "item_type": "ITEM",
                    "base_price_money": {
                        "amount": 10000,
                        "currency": "USD"
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

    def test_scrape(self):
        result = self.scraper.scrape_amazon()
        self.assertTrue(result is not None)


if __name__ == '__main__':
    unittest.main()
