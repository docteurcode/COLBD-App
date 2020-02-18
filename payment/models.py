from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PAYMENT_CHOICES = (
    ('1', 'Card'),
    ('2', "Bkash"),
    ('3', "Rocket"),
    ("4", "Ipay"),
    ("5", "Nagad")
)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    payment_type = models.CharField(max_length=100, choices=PAYMENT_CHOICES)
    # made_by = models.ForeignKey(
    #     User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
