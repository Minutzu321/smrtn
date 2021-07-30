from django.contrib import admin
from .models import *

class IPAdmin(admin.ModelAdmin):
    list_display = ('ip', 'ora_data')

class UtilizatorAdmin(admin.ModelAdmin):
    list_display = ('nume', 'ultima_logare')

class ExecutabilAdmin(admin.ModelAdmin):
    list_display = ('program', 'ora_data_upload')


admin.site.register(IP, IPAdmin)
admin.site.register(Utilizator, UtilizatorAdmin)
admin.site.register(Executabil, ExecutabilAdmin)
