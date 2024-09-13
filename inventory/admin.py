from django.contrib import admin
from .models import Category, Product, ProductType, ProductLine


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    
#     prepopulated_fields = {'slug':('name',)}

    list_display = ('id', 'name', 'slug')
    search_fields = ['name','slug']
    list_display_links = ('id',)
    list_editable = ('name',)
    

class ProductLineInline(admin.StackedInline):
    model = ProductLine
    extra = 1
    

class ProductAdmin(admin.ModelAdmin):
    inline = [ProductLineInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
