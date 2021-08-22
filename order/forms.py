<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from django import forms
from . import models


class ProductForm(forms.Form):
    book = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(initial=1)
<<<<<<< HEAD
=======
=======
from django.conf import settings
from django.forms.models import ModelForm

from .models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['customer']
>>>>>>> d48277e8718ded697aae5e131e4f35d5c59606b4
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
