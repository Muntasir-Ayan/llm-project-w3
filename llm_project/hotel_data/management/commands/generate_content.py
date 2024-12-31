from django.core.management.base import BaseCommand
from hotel_data.models import Hotel
from hotel_data.utils import generate_title_and_description, generate_summary_and_review
from django.db import connection

class Command(BaseCommand):
    help = 'Generate titles, descriptions, summaries, and reviews for hotels'

    def handle(self, *args, **kwargs):
        # Fetch hotels using raw SQL
        hotels = self.fetch_hotels_raw_sql()

        if not hotels:
            self.stdout.write(self.style.WARNING('No hotels found in the database.'))
            return

        for hotel in hotels:
            # Extract data from each hotel row
            hotel_id, title, city_name, price, rating, room_type, location, latitude, longitude, image = hotel
            # Create a hotel object-like structure to pass to the generate functions
            hotel_obj = Hotel(
                hotel_id=hotel_id,
                title=title,
                city_name=city_name,
                price=price,
                rating=rating,
                room_type=room_type,
                location=location,
                latitude=latitude,
                longitude=longitude,
                image=image
            )

            self.stdout.write(f"Generating content for hotel {hotel_id}...")

            # Generate and store title and description
            generate_title_and_description(hotel_obj)

            # Generate and store summary, rating, and review
            generate_summary_and_review(hotel_obj)

        self.stdout.write(self.style.SUCCESS('Successfully generated content for all hotels'))

    def fetch_hotels_raw_sql(self):
        # Function to fetch hotels from database using raw SQL
        with connection.cursor() as cursor:
            cursor.execute("SELECT hotel_id, title, city_name, price, rating, room_type, location, latitude, longitude, image FROM hotels;")
            hotels = cursor.fetchall()
        return hotels
