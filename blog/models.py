from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        title = self.title
        if self.slug == "":
            self.slug = slugify(title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
