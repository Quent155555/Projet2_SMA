from Manche import *
from Joueur import *

ZeroTwo = Joueur("ZeroTwo", "TFT")
Quentin = Joueur("Quentin", "JOSS")
Lucas = Joueur("Lucas", "TESTER")
Yassine = Joueur("Yassine", "RANDOM")
ds = Joueur("ds", "ALL-D")
pigeon = Joueur("pigeon", "ALL-C")#ALL-C
jester = Joueur("Jester", "FARCEUR")
superstition = Joueur("Superstition", "PATTERN")
ds2 = Joueur("ds2", "ALL-D2")

joueurs = [ZeroTwo, Quentin, Lucas, Yassine, ds, jester, superstition, pigeon ,ds2]#on elève allc
t = Tournoi(joueurs, 5, 200)
t.debut_tournoi()
#p = Partie(0, 200, ZeroTwo, Quentin)
#p.rencontre()
n=len(joueurs)
#print(R)
classement = []
for i in range(n) :
    classement.append(joueurs[i])
    print("joueur : ", joueurs[i].nom, ", strat :" , joueurs[i].strat, "score : ", joueurs[i].score)
m = len(classement)
for j in range(m):
    for k in range(j + 1, m):
        if classement[j].score < classement[k].score:
            classement[j], classement[k] = classement[k], classement[j]
print("Classement :")
for i in range(m):
    print(i+1," ", classement[i].strat, ":", classement[i].score)