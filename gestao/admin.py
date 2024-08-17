from django.contrib import admin
from .models import Product, Category, ProductPhoto

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'size', 'category', 'views')
    search_fields = ('name', 'code')
    list_filter = ('code',)
    
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)

class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('product','photo')
admin.site.register(ProductPhoto, ProductPhotoAdmin)