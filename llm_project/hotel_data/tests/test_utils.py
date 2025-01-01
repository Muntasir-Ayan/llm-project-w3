from django.test import TestCase
from unittest.mock import patch
from hotel_data.models import Hotel
from hotel_data.utils import parse_generated_text, generate_title_and_description, generate_summary_and_review

class UtilsTest(TestCase):
    def test_parse_generated_text(self):
        text = "**Option 1**Title: Hotel Paradise**Description: A beautiful place to stay**"
        options = parse_generated_text(text)
        self.assertEqual(len(options), 1)
        self.assertEqual(options[0], ("Hotel Paradise", "A beautiful place to stay"))

    @patch('hotel_data.utils.requests.post')
    def test_generate_title_and_description(self, mock_post):
        hotel = Hotel(
            hotel_id=101, title="Test Hotel", city_name="Test City",
            room_type="Deluxe"
        )
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "candidates": [
                {"content": {"parts": [{"text": "**Option 1**Title: Luxury Stay**Description: A great experience**"}]}}
            ]
        }

        generate_title_and_description(hotel)
        self.assertTrue(mock_post.called)

    @patch('hotel_data.utils.requests.post')
    def test_generate_summary_and_review(self, mock_post):
        hotel = Hotel(
            hotel_id=101, title="Test Hotel", city_name="Test City",
            price=100.50, rating="4.5", room_type="Deluxe", location="Test Location"
        )
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "candidates": [
                {"content": {"parts": [{"text": "Test Summary"}]}}
            ]
        }

        generate_summary_and_review(hotel)
        self.assertTrue(mock_post.called)
