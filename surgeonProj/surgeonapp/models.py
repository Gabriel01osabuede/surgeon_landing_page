from django.db import models

class subscriber(models.Model):
    email = models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return self.email