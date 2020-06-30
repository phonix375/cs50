from django.contrib import admin

from .models import Run, userFrends, runLocations

# Register your models here.

admin.site.register(Run)
admin.site.register(userFrends)
admin.site.register(runLocations)

