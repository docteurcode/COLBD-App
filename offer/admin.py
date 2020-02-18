from django.contrib import admin

from .models import Offer
# Register your models here.


class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'end_at', "image")
    search_fields = ('title', 'discription')


admin.site.register(Offer, OfferAdmin)
