from django.contrib import admin
import nested_admin
from .models import (Category,
                    Product, 
                    ProductType, 
                    ProductLine, 
                    Attribute, 
                    AttributeValue, 
                    SeasonalEvent,
                    ProductImage
                    )

# Register your models here.

class ProductImageInline(nested_admin.NestedStackedInline):
    model = ProductImage
    extra = 1
    
class ProductLineInline(nested_admin.NestedStackedInline):
    model = ProductLine
    inlines = [ProductImageInline]
    extra = 1
    
class ProductAdmin(nested_admin.NestedModelAdmin):
    inlines = [ProductLineInline]
    list_display = ('name', 'category', 'stock_status', 'is_active')
    list_filter = ('category', 'stock_status', 'is_active')
    search_fields = ('name',)

class SeasonalEventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', )

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1
    
class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]

class ChildTypeInline(admin.TabularInline):
    model = ProductType
    fk_name = 'parent'
    extra = 1 
    
class ParentTypeAdmin(admin.ModelAdmin):
    inlines = [ChildTypeInline]
    
    def parent_name(self, obj):
        return(obj.parent.name if object else None)
    
class ChildCategoryInline(admin.TabularInline):
    model = Category
    fk_name = 'parent'
    extra = 1 
    
class ParentCategoryAdmin(admin.ModelAdmin):
    inlines = [ChildCategoryInline]
    list_display = ('name', 'parent_name', )
    
    def parent_name(self, obj):
        return(obj.parent.name if obj.parent else None)
    
    
    
admin.site.register(Category, ParentCategoryAdmin)
admin.site.register(ProductType, ParentTypeAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(SeasonalEvent, SeasonalEventsAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductLine)
