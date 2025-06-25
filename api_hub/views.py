from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from django.shortcuts import get_object_or_404, redirect
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('joined_date')
    serializer_class = EmployeeSerializer
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            employees = self.get_queryset()
            return Response({'employees': employees}, template_name='employees.html')
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            employee = self.get_object()
            return Response({'employee': employee}, template_name='register.html')
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('employee-list')
            return Response({'serializer': serializer}, template_name='register.html', status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('employee-list')
            return Response({'employee': instance}, template_name='register.html', status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    def delete_emp(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            instance = self.get_object()
            instance.delete()
            return redirect('employee-list')
        return super().destroy_emp(request, *args, **kwargs)


class EmployeeRegisterView(APIView):
    """
    Handles HTML and JSON rendering for the employee registration form.
    GET  /api/register/ → render empty register.html
    POST /api/register/ → create employee and redirect to list
    """
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'register.html'

    def get(self, request):
        # Render with an empty serializer for form fields
        serializer = EmployeeSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        # Handle form submission or JSON create
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('employee-list')
        return Response({'serializer': serializer}, template_name='register.html', status=status.HTTP_400_BAD_REQUEST)
