from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="home"),
    path("home" , views.home),
    path("beslenme" , views.beslenme , name="beslenme"),
    path("pre-workout-sec" , views.preworkout , name="pre-workout-sec"),
    path("ogun-1-secim" , views.ogun1secim , name="ogun-1-secim"),
    path("ogun-2-secim" , views.ogun2secim , name="ogun-2-secim"),
    path("ogun-3-secim" , views.ogun3secim , name="ogun-3-secim"),
    path("ogun-4-secim" , views.ogun4secim , name="ogun-4-secim"),
    path("ogun-5-secim" , views.ogun5secim , name="ogun-5-secim"),
    path("ogun-6-secim" , views.ogun6secim , name="ogun-6-secim"),
    path("ogun-7-secim" , views.ogun7secim , name="ogun-7-secim"),
    path("ogun-8-secim" , views.ogun8secim , name="ogun-8-secim"),
    path("beslenmeprogrami" , views.diet , name="dietprogrami"),
    path("urunler" , views.urunlerPage , name = "urunler")

]