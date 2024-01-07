# resources.py
from import_export import resources
from api.models import Product


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ('description',)
        fields = ('name', 'description', 'img')
        # skip_unchanged = True
        # use_bulk = True
