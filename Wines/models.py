from django.db import models

# Create your models here.

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    Useremail = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class WineProduct(models.Model):
    Products = models.CharField(max_length=100)
    Product_quantity = models.IntegerField() 

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=500)
    submission_time = models.DateTimeField(auto_now_add=True)

class Monitor(models.Model):
    email = models.CharField(max_length=100)
    Login_time = models.DateTimeField(auto_now_add=True)
    Logout_time = models.DateTimeField(auto_now_add=True)