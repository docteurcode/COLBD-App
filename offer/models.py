from django.db import models

# Create your models here.


class Offer (models.Model):
    title = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    end_at = models.DateField()
    discription = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
