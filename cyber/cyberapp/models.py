from django.contrib.auth.models import User
from django.db import models


# # Create your models here.
# class Document(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     pdf = models.FileField(upload_to='pdfs/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username}'s PDF"
