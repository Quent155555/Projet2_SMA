from Manche import *
from Joueur import *

ZeroTwo = Joueur("ZeroTwo", "TFT")
Quentin = Joueur("Quentin", "JOSS")
Lucas = Joueur("Lucas", "TESTER")
Yassine = Joueur("Yassine", "RANDOM")
ds = Joueur("ds", "ALL-D")
#pigeon = Joueur("pigeon", "")#ALL-C

joueurs = [ZeroTwo, Quentin, Lucas, Yassine, ds]#, pigeon]
t = Tournoi(joueurs, 5, 200)
t.debut_tournoi()
#p = Partie(0, 200, ZeroTwo, Quentin)
#p.rencontre()
n=len(joueurs)
#print(R)
for i in range(n) :
    print("joueur : ", joueurs[i].nom, ", strat :" , joueurs[i].strat, "score : ", joueurs[i].score)