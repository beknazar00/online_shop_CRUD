import form
from .models import Order
from django import forms
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'username')


####
from django import forms
from online_shop.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
