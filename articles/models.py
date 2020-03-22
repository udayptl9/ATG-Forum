from django.db import models
from django.contrib.auth.models import User as Auther
from django.utils import timezone

class Article(models.Model):
    choices = (
        ('Public', 'Public'),
        ('Private', 'Private')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'article_imgs', blank=True)
    privacy = models.CharField(max_length=20, choices=choices, default="Public")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Articles"