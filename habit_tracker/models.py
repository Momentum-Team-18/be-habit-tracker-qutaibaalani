from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    birthdate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    target_number = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.name


class HabitRecord(models.Model):
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name="HabitRecords"
    )

    record_date = models.DateField(
        auto_now_add=False,
        auto_now=False,
        blank=False,
        null=False,
        default=timezone.now(),
    )
    achieved = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f"{self.habit} on {self.record_date}"
