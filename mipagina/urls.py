from django.contrib import admin
from django.urls import path
from mi_aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('do/', views.do, name='do'),  # Asegúrate de que esta vista existe
    path('portfolio/', views.portfolio, name='portfolio'),  # Asegúrate de que esta vista existe
    path('contact/', views.contact, name='contact'),  # Asegúrate de que esta vista existe
]
