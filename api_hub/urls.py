from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from . import views

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
    path('register', views.employee_create, name='employee-register'),
    path('employees', views.employee_list, name='employee-list'),
    path('employees/edit/<int:pk>/',
         views.employee_edit,   name='employee-edit'),
    path('employees/delete/<int:pk>/',
         views.employee_delete, name='employee-delete'),
]
