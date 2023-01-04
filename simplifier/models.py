from django.db import models

class Simplifier(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10)
    ip = models.CharField(max_length=128)
    creation_date = models.DateTimeField("date_add")

    def __str__(self):
        return "Urls"

    class Meta:
        verbose_name_plural = "Urls"