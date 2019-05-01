from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):

    SCORE_CHOICES = (

        ('★☆☆☆☆', '별 한개'),
        ('★★☆☆☆', '별 두개'),
        ('★★★☆☆', '별 세개'),
        ('★★★★☆', '별 네개'),
        ('★★★★★', '별 다섯개'),
    )
    title = models.CharField(max_length=200)
    contents = models.TextField()
    author = models.CharField(max_length=50)
    score = models.CharField(max_length=10, choices=SCORE_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
