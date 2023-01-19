from django import forms 
from django.contrib.auth.models import User
from .models import Profile, Card
from cloudinary.forms import CloudinaryFileField

class AddCardInfo(forms.ModelForm):
  cardnumber = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Card Number'}))
  amount = forms.IntegerField(required=True, label_suffix=" : ", min_value=0, max_value=10000,widget=forms.NumberInput(attrs={'class': 'form-control mb-4', 'placeholder':'Amount'}))

  class Meta:
        model = Card
        fields = ['cardNumber', 'amount']