from django.db import models

# Create your models here.

class studentRegister_model(models.Model):
    name=models.CharField(max_length=15)
    register_no=models.IntegerField(unique=True)
    department=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} {self.register_no} {self.department}"