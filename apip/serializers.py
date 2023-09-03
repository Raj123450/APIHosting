from rest_framework import serializers
from apip.models import Company, Employee
#Create Seializers here 
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id= serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields='__all__'

#Create Employees Serializers
class EmpolyeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'