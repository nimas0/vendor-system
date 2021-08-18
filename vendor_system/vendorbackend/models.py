from django.db import models
import json

# Database model for each vendor represented as a Python object which will be converted into a MySQL table
class Photographer(models.Model):

    # Queries vendors that are only active 
    class PhotographerObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset.filter(status='active')

    options = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )

    #vendor_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=1000)
    # max length of 1000 is randomly picked to handle dictionary length
    address = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    availability = models.TextField()

    acceptance_score = models.IntegerField()
    total_job_offers = models.IntegerField()

    rating_score = models.IntegerField()
    total_ratings = models.IntegerField()


    fixed_cost = models.IntegerField()
    distance_cost = models.TextField()
    size_cost = models.TextField()

    appointments = models.TextField()

    # Keeps track if the vendor is active or inactive (able to recieve jobs or not)
    status = models.CharField(max_length=10, choices=options, default='active')

    def __str__(self):
        return f"{self.vendor_id}: {self.company_name}"

    # This takes in a JSON object of a dictionary as the parameter and converts it to a string for CharField
    def set_availability(self, new_availability):
        self.availability = json.dumps(new_availability)


    def get_availability(self):
        return json.loads(self.availability)


    # This takes in a JSON object of a dictionary as the parameter and converts it to a string for CharField
    def set_size_cost(self, new_size_cost):
        self.size_cost = json.dumps(new_size_cost)


    def get_size_cost(self):
        return json.loads(self.size_cost)

    # This takes in a JSON object of a dictionary as the parameter and converts it to a string for CharField
    def set_address(self, new_address):
        self.address = json.dumps(new_address)


    def get_address(self):
        return json.loads(self.address)


    # This takes in a JSON object of a dictionary as the parameter and converts it to a string for CharField
    def set_distance_cost(self, new_distance_cost):
        self.distance_cost = json.dumps(new_distance_cost)


    def get_distance_cost(self):
        return json.loads(self.distance_cost)


   # This takes in a JSON object of a dictionary as the parameter and converts it to a string for CharField
    def set_appointments(self, new_appointments):
        self.appointments = json.dumps(new_appointments)


    def get_appointments(self):
        return json.loads(self.appointments)
