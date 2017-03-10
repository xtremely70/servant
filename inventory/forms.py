from django.forms import ModelForm
from .models import Supplier

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'memo', 'status', ]

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({ 'class': 'form-control' })
        self.fields['memo'].widget.attrs.update({ 'class': 'form-control' })
        self.fields['status'].widget.attrs.update({ 'class': 'form-control' })
