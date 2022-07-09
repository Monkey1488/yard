from django.contrib import admin
from .models import GPoint

# Register your models here.
class GoogleAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment', 'activate', "total_number", "start_time", "end_time", "created_at", "updated_at")
    # list_editable = ('activate',"total_number", "start_time",)

admin.site.register(GPoint, GoogleAdmin)