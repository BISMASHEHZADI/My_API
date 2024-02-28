from django.db import models

# Create your models here.
class My_Model(models.Model):
    title = models.CharField(max_length = 150)
    product_name = models.CharField(max_length = 150)




def __str__(self):
    return self.product_name