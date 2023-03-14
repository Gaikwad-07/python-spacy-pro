from django.db import models

# Create your models here.
class department(models.Model):
        id=models.IntegerField(primary_key=True)
        dept=models.CharField(max_length=50)
        def __str__(self):
                return self.dept
class employee(models.Model):
        ename = models.CharField(max_length=50)
        empid=models.IntegerField()
        email=models.EmailField(max_length=50)
        password=models.CharField(max_length=50)
        mobile=models.IntegerField()
        dep=models.ForeignKey(department,on_delete=models.CASCADE)
        
        def __str__(self):
                return self.ename

        