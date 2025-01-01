from django.db import models

# This model represents the original `hotels` table
class Hotel(models.Model):
    city_id = models.IntegerField()
    hotel_id = models.IntegerField()
    city_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class GeneratedTitleDesc(models.Model):
    hotel_id = models.IntegerField(null=True, blank=True)  # Assuming hotel_id is unique
    title = models.CharField(max_length=255)
    generated_title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Generated Title for Hotel {self.hotel_id}"

# Model for storing summaries
class SummaryTable(models.Model):
    hotel_id = models.IntegerField(null=True, blank=True)
    summary = models.TextField()
    rating = models.FloatField()  # Rating between 1 to 5
    review = models.TextField()

    def __str__(self):
        return f"Summary for Hotel {self.hotel_id}"