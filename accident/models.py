from django.db import models
from django.contrib.auth.models import User


class AccidentReport(models.Model):
    VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('bus', 'Bus'),
        ('truck', 'Truck'),
        ('auto', 'Auto'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='report/', blank=True, null=True)
    reported_at = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='accident_videos/', blank=True, null=True)

    # Additional fields
    name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    vehicle_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.vehicle_type}"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
