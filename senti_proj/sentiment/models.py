from django.db import models

# Create your models here.
class Sentiment(models.Model):
  event = models.TextField()
  date = models.DateTimeField()
  text = models.TextField()
  sentiment = models.CharField(max_length=10)