from django.db import models


# Create your models here.
class Questions(models.Model):
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
