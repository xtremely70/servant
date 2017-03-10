from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Style, Supplier, Item, Rawmaterial
from .forms import SupplierForm

# Create your views here.
"""
def index(request):
    context = {}
    return render(request, 'inventory/index.html', context)
"""

class MainView(TemplateView):
    template_name = 'inventory/index.html'

class SupplierView(ListView):
    template_name = 'inventory/supplier.html'
    model = Supplier

class SupplierDetailView(DetailView):
    template_name = 'inventory/supplier_detail.html'
    model = Supplier

class InsertSupplier(View):
    """
    새로운 공급업체 핸들링
    """
    form_class = SupplierForm
    template_name = 'inventory/supplier_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/')
