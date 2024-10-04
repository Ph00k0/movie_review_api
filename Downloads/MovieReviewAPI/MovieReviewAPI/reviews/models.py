from django.db import models

class MovieReview(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title
    
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
