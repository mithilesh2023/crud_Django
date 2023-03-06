from django.db import models

# Create your models here.
class Emplyee(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.IntegerField(max_length=20)

    def __str__(self):
        
        return self.name