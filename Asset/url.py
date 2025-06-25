
from django.urls import path
from .views import AssetView, RunChecksView, asset_list, notification_list, violation_list

urlpatterns = [
    path('assets/',asset_list, name='asset_list'),
    path('notification/', notification_list, name='notification_list'),
    path('violations/', violation_list, name='violation_list'),
    path('api/assets/', AssetView.as_view()),
    path('api/run-checks/', RunChecksView.as_view())
    ]