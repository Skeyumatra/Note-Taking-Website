from django.urls import path
from . import views
urlpatterns = [
    path("",views.entry,name="entry"),
    path("home/<name>/",views.homePage,name="home"),
    path("notes/<name>/<pk>/",views.note, name="note"),
    path("exit/<name>",views.exit,name="exit")
]