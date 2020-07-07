from django.db import models
from django.urls import reverse


class Tweet(models.Model):
    title=models.CharField(max_length=20)
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body=models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tweet_detail', args=[str(self.id)])




# Create your models here.
