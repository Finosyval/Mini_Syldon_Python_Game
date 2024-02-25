import random
import Effets
import TwoPlayers
def JouerContreHumain () :
    
    #les deux joueurs entre leurs noms / pseudos
    NomJoueur1 = str(input (" Que le Joueur 1 entre son nom : "))
    NomJoueur2 = str(input (" Que le Joueur 2 entre son nom : "))
    
    NbreBatonnets = random.randint (20,30) #Nombre de bâtonnets pour cette partie
    Effets.AffichageLentePhrase("Dans cette partie, il y aura " + str (NbreBatonnets) + " bâtonnets" + "\n")
    Effets.AffichageLentePhrase ("Bien, il reste à décider de qui commence pour ce jeu. Bien evidemment ce sera aléatoire" + "\n")
    Effets.AffichageLentePhrase("Selection de celui qui a le trait" + "\n")
    TraitA = random.randint(0,1) #0 pour Joueur 1, 1 pour Joueur 2
    if TraitA == 0 :
        Effets.AffichageLentePhrase(NomJoueur1 + " commence " + "\n")
        TwoPlayers.Joueur1Commence(NbreBatonnets, NomJoueur1,NomJoueur2)
    
    
    else :
        Effets.AffichageLentePhrase(NomJoueur2 + " commence + \n")
        TwoPlayers.Joueur2Commence(NbreBatonnets,NomJoueur1,NomJoueur2)