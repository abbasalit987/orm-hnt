from django.db import models


class Blue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color_code = models.CharField(max_length=10)
    size = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
