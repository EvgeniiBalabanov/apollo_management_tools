from django.contrib import admin
from .models import AccessSetting, Setting

class SettingAdmin(admin.ModelAdmin):
    list_display = ('access_setting', 'name')

admin.site.register(AccessSetting)
admin.site.register(Setting, SettingAdmin)