from django.db import models

class Simplifier(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField("date_add")