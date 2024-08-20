from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=50, unique=True)
    size = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True,
        blank = True,
        )
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

#Criei essa classe para várias fotos 
class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, related_name='fotos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='produtos_fotos/')
   
    def __str__(self):
        return f"Foto de {self.product.name}"