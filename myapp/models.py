from django.db import models

class Abc (models.Model):
    name = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)