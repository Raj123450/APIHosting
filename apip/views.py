from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from apip.models import Company, Employee
from apip.serializers import CompanySerializers, EmpolyeeSerializers
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers

    @action(detail=True, methods=['get'])
    def empolyees(self, request, pk=None):
        try:
            company=Company.objects.get(pk=pk)
            empe=Employee.objects.filter(company=company)
            emps_serializer=EmpolyeeSerializers(empe, many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
            'message':'Data might not be exist'
            })
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmpolyeeSerializers
