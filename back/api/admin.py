from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import ProductResource  # Импортируйте MedicineResource из правильного места

from .models import User, Imperfection, SkinType, Question, Answer, Product, UserTestResult, CategoryProduct, \
    ImageProduct, Order, OrderItem, ProductRating, StoreSettings, SupplierOrder, SupplierOrderItem

admin.site.register(User)
admin.site.register(CategoryProduct)
admin.site.register(Imperfection)
admin.site.register(SkinType)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ImageProduct)
admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(UserTestResult)


@admin.register(Product)
class MedicineAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('name', 'description', 'treats', 'img', 'price', 'category')


class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ('get_product_name', 'get_user_username', 'rating')

    def get_product_name(self, obj):
        return obj.product.name

    get_product_name.short_description = 'Product Name'  # Название столбца

    def get_user_username(self, obj):
        return obj.user.username

    get_user_username.short_description = 'User Username'  # Название столбца


admin.site.register(ProductRating, ProductRatingAdmin)


@admin.register(StoreSettings)
class StoreSettingsAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'currency', 'tax_rate', 'shipping_fee')


class SupplierOrderItemInline(admin.TabularInline):
    model = SupplierOrderItem
    extra = 1


class SupplierOrderAdmin(admin.ModelAdmin):
    inlines = [SupplierOrderItemInline]


admin.site.register(SupplierOrder, SupplierOrderAdmin)
