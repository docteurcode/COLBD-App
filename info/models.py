from django.db import models
from django.contrib.auth.models import User

from area.models import Distic, Thana
from package.models import Package

# Create your models here.

STATUS_CHOICES = (
    ('1', "Pending"),
    ('2', "Active"),
    ('3', "Hold"),
    ('4', "Closed"),
)


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=False)
    pn_number = models.IntegerField()
    birth_date = models.DateField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='1')
    distic = models.ForeignKey(Distic, on_delete=models.SET_NULL, null=True)
    thana = models.ForeignKey(Thana, on_delete=models.SET_NULL, null=True)
    zip_code = models.CharField(max_length=100)
    address = models.CharField(max_length=800)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    ref_by = models.CharField(max_length=50, blank=True)
    active_on = models.DateField(blank=True)
    expired_at = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
