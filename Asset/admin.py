from django.contrib import admin
from .models import Asset, Notification, Violation

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display=['name', 'service_time','expiration_time','serviced']
    list_filter=['serviced']
    search_fields=['name']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=['asset', 'notification_time','message']
    list_filter=['notification_time']
    search_fields=['asset__name','message']

@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display=['asset', 'violation_time','message']
    list_filter=['violation_time']
    search_fields=['asset__name','message']
# Register your models here.
