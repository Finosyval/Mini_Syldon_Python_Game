""" Fichier Principal. Le coeur même """

import PlayVsComputer 
import PlayAgainstHuman 
import PlayerOptions 
import Greeting

Greeting.Salutation () #petite salutation
while True  : 
    mode = PlayerOptions.ModeDeJeu() # si le joueur veut affronter l'ordi ou un ami
    
    
    
    if mode == 1 :
        PlayVsComputer.JouerContreOrdi()  #Le joueur affronte l'ordi
    else :
        PlayAgainstHuman.JouerContreHumain() # Le joueur affronte u autre joueur
        
    while True:
        #demande après chaque partie si le(s) joueur(s) veu(len)t rejouer ou quitter le programme
        try: 
            ContinueOuPas = int(input ("Tapez 0 pour fermer le programme et 1 pour jouer une nouvelle partie : "))
            if ContinueOuPas == 0 or ContinueOuPas == 1:
               if ContinueOuPas ==0 :
                   exit ()
               else :
                   break 
                
            else:
                print("Choisis strictement entre 0 ou 1. Reessaie.")
        except ValueError:
            print("Par pitié choisis au moins une valeur entière")
    
    