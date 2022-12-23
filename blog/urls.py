from django.urls import path
from . import views

urlpatterns = [
    path("programlar" , views.allPrograms),
    path("koclukal" , views.koclukalPage),
    path("programlar/<int:id>" , views.ProgramPage),
    path("iletisim" , views.iletisimPage , name="iletisim")

]