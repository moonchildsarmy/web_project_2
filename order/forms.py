from django import forms
from django.forms.widgets import TextInput, EmailInput
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'email']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
        }