from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.CharField( max_length= 122)
    password =  models.CharField( max_length= 122)
    address =  models.TextField( max_length= 200)
    address2 = models.TextField( max_length= 200)
    city = models.CharField( max_length= 100)
    state = models.CharField( max_length= 100)
    zip = models.CharField( max_length= 50)
    date = models.DateField()

    def __str__(self):
        return self.email
