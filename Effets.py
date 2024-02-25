""" A défaut de créer un jeu trop complexe avec des rendus graphiques,
les fonctions de ce fichier servent à rendre le programme on ne peut
plus attractifs """

import time

def Pause (tempsPause) :
    time.sleep (tempsPause)


def Point(nbreDePoints):
    for i in range(nbreDePoints):
        print(".", end=" ",flush = True)  # flush permet le vidage de la memoire tampon ( retire ce parametre et tu verras)
        #VideMemoireTampon()
        time.sleep(2)  # Attendre 2 secondes après l'impression du point
    # Effacer les points
    print("\b" * (nbreDePoints * 2), end="", flush=True)
    
    
def AffichageLentePhrase (Phrase) : 
    for i in Phrase :
        print (i, flush=True,end="")
        Pause(0.1)
    Point(3)

def FinDuJeu (Vainqueur) :
    AffichageLentePhrase(" **** FIIIIIIIINNNNNNNNNNNNNNNN **** " + "\n")
    AffichageLentePhrase ("Le jeu est terminé. Le vainqueur est " + Vainqueur + "\n")
    

#Point(3)  # Appel de la fonction avec 3 points 
