from django.contrib import admin

from .models import Bands


class BandsAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


admin.site.register(Bands, BandsAdmin)
