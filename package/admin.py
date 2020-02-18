from django.contrib import admin

from .models import Package, PackageOffer

# Register your models here.


class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_pub', 'bdix', 'youtube')
    list_editable = ('is_pub',)
    search_fields = ('name', 'price')
    list_per_page = 50


class PackageOfferAdmin(admin.ModelAdmin):
    list_display = ('package', 'month', 'installation_charge')
    search_fields = ('package',)


admin.site.register(Package, PackageAdmin)
admin.site.register(PackageOffer, PackageOfferAdmin)
