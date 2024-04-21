from django.db import models

# Create your models here.
class studentclass(models.Model):
    s_class=models.CharField(max_length=50)

    def __str__(self):
        return self.s_class

class studentinfo(models.Model):
    name=models.CharField( max_length=50)
    s_class=models.ForeignKey(studentclass, on_delete=models.CASCADE)
    address=models.CharField( max_length=100,null=True)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return self.name
    