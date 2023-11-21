from django.contrib import admin
from django.urls import path
from Test_Contactanos.vista import contacto
from . import vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', vista.contacto, name='contacto'),

]
