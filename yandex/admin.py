from django.contrib import admin
from .models import Point

class YandexAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     # (None,               {'fields': ['']}),
    #     # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [Point]
    list_display = ('title', 'comment', 'activate', "total_number", "start_time", "end_time", "created_at", "updated_at")
    # list_display_links: ("title", )
    list_editable = ('activate',"total_number", "start_time",)
    # readonly_fields = ()

admin.site.register(Point, YandexAdmin)

# admin.site.site_title("Администрирование")
