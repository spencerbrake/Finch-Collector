from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


LOCATIONS = (
    ('P', 'Park'),
    ('C', 'City'),
    ('F', 'Forest')
)
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('finches_detail', kwargs={'pk': self.id})

class Finch(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})

class Seen(models.Model):
  date = models.DateField('seen date')
  location = models.CharField(
    max_length=1,
    choices=LOCATIONS,
    default=LOCATIONS[0][0]
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_location_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']