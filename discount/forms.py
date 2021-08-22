from django import forms


class CodeDiscountForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'id': 'discount_code'}))
