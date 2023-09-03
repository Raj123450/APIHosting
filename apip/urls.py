from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from apip.views import CompanyViewSet, EmployeeViewSet
router=routers.DefaultRouter()
router.register(r'Companies', CompanyViewSet)
router.register(r'empolyees', EmployeeViewSet)
urlpatterns = [
   path('', include(router.urls))
]
#Company/company_id/employees
