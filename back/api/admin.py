from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import MedicineResource  # Импортируйте MedicineResource из правильного места

from .models import User, Imperfection, SkinType, Question, Answer, Medicine, UserTestResult,CategoryProduct,ImageProduct,Order,OrderItem


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

@admin.register(Medicine)
class MedicineAdmin(ImportExportModelAdmin):
    resource_class = MedicineResource
    list_display = ('name', 'description', 'treats', 'img', 'price', 'category')