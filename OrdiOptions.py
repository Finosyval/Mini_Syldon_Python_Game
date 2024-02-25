import random
import Effets

def ChoixOrdi (nombreBatonnetsASonTour) :
    
    if nombreBatonnetsASonTour % 4 ==0 :
        return random.randint (1,3)
    else :
        return nombreBatonnetsASonTour % 4


def OrdiCommence (NbBat) : 
    import PlayerOptions #pour eviter les erreurs d'import circulaire
    while True :
        Phr = "Bâtonnets actuels : " + str(NbBat) + " " + "|" * NbBat + "\n"
        Effets.AffichageLentePhrase(Phr)
        
        BatonnetsTiresParOrdi =ChoixOrdi(NbBat)
        if BatonnetsTiresParOrdi > NbBat :
            BatonnetsTiresParOrdi = NbBat
        Effets.AffichageLentePhrase("L'ordi a choisi" + " " + str (BatonnetsTiresParOrdi) + "\n\n")
        NbBat -= BatonnetsTiresParOrdi
        if NbBat ==0 :
            Effets.FinDuJeu(" l'ordi ")
            break
        
       
        BatonnetsTiresParLeJoueur=PlayerOptions.ChoixBatonnets()
        if BatonnetsTiresParLeJoueur > NbBat :
            BatonnetsTiresParLeJoueur = NbBat
        NbBat -= BatonnetsTiresParLeJoueur
        if NbBat ==0 :
            Effets.FinDuJeu(" vous ")
            break
        
       
#OrdiCommence (22)