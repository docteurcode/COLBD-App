from django.db import models

# Create your models here.

SPEED_CHOICES = (
    ('1', '10'),
    ('2', '20'),
    ('3', '25'),
    ('4', '30'),
    ('5', '40'),
    ('6', '50'),
    ('7', '70'),
    ('8', '100'),
)


class Package(models.Model):
    name = models.CharField(max_length=300)
    speed = models.IntegerField()
    price = models.IntegerField()
    bdix = models.CharField(max_length=10, choices=SPEED_CHOICES, default='6')
    youtube = models.CharField(
        max_length=10, choices=SPEED_CHOICES, default='6')
    facebook = models.CharField(
        max_length=10, choices=SPEED_CHOICES, default='6')
    ftp = models.CharField(max_length=10, choices=SPEED_CHOICES, default='8')
    is_pub = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PackageOffer(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    month = models.IntegerField()
    installation_charge = models.IntegerField()

    def __str__(self):
        return str(self.package)
