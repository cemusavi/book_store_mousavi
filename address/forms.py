from django import forms
<<<<<<< HEAD

=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from . import models


class AddressForm(forms.Form):
    city = forms.CharField(required=False)
    exact_address = forms.CharField(required=False)
<<<<<<< HEAD


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = (
            'city',
            'exact_address'
        )

    def save(self, commit=True):
        self.instance.user = self.cleaned_data['user']
        self.instance.save()
        return self.instance
=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
