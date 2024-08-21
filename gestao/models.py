from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='categorias_fotos/', blank=False, default='null')

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
    photos = models.JSONField(default=list, blank=False)
    
    def __str__(self):
        return self.name