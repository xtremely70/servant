from django.conf.urls import url
from inventory import views

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='index'),
    url(r'^supplier/$', views.SupplierView.as_view(), name='supplier'),
    url(r'^supplier/new/$', views.InsertSupplier.as_view(), name='insert_supplier'),
    url(r'^supplier/(?P<pk>\d+)/$', views.SupplierDetailView.as_view(), name='supplier_detail'),
]
