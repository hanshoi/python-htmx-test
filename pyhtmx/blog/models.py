from django.db import models

# Create your models here.
class Blog(models.Model):
    published = models.DateTimeField("date published", auto_now_add=True)
    modified = models.DateTimeField("date modified", auto_now=True)
    author = models.CharField(max_length=100, blank=True, default="hanshoi")
    title = models.CharField(max_length=200)
    synopsis = models.TextField(null=True)
    content = models.TextField(null=True)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.code

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    message = models.CharField(max_length=1080)
