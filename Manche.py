from Joueur import *
#une matrice qui correspond au dilemme qui pour chaque case (i,j)
#stocke les actions possible des agents par ex: A={C,D} et B={C,D}
#Alors (0,0) correspond à (C,C)



#O = Coopération et 1 = D
class Manche :
    def __init__(self, id, p1, p2, matrice) :  
        self.id = id
        self.mat_dil = matrice#contient le détail des scores de la partie
        self.joueurs = [p1, p2]#une liste de joueur

        self.finit = False

    def jouer(self) :  
        Z = self.joueurs[0]
        Q = self.joueurs[1]

        #demande au joueur de faire un choix
        Z.decision()
        Q.decision()

        choix_Z = Z.choix 
        choix_Q = Q.choix

        #determine combien chq joueurs va gagner
        pt_Z = self.mat_dil[choix_Z][choix_Q][0]
        pt_Q = self.mat_dil[choix_Z][choix_Q][1]

        Z.score += pt_Z
        Q.score += pt_Q

        #Pour que chaque joueur puisse avoir accès aux précédents coups
        Z.historique_choix.append(choix_Z)
        Z.historique_adverse.append(choix_Q)

        Q.historique_choix.append(choix_Q)
        Q.historique_adverse.append(choix_Z)

        self.finit = True

class Partie :
    def __init__(self, id, nbmanche, p1, p2, matrice) :
        self.id = id
        self.nbmanche = nbmanche
        self.p1 = p1
        self.p2 = p2
        self.matrice = matrice

    def rencontre(self):
        self.p1.reinitialiser()
        self.p2.reinitialiser()
        for i in range(self.nbmanche) :
            manche = Manche(i, self.p1, self.p2, self.matrice)
            manche.jouer()


class Tournoi :
    def __init__(self, joueurs, nbpartie, nbmanche) :
        self.joueurs = joueurs
        self.nbmanche = nbmanche
        self.nbpartie = nbpartie

    def debut_tournoi(self, matrice) :
        n = len(self.joueurs)
        for i in range(n-1) :
            for j in range(i+1, n) :
                for m in range(self.nbpartie):
                    p = Partie(m, self.nbmanche, self.joueurs[i], self.joueurs[j], matrice)
                    p.rencontre()
