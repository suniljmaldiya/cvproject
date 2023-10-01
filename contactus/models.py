import email
from pydoc import describe
from django.db import models

class contactus(models.Model):
    sno = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    email   = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    desc = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)





# Create your models here.
