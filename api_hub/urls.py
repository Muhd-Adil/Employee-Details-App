from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, EmployeeRegisterView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', EmployeeRegisterView.as_view(), name='employee-register'),
]
