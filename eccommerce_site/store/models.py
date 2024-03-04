from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_featured = models.BooleanField(default=False)


    def __str__(self):
        return self.name 