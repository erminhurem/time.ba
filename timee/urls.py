from django.urls import path
from . import views

app_name = "timee"

urlpatterns = [
    path('', views.index, name="homepage"),
    path('sport/', views.sport, name="sport"),
    path('magazin/', views.magazin, name="magazin"),
    path('bih/', views.bih_category, name='bih_category'),
    path('ekonomija/', views.ekonomija_category, name="ekonomija_category"),
    path('balkan/', views.balkan_category, name="balkan_category"),
    path('svijet/', views.svijet_category, name="svijet_category"),
    path('sarajevo/', views.sarajevo_category, name="sarajevo_category"),
    path('hronika/', views.hronika_category, name="hronika_category"),
    path('kultura/',views.kultura_category, name="kultura_category"),
    path('scena/', views.scena_category, name="scena_category"),
    path('sport/fudbal/', views.fudbal_category, name="fudbal_category"),
    path('sport/kosarka/', views.kosarka_category, name="kosarka_category"),
    path('sport/tenis', views.tenis_category, name="tenis_category"),
    path('sport/ostalo', views.ostalo_category, name="ostalo_category"),
    path('magazin/zabava', views.zabava_category, name="zabava_category"),
    path('magazin/automobili', views.automobili_category, name="automobili_category"),
    path('magazin/tehnologija', views.tehnologija_category, name="tehnologija_category"),
    path('magazin/lifestyle', views.lifestyle_category, name="lifestyle_category"),
    path('magazin/hrana', views.hrana_category, name="hrana_category"),
    path('magazin/intima', views.intima_category, name="intima_category"),
    path('najnovije_vijesti/',views.najnovije_vijesti, name="najnovije_vijesti"),
    path('izvori/', views.izvori, name="izvori"),
    path('film/', views.film, name="film"),
 

]