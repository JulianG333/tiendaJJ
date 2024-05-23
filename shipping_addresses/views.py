from django.shortcuts import render,redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import ShippingAddress
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .forms import ShippingAddressForm

class ShippingAddressListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_address/shipping_address.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    
class ShippongAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'shipping_address/update.html'
    success_message = 'Direccion actualizada exitosamente'

    def get_success_url(self):
        return reverse('shipping_addresses:shipping_addresses')

    
@login_required(login_url='login')
def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user

        shipping_address.default = not ShippingAddress.objects.filter(user=request.user).exists()

        shipping_address.save()

        messages.success(request, 'Dirección creada exitosamente')
        return redirect('shipping_addresses:shipping_addresses')

    return render(request, 'shipping_address/create.html',{
        'form': form
    })




