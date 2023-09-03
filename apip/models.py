from django.db import models

# Create your models here.
#Creating Company models
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type= models.CharField(max_length=100, choices=(('IT', 'IT'), ('Non IT', 'Non IT'), ('mobile', 'mobile')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name

#Employee Models
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=13)
    about=models.TextField()
    position=models.CharField(max_length=50, choices=(('Manager', 'manager'), 
                                                             ('Software', 'developer'), 
                                                             ('Project leader', 'Poject Managre')))
    company=models.ForeignKey(Company, on_delete=models.CASCADE)

