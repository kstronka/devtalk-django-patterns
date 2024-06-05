from django.urls import path
from .views import OrderViewSet


urlpatterns = [
    path('create/', OrderViewSet.as_view({'post': 'create'}), name='place-order')
]
