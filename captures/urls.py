from django.urls import path
from . import views

from . import views

urlpatterns = [
    path("", views.index, name="index"), #index de la page
    path("afterSubmit/", views.afterSubmit, name="afterSubmit"), #une fois que le formulaire est envoyé
    path("run-script/<int:id>/", views.executeScript, name='executeScript'), #redirection vers la fonction executeScript de la view a l'appuie du bouton "Executer le script"
]