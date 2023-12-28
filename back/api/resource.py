# resources.py
from import_export import resources
from api.models import Medicine


class MedicineResource(resources.ModelResource):
    class Meta:
        model = Medicine
        import_id_fields = ('description',)
        fields = ('name', 'description', 'img')
        # skip_unchanged = True
        # use_bulk = True
