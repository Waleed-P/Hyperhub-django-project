from django import forms
from . models import ProductModel,CategoryModel,ProfileModel,InventoryModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields='__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields='__all__'
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields='__all__'


class Regform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'uname','placeholder':'Enter your username'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'fname','placeholder':'Enter your  first name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'lname','placeholder':'Enter your last name'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'email','placeholder':'Enter your email address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'pass1','placeholder':'Enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'pass2','placeholder':'Retype password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class InventoryForm(forms.ModelForm):
    class Meta:
        model=InventoryModel
        fields='__all__'