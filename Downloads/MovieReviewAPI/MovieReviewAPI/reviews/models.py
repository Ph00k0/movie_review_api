from django.db import models

class MovieReview(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title

# Create your models here.
