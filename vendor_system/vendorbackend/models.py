from django.db import models
import json

class Photographer(models.Model):

    # Queries vendors that are only active 
    class PhotographerObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset.filter(status='active')

    options = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )

    # vendor_id = models.IntegerField(primary_key=True)
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




'''
    {
        "vendor_id": 1,
        "company_name": "2",
        "address": "3",
        "phone_number": "4",
        "email": "nick@findingspaces.com",
        "availability": "6",
        "acceptance_score": 7,
        "total_job_offers": 8,
        "rating_score": 9,
        "total_ratings": 10,
        "fixed_cost": 11,
        "distance_cost": "12",
        "size_cost": "13",
        "appointments": "14",
        "status": "active"
    },
    {
        "vendor_id": 10,
        "company_name": "1",
        "address": "2",
        "phone_number": "3",
        "email": "4@findingspaces.com",
        "availability": "5",
        "acceptance_score": 6,
        "total_job_offers": 7,
        "rating_score": 8,
        "total_ratings": 9,
        "fixed_cost": 10,
        "distance_cost": "11",
        "size_cost": "12",
        "appointments": "{13}",
        "status": "active"
    }

'''