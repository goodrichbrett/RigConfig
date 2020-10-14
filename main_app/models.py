from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
COMPONENTS = (
    ('CPU', 'Processor'),
    ('GC', 'Graphics Card'),
    ('PSU', 'Power Supply'),
    ('RAM', 'RAM'),
    ('MB', 'Motherboard'),
    ('CASE', 'Case')
)


class Part(models.Model):
    name = models.CharField(max_length=50)
    component = models.CharField(
        choices=COMPONENTS, default=COMPONENTS[0][0], max_length=4)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"part_id": self.id})
