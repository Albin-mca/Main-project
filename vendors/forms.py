from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Vendor


class VendorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('email', 'name', 'address', 'password1', 'password2')

    def save(self, commit=True):
        user = super(VendorRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            vendor = Vendor.objects.create(user=user, name=self.cleaned_data['name'], address=self.cleaned_data['address'])
            vendor.save()
        return user
