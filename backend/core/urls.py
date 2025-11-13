from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyInfoViewSet

router = DefaultRouter()
router.register(r'company-info', CompanyInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
