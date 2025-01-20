from django.db import models

# Create your models here.
class companyRegister_model(models.Model):
    company_name=models.CharField(max_length=150)
    registration_number=models.IntegerField(null=False)
    email=models.EmailField(max_length=254)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=200)
    industry_type=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.company_name} {self.adress} {self.industry_type}"