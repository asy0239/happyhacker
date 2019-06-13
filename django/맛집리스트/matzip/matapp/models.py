from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.user_id} - {self.body}'

