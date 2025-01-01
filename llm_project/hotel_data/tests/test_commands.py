from django.core.management import call_command
from django.test import TestCase
from hotel_data.models import Hotel, GeneratedTitleDesc, SummaryTable
from unittest.mock import patch

class GenerateContentCommandTest(TestCase):
    def setUp(self):
        Hotel.objects.create(
            hotel_id=101, title="Test Hotel", city_name="Test City",
            price=100.50, rating="4.5", room_type="Deluxe",
            location="Test Location", latitude="12.345",
            longitude="67.890", image="test.jpg"
        )

    @patch('hotel_data.utils.generate_title_and_description')
    @patch('hotel_data.utils.generate_summary_and_review')
    def test_generate_content_command(self, mock_summary, mock_title):
        call_command('generate_content')
        mock_title.assert_called_once()
        mock_summary.assert_called_once()
