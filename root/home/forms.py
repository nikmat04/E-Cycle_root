from django import forms
from .models import book
from django.forms import ModelForm
class BookForm(ModelForm):
    class Meta:
        Model = book
        fields = ['fullname', 'email','contactnum','address','pincode','device','defect','date']
