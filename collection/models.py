from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Item(models.Model):
    title = models.CharField(max_length=225)
    location = models.TextField()
    collector = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='item_upload',
        default=True
    )
    horizon = models.TextField()
    body = models.TextField()
    date = models.DateField()
    image = CloudinaryField('image', null=False)
    slug = models.SlugField(null=False, unique=True)


def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse("article_detail", kwargs={"slug": self.slug})
