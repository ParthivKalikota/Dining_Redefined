from django.db import models
class Customer(models.Model):
    Restaurant_name = models.CharField(max_length=100)
    About = models.TextField()
    # no_of_items : models.IntegerField
    location = models.TextField()
    phone_no = models.TextField()
    email = models.TextField()
    template = models.CharField(max_length=50)
