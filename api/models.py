from django.db import models
from django.forms import CharField

class Checkbox(models.Model):

    name = models.CharField(max_length=150)
    is_checked = models.BooleanField(default=False)
