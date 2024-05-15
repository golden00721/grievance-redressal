from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    description = models.TextField(max_length=255)

    


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email