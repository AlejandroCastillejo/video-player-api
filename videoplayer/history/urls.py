from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import HistoryViewSet

router = routers.DefaultRouter()
router.register('history', HistoryViewSet)

urlpatterns = [
    # path('', HistoryViewSet),
    path('', include(router.urls)),
]