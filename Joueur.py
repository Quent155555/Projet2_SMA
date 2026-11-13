#Strat : 
#0 = Coop et 1 = D
from random import *
class Joueur :

    def __init__(self, strat):
        self.preference = None#Les preferences du joueur
        self.score = 0
        self.choix = None
        
        self.strat = strat
        self.historique_choix = []#Pour regarder les choix de l'autre
        self.historique_adverse = []

    def decision(self) :
        #Calcul avec une stratégie
        strat = self.strat
        hist = self.historique_choix
        hist_adv = self.historique_adverse
        TFT = False
        
        #ALL-D
        if (strat == "ALL-D") :
            nouveau_choix = 1#D
        
        #RANDOM
        elif (strat == "RANDOM") :
            piece = randint(1,2)
            if (piece == 1) :
                nouveau_choix = 0#C
            else :
                nouveau_choix = 1#D
        
        #TIT-FOR-TAT
        elif (strat == "TIT-FOR-TAT") :
            if(hist == []):
                nouveau_choix = 0#C
            else :
                n = len(hist_adv)
                nouveau_choix = hist_adv[n-1]
        
        #TESTER
        elif (strat == "TESTER") :
            if(hist == []):
                nouveau_choix = 1#D
            else :
                n = len(hist_adv)
                if hist_adv[n-1] != 1 and not TFT:
                    if hist[n-1] == 1 :
                        nouveau_choix = 0
                    else :
                        if hist[n-2] == 0:
                            nouveau_choix = 1
                        else :
                            nouveau_choix = 0
                else :#Si au coup precedent, l'adversaire a choisit de D, donc de riposter, alors on devient TIT-FOT-TAT
                    TFT = True
                    nouveau_choix = hist_adv[n-1]

        #JOSS
        elif (strat == "JOSS") :
            if(hist == []):
                nouveau_choix = 0#C
            else :
                n = len(hist_adv)
                nouveau_choix = hist_adv[n-1]
            if nouveau_choix == 0 :
                mutation = randint(1,10)
                if mutation == 1 :
                    nouveau_choix = 1
        
        #ALLC
        else :
            nouveau_choix = 0
            
        self.choix = nouveau_choix 