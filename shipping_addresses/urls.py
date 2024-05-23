from django.urls import path
from . import views

app_name = 'shipping_addresses'

urlpatterns = [ 
    path('', views.ShippingAddressListView.as_view(), name='shipping_addresses'),
    path('nuevo', views.create, name='create'),
    path('editar/<int:pk>', views.ShippongAddressUpdateView.as_view(), name='update')
]