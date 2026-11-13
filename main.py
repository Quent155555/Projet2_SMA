from Manche import *
from Joueur import *

ZeroTwo = Joueur("TESTER")
Quentin = Joueur("ALL-D")

p = Partie(0, 200, ZeroTwo, Quentin)
p.rencontre()
print("Z : ", ZeroTwo.score, ", Q : ", Quentin.score)