from django.db import models

# Create your models here.

class book(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    contactnum = models.IntegerField()
    address = models.TextField()
    pincode = models.IntegerField()
    device = models.CharField(max_length=100)
    defect = models.TextField()
    date = models.DateField()
