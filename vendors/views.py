from django.http import HttpResponse


def v_index(request):
    return HttpResponse("Hello Geeks")

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import VendorRegistrationForm

def vendor_registration(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            vendor = user.vendor
            vendor.name = form.cleaned_data.get('name')
            vendor.address = form.cleaned_data.get('address')
            vendor.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('v_index')
            print("Success")
    else:
        form = VendorRegistrationForm()
        print("failed")
    return render(request, 'vendors/vendor_registration.html', {'form': form})
