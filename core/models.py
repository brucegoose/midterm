from django.db import models

# Create your models here.
class Question(models.Model):
  name = models.CharField(max_length=25)
  email = models.CharField(max_length=30)
  message = models.TextField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
