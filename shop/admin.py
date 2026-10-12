from django.contrib import admin
from shop.models import producto



class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'fecha_creacion']
   

admin.site.register(producto, ProductoAdmin)

