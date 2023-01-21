from django import forms 
from django.contrib.auth.models import User
from .models import Profile, Card
from cloudinary.forms import CloudinaryFileField

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class AddCardInfo(forms.ModelForm):
  cardnumber = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Card Number'}))
  amount = forms.IntegerField(required=True, label_suffix=" : ", min_value=0, max_value=10000,widget=forms.NumberInput(attrs={'class': 'form-control mb-4', 'placeholder':'Amount'}))

  class Meta:
        model = Card
        fields = ['cardNumber', 'amount']

class UpdateProfileForm(forms.ModelForm):
  fullname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Full name'}))
  phonenumber = forms.IntegerField(required=True, label_suffix=" : ", widget=forms.NumberInput(attrs={'class': 'form-control mb-4', 'placeholder':'Phone Number'}))

  class Meta:
        model = Profile
        fields = ['phonenumber', 'fullname']