
def ChoixJoueur (joueur):
    """Le joueur doit choisir entre 1 , 2 , ou 3. Si il choisit autre chose, il deva retaper encore et encore"""
    while True:
        try:
            BatonnetsJoueur = int(input("\n"+joueur + ", choisis le nombre de bâtonnets que tu veux retirer entre 1 , 2 ou 3 : "))
            if BatonnetsJoueur == 1 or  BatonnetsJoueur == 2 or BatonnetsJoueur == 3:
                break
            else:
                print("Choisis strictement entre 1, 2 ou 3. Reessaie.")
        except ValueError:
            print("Par pitié choisis au moins une valeur entière")
    return BatonnetsJoueur


def Joueur1Commence (NbBat, Name1,Name2):
    import Effets
    while True :
        Phr = "Bâtonnets actuels : " + str(NbBat) + " " + "|" * NbBat + "\n\n"
        Effets.AffichageLentePhrase(Phr)
        
        BatonnetsTiresParJoueur1 = ChoixJoueur(Name1) #Le joeuur 1 commence
        if BatonnetsTiresParJoueur1 > NbBat :#si le nombre de batonnets tirés par le joueur dépasse 
            # ... le nombre de batonnets restant
            BatonnetsTiresParJoueur1 = NbBat
            print("Il ya moins de ", BatonnetsTiresParJoueur1, "bâtonnets. On convertit alors votre choix à ", NbBat, " qui est le nombre de bâtonnets restant")
        
        NbBat -= BatonnetsTiresParJoueur1
        if NbBat ==0 :
            Effets.FinDuJeu(Name1)
            break
        
       
        BatonnetsTiresParJoueur2=ChoixJoueur(Name2) #Au tour du joueur 2
        if BatonnetsTiresParJoueur2 > NbBat :
            BatonnetsTiresParJoueur2 = NbBat
            print("Il ya moins de ", BatonnetsTiresParJoueur2, "bâtonnets. On convertit alors votre choix à ", NbBat, " qui est le nombre de bâtonnets restant")
        NbBat -= BatonnetsTiresParJoueur2
        if NbBat ==0 :
            Effets.FinDuJeu(Name2)
            break



def Joueur2Commence (NbBat,Name1,Name2):
    #Je ne fais aucun commentaire ici parce que c'est exactement comme la fonction precedente
    #.. à difference près que l'ordre de commencenemt est inversé
    import Effets
    while True :
        Phr = "Bâtonnets actuels : " + str(NbBat) + " " + "|" * NbBat + "\n\n"
        Effets.AffichageLentePhrase(Phr)
        BatonnetsTiresParJoueur2=ChoixJoueur(Name2)
        if BatonnetsTiresParJoueur2 > NbBat :
            BatonnetsTiresParJoueur2 = NbBat
            print("Il ya moins de ", BatonnetsTiresParJoueur2, "bâtonnets. On convertit alors votre choix à ", NbBat, " qui est le nombre de bâtonnets restant")
        NbBat -= BatonnetsTiresParJoueur2
        if NbBat ==0 :
            Effets.FinDuJeu(Name2)
            break
        BatonnetsTiresParJoueur1 = ChoixJoueur(Name1)
        if BatonnetsTiresParJoueur1 > NbBat :
            BatonnetsTiresParJoueur1 = NbBat
            print("Il y a moins de ", BatonnetsTiresParJoueur1, "bâtonnets. On convertit alors votre choix à ", NbBat, " qui est le nombre de bâtonnets restant")
        
        NbBat -= BatonnetsTiresParJoueur1
        if NbBat ==0 :
            Effets.FinDuJeu(Name1)
            break       

        
"""Histoire de tester le code actuel """
#Joueur1Commence(20,"Alex", "Jeanne")
#Joueur2Commence (20, "Alex", "Jeanne")