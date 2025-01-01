from django.test import TestCase
from hotel_data.models import Hotel, GeneratedTitleDesc, SummaryTable

class HotelModelTest(TestCase):
    def test_hotel_str(self):
        hotel = Hotel.objects.create(
            city_id=1, hotel_id=101, city_name="Test City",
            title="Test Hotel", price=100.50, rating="4.5",
            room_type="Deluxe", location="Test Location",
            latitude="12.345", longitude="67.890", image="test.jpg"
        )
        self.assertEqual(str(hotel), "Test Hotel")

class GeneratedTitleDescTest(TestCase):
    def test_generated_title_desc_str(self):
        generated_title_desc = GeneratedTitleDesc.objects.create(
            hotel_id=101, title="Test Title",
            generated_title="Generated Title",
            description="Test Description"
        )
        self.assertEqual(str(generated_title_desc), "Generated Title for Hotel 101")

class SummaryTableTest(TestCase):
    def test_summary_table_str(self):
        summary = SummaryTable.objects.create(
            hotel_id=101, summary="Test Summary",
            rating=4.0, review="Test Review"
        )
        self.assertEqual(str(summary), "Summary for Hotel 101")
