from django.db import models
from django.db.models import Model, CharField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(Model):
    name = CharField(max_length=30, unique=True, blank=False)
    description = CharField(max_length=120, blank=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

