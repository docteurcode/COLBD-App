from django.contrib import admin

from .models import Info
# Register your models here.


class InfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name',
                    'status', 'package', 'expired_at')
    list_filter = ('package', 'status', 'distic', 'thana')
    search_fields = ('user', 'first_name', 'pn_number', 'ref_by')
    list_per_page = 50


admin.site.register(Info, InfoAdmin)
