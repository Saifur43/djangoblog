from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


