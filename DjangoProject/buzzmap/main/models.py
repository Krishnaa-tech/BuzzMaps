from django.db import models

class users(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_description = models.TextField(max_length=40)

    table Students{
        input 
    }