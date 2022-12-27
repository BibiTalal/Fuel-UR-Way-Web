from django.contrib.auth.models import User
from tabnanny import check
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from django import forms
User = get_user_model()


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput()
        }


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class OrderForm(forms.ModelForm):

    class Meta:

        model = Order
        fields = ["user", "carType", "fuelType", "litter",
                  "address", "date", "time", "price", "payed", "status"]

        def __init__(self):

            self.fields["status"]
