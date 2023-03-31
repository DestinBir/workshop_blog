from django.db import models
from django.urls import reverse
from blog.settings import AUTH_USER_MODEL

class News(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    picture = models.ImageField(upload_to="articles", blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

