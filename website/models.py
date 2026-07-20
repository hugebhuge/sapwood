#from django.db import models
from django.db import models


class Consultation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def str(self):
        return self.name
# Create your models here.
