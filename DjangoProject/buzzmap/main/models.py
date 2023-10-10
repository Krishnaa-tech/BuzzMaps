from django.db import models

# Define the User model for managing users
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Add other user-related fields as needed

    def __str__(self):
        return self.username

# Define the Bus model for managing buses and drivers
class Bus(models.Model):
    bus_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    # Add other bus-related fields as needed

    def __str__(self):
        return self.bus_number

# Define the Route model for managing routes and landmarks
class Route(models.Model):
    route_name = models.CharField(max_length=100)
    landmarks = models.TextField()
    # Add other route-related fields as needed

    def __str__(self):
        return self.route_name

