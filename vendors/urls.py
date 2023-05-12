from django.urls import path
from . import views

urlpatterns = [
    path('v_index/', views.v_index, name='v_index'),
    path('vendor_registration/', views.vendor_registration, name='vendor_registration'),


]
