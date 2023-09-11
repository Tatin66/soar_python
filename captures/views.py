from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from scapy.all import *
from .models import Captures
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
  interfaces = get_if_list()  #récupération de la liste des intérfaces disponnibles

  #création de la liste des intérface d'apres get_if_list()
  interface_options = [(interface, interface) for interface in interfaces]

  template = loader.get_template('captures/index.html') #lien vers le template
  context = {
    'interface_options': interface_options, #ajout des variables a envoyer a la vue
  }
  return HttpResponse(template.render(context, request))

@csrf_exempt #ne pas utiliser le csrf
def afterSubmit(request):
  is_good = False
  if request.method == 'POST':
    #récupération des valeurs du formulaire
    interface = request.POST.get('interface')
    nombre_packets = request.POST.get('nombre_packets')
    date_heure = request.POST.get('date_heure')

    #verrifications
    try:
      nombre_packets = int(nombre_packets)
    except ValueError:
      template = loader.get_template('captures/fail.html')
      return HttpResponse(template.render())

    if interface != "" and nombre_packets > 0:
      is_good = True

    if is_good:
      #creation d'un nouvel ellement a ajouter a la base de donées
      capture = Captures(
        interface=interface,
        nb_packet=nombre_packets,
        date_heure=date_heure,
        fait=False
      )
      capture.save() #ajout a la base de donées
      template = loader.get_template('captures/succes.html') #affichage du succes
      return HttpResponse(template.render())
    else:
      template = loader.get_template('captures/fail.html') #affichage de l'erreur
      return HttpResponse(template.render())

  template = loader.get_template('captures/fail.html') #affichage de l'erreur
  return HttpResponse(template.render())

def executeScript(request, id):
  #récupération de l'objet avec le bon id
  capture = Captures.objects.get(id=id)

  interface = capture.interface
  nombre_packets = capture.nb_packet

  #affichage du message de la commade a saisir par l'administrateur pour lancer le sniff
  messages.info(request, f"Merci d'executer la commande : sudo python3 sniffScript.py {interface} {nombre_packets} {id} dans le répertoire soar_python/scapyScript" )

  #changement de l'etat de la collone "FAIT"
  capture.fait = True
  capture.save()

  #retourner sur l'admin
  return redirect('admin:captures_captures_changelist') #redirection vers