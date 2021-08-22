<<<<<<< HEAD
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import models, forms


class AddAddress(generic.View):
    def get(self, request):
        form = forms.AddAddressForm()
        return render(request, 'add_address.html', {'form': form})
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
