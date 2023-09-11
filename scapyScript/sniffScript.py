import sys
from scapy.all import *

#verrification des argument passé
if len(sys.argv) < 4:
    print("Utilisation : python3 monScripte.py monInterface nbPaquet id_capture")
else:
    interface = sys.argv[1]

    try:
        nbPackets = int(sys.argv[2])
    except ValueError:
        print("le nombre de paquet doit etre un nombre entier")
        sys.exit(1)

    try:
        id_capture = int(sys.argv[3])
    except ValueError:
        print("l'id de la demande doit etre un nombre entier")
        sys.exit(1)

    if nbPackets < 1:
        print("le nombre de paquet a récupérer ne peut etre inférieur a 1")
        sys.exit(1)

    nbPaquetsCaptures = 0

    #creatopn du nom du fichier d'apres les informations fournies
    filename = f"sniffs/result_sniff_{interface}_id_{id_capture}.txt"

    #creation du fichier
    with open(filename, "w") as file:

        print(f"Début de la capture sur l'interface {interface}.")
        #tentative de capture
        try:
            for packet in sniff(iface=interface, count=nbPackets):
                nbPaquetsCaptures += 1

                #ecriture des résultat dans le fichier
                file.write(f"Paquet capturé => interface :{interface}, ({nbPaquetsCaptures}/{nbPackets}) : {packet.summary()}" + "\n")

                #la fin de la capture ? si non, continuer
                if nbPaquetsCaptures >= nbPackets:
                    print("Nombre de paquets atteint. Arrêt de la capture.")
                    break
        except KeyboardInterrupt:
            print("Capture interrompue")
        except Exception as e:
            print(f"Erreur a la capture : {e}")
    #fin de la capture
    print(f"Fin de la capture, résultat disponnible dans le fichier {filename}")