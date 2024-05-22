from django.shortcuts import render
from .models import ShippingAddress
from django.views.generic import ListView

class ShippingAddressListView(ListView):
    model = ShippingAddress
    template_name = 'shipping_address/shipping_address.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    
def create(request):
    return render(request, 'shipping_address/create.html',{
        
    })


