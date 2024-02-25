import Effets

def ModeDeJeu () :
    while True: #s'assure que la valeur entrée est 1 ou 2
        try:
            modeJoueur = int(input("Choisis 1 pour joueur avec l'ordi et 2 pour jouer avec  quelqu'un : "))
            if modeJoueur == 1 or modeJoueur == 2:
               return modeJoueur 
                
            else:
                print("Choisis strictement entre 1 ou 2. Reessaie.")
        except ValueError:
            print("Par pitié choisis au moins une valeur entière")
        
    

def ChoixBatonnets() :
    while True:#s'assure que la valeur entrée est 1 , 2 ou 3
        try:
            BatonnetsJoueur = int(input("Choisis le nombre de bâtonnets que tu veux retirer entre 1 , 2 ou 3 : "))
            if BatonnetsJoueur == 1 or  BatonnetsJoueur== 2 or BatonnetsJoueur == 3:
                break
            else:
                print("Choisis strictement entre 1, 2 ou 3. Reessaie.")
        except ValueError:
            print("Par pitié choisis au moins une valeur entière")
    return BatonnetsJoueur

def JoueurCommence (NbBat) :
    import OrdiOptions #pour eviter les problèmes liés aux imports circulaires
    while True :
        Phr = "Bâtonnets actuels : " + str(NbBat) + " " + "|" * NbBat + "\n"
        Effets.AffichageLentePhrase(Phr) 
        BatonnetsTiresParLeJoueur=ChoixBatonnets()
        if BatonnetsTiresParLeJoueur > NbBat : # si le nombre de batonnet tirés par le joueur
            #est superieur au nombre de bâtonnets restants
            BatonnetsTiresParLeJoueur = NbBat
            print("Il ya moins de ", BatonnetsTiresParLeJoueur, "bâtonnets. On convertit alors votre choix à ", NbBat, " qui est le nombre de bâtonnets restant")
            
        NbBat -= BatonnetsTiresParLeJoueur
        if NbBat ==0 : #fin de la partie si 0 bâtonnet restant, logique
            Effets.FinDuJeu(" vous ")
            break
        
        BatonnetsTiresParOrdi = OrdiOptions.ChoixOrdi(NbBat)
        if BatonnetsTiresParOrdi > NbBat :
            BatonnetsTiresParOrdi = NbBat
        Effets.AffichageLentePhrase("L'ordi a choisi" + " " + str (BatonnetsTiresParOrdi) + "\n")
        NbBat -= BatonnetsTiresParOrdi
        if NbBat ==0 :
            Effets.FinDuJeu(" l'ordi ")
            break
        
#JoueurCommence (22)