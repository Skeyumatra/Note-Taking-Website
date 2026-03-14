from django.urls import path
from . import views
urlpatterns = [
    path("",views.entry,name="entry"),
    path("home/<name>/",views.homePage,name="home"),
    path("notes/<name>/<pk>/",views.note, name="note"),
    path("addNote/<name>/",views.addNote,name="addNote"),
    path("updateNote/<name>/<pk>/",views.updateNote, name="updateNote"),
    path("deleteNote/<name>/<pk>",views.deleteNote,name="deleteNote"),
    path("exit/<name>",views.exit,name="exit"),
]