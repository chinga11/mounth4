from django import forms

class ProductForm(forms.Form):
    name  = forms.CharField(max_length=10, min_length=3)
    description = forms.CharField(max_length=100)
    price = forms.IntegerField()
    photo = forms.ImageField()