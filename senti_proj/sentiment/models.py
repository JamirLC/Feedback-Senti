from django.db import models

class Sentiment(models.Model):
    event = models.TextField()
    text = models.TextField()
    sentiment = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)  # Ensure this is correct

    def __str__(self):
        return f'{self.id} - {self.event} - {self.sentiment} - {self.created_at}'

