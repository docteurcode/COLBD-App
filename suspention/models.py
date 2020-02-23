from django.db import models
from django.contrib.auth.models import User

MONTH_CHOICES = (
    ("1", "January"),
    ("2", "February"),
    ("3", "March"),
    ("4", "April"),
    ("5", "May"),
    ("6", "June"),
    ("7", "July"),
    ("8", "Auguest"),
    ("9", "September"),
    ("10", "Octobor"),
    ("11", "November"),
    ("12", "December"),
)

# Create your models here.


class SuspentionTemporary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_month = models.CharField(max_length=100, choices=MONTH_CHOICES)
    num_of_month = models.IntegerField(default=1)
    approve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class SuspentionPermanently(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    device_collect_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
