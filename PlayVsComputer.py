from random import randint
import Effets
import PlayerOptions
import OrdiOptions
def  JouerContreOrdi () :
    """Fonction qui gère le mode 1 joueur. 
    C'est à dire lorsque l'utilisateur affronte l'ordi"""
    Phrase1 = "Selection du nombre de bâtonnets pour cette partie" + "\n"
    Effets.AffichageLentePhrase(Phrase1)
    
    NbreBatonnets = randint (20,30)
    
    
    Phrase2 = "Dans cette partie, il y aura " + str (NbreBatonnets) + " bâtonnets" + "\n"
    Effets.AffichageLentePhrase(Phrase2)
    
    Effets.AffichageLentePhrase ("Bien, il reste à décider de qui commence pour ce jeu. Bien evidemment ce sera aléatoire" + "\n")
    Effets.AffichageLentePhrase("Selection de celui qui a le trait" + "\n")
    
    
    TraitA = randint(0,1) #0 pour l'ordi, 1 pour l'utilisateur
    if TraitA == 0 :
        Effets.AffichageLentePhrase("L'ordi commence " + "\n")
        OrdiOptions.OrdiCommence(NbreBatonnets)
        
        
    else :
        Effets.AffichageLentePhrase("Tu commences + \n")
        PlayerOptions.JoueurCommence(NbreBatonnets)
        
    
#JouerContreOrdi ()