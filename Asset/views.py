from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Asset, Notification, Violation
from .serializers import AssetSerializer, NotificationSerializer, ViolationSerializer
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Asset, Notification, Violation

class AssetView(APIView):
    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RunChecksView(APIView):
    def get(self, request):
        current_time = datetime.now()
        assets = Asset.objects.all()
        for asset in assets:
            # Check for reminders
            if (asset.service_time- current_time).total_seconds() / 60 <= 15:
                Notification.objects.create(asset=asset, message="Service time is near")
            if (asset.expiration_time- current_time).total_seconds() / 60 <= 15:
                Notification.objects.create(asset=asset, message="Expiration time is near")
            # Check for violations
            if asset.expiration_time < current_time:
                Violation.objects.create(asset=asset, message="Asset has expired")
            if asset.service_time < current_time and not asset.serviced:
                Violation.objects.create(asset=asset, message="Asset service is overdue")
            return Response({"message": "Checks ran successfully"})


def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'assets/asset_list.html', {'assets': assets})
def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'assets/notification_list.html', {'notifications': notifications})

def violation_list(request):
    violations = Violation.objects.all()
    return render(request, 'assets/violation_list.html', {'violations': violations})


