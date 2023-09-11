from django.contrib import admin
from .models import Captures
from django.utils.html import format_html
from django.urls import reverse

class CapturesAdmin(admin.ModelAdmin):
    #ajout des champ visible dans le menu Admin
    list_display = ('interface', 'nb_packet', 'date_heure', 'fait', 'executeScript')

    def executeScript(self, obj):
        #rediréction vers la view "executeScript"
        url = reverse('executeScript', kwargs={'id': obj.id})
        return format_html('<a href="{}">Exécuter le script</a>', url)

    #ajout d'un label pour la nouvelle collone
    executeScript.short_description = 'Executer'

#liaison entre le model et la class
admin.site.register(Captures, CapturesAdmin)

