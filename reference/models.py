from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FreeReference(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True)
    ref_code = models.CharField(max_length=50, unique=True)
    pn_number = models.IntegerField()
    bkash_num = models.IntegerField(blank=True)
    bkash_payment = models.BooleanField(default=False)
    mobile_recharge = models.BooleanField(default=False)
    num_of_ref = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Reference(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    num_of_ref = models.IntegerField(default=0)
    bkash_num = models.IntegerField()
    bkash_payment = models.BooleanField(default=False)
    mobile_recharge = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
