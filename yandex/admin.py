from django.contrib import admin
from .models import Point
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class YandexAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment', 'activate', "total_number", "start_time", "end_time", "created_at", "updated_at")
    list_editable = ('activate',"total_number", "start_time",)

admin.site.register(Point, YandexAdmin)

# admin.site.site_title("Администрирование")
