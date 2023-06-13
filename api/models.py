from django.db import models
from django import forms

class Api(models.Model):
    id = models.IntegerField(("id"), primary_key=True)
    date = forms.DateTimeField(
        input_formats="%Y-%m-%d %H:%M:%S %z"
    )
    user = models.CharField(("user"), max_length=255)
    department = models.CharField(("department"), max_length=255)
    software = models.CharField(("software"), max_length=255)
    seats = models.IntegerField(("seats"))
    amount = models.FloatField(("amount"))

    def __str__(self):
        return self.id

