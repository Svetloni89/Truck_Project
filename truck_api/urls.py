from django.urls import path

from truck_api.views import TruckListApiView, TruckDetailsApiView

urlpatterns = [
    path('', TruckListApiView.as_view(), name='truck list api'),
    path('<int:pk>/', TruckDetailsApiView.as_view(), name='truck details api')
]
