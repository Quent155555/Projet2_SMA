#Strat : 
#0 = Coop et 1 = D
import random
R = random.Random(123456789)
class Joueur :

    def __init__(self, nom ,strat):
        self.preference = None#Les preferences du joueur
        self.score = 0
        self.choix = None
        self.nom = nom
        
        self.mode_TFT = False

        
        self.strat = strat
        self.historique_choix = []#Pour regarder les choix de l'autre
        self.historique_adverse = []

    def reinitialiser(self) :
        self.choix = None
        self.historique_adverse = []
        self.TFT = False
        self.historique_choix = []

    def decision(self) :
        #Calcul avec une stratégie
        strat = self.strat
        hist = self.historique_choix
        hist_adv = self.historique_adverse
        
        #ALL-D
        if (strat == "ALL-D") :
            nouveau_choix = 1#D
        
        #RANDOM
        elif (strat == "RANDOM") :
            piece = R.randint(1,2)
            if (piece == 1) :
                nouveau_choix = 0#C
            else :
                nouveau_choix = 1#D
        
        #TIT-FOR-TAT
        elif (strat == "TIT-FOR-TAT" or strat == "TFT") :
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
                if hist_adv[n-1] != 1 and not self.mode_TFT:
                    if hist[n-1] == 1 :
                        nouveau_choix = 0
                    else :
                        if hist[n-2] == 0:
                            nouveau_choix = 1
                        else :
                            nouveau_choix = 0
                else :#Si au coup precedent, l'adversaire a choisit de D, donc de riposter, alors on devient TIT-FOT-TAT
                    self.mode_TFT = True
                    nouveau_choix = hist_adv[n-1]

        #JOSS
        elif (strat == "JOSS") :
            if(hist == []):
                nouveau_choix = 0#C
            else :
                n = len(hist_adv)
                nouveau_choix = hist_adv[n-1]
            if nouveau_choix == 0 :
                mutation = R.randint(1,10)
                if mutation == 1 :
                    nouveau_choix = 1

        ################             Nouvelles strats               ##########################

        #FARCEUR
        #Le but est de choisir l'oppose du choix de l'adversaire sur le dernier coup
        elif (strat == "FARCEUR") :
            if hist_adv == [] :
                nouveau_choix = 1
            else :
                n = len(hist_adv)
                nouveau_choix = 1 - hist_adv[n-1]

        #PATTERN
        #Ici on effectue C,C,D,D et on répète
        elif (strat == "PATTERN") :
            n = len(hist)
            patt = n%4
            if patt == 0 or patt == 1 :
                nouveau_choix = 0
            else :
                nouveau_choix = 1

        #ALL-D2
        elif (strat == "ALL-D2") :
            if hist == []:
                nouveau_choix = 0#C
            else :
                nouveau_choix = 1#D

        #ALLC
        else :
            nouveau_choix = 0

        self.choix = nouveau_choix 