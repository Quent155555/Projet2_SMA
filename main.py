from Manche import *
from Joueur import *

MATRICE_COURS = [[(3,3), (0,5)], [(5,0), (2,2)]]
MATRCIE_CERF = [[(4,4), (0,3)], [(3,0), (1,1)]]

#Pour afficher le classement + renvoie liste des joueurs selon leurs positions dans le podium
def print_classement(joueurs):
    print("Resume score :")
    n=len(joueurs)
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
    return classement

#Pour le tournoi avec les 5 strats du cours
def tournoi_classique(matrice, nvstrat, allc):
    ZeroTwo = Joueur("ZeroTwo", "TFT")
    Quentin = Joueur("Quentin", "JOSS")
    Lucas = Joueur("Lucas", "TESTER")
    Yassine = Joueur("Yassine", "RANDOM")
    ds1 = Joueur("ds1", "ALL-D")
    joueurs = [ZeroTwo, Quentin, Lucas, Yassine, ds1]

    if nvstrat :
        jester = Joueur("Jester", "FARCEUR")
        superstition = Joueur("Superstition", "PATTERN")
        ds2 = Joueur("ds2", "ALL-D2")
        joueurs.extend([jester, superstition, ds2])
    if allc :
        pigeon = Joueur("pigeon", "ALL-C")
        joueurs.append(pigeon)
            
    t = Tournoi(joueurs, 5, 200)
    t.debut_tournoi(matrice)
    classement = print_classement(joueurs)

#Lance nb_generation_max tournois avec mutation mutations par generation
def tournoi_selection(matrice, nb_generation_max, mutation, pop2):
    ZeroTwo = Joueur("ZeroTwo", "TFT")
    Quentin = Joueur("Quentin", "JOSS")
    Lucas = Joueur("Lucas", "TESTER")
    Yassine = Joueur("Yassine", "RANDOM")
    ds1 = Joueur("ds1", "ALL-D")
    pigeon = Joueur("pigeon", "ALL-C")#ALL-C
    jester = Joueur("Jester", "FARCEUR")
    superstition = Joueur("Superstition", "PATTERN")
    ds2 = Joueur("ds2", "ALL-D2")

    joueurs = [ZeroTwo, Quentin, Lucas, Yassine, ds1, jester, superstition, pigeon ,ds2]

    if pop2 == True:
        ZeroTwo2 = Joueur("ZeroTwo2", "TFT")
        Quentin2 = Joueur("Quentin2", "JOSS")
        Lucas2 = Joueur("Lucas2", "TESTER")
        Yassine2 = Joueur("Yassine2", "RANDOM")
        ds12 = Joueur("ds12", "ALL-D")
        pigeon2 = Joueur("pigeon2", "ALL-C")#ALL-C
        jester2 = Joueur("Jester2", "FARCEUR")
        superstition2 = Joueur("Superstition2", "PATTERN")
        ds22 = Joueur("ds22", "ALL-D2")
        joueurs.extend([ZeroTwo2, Quentin2, Lucas2, Yassine2, ds12, jester2, superstition2, pigeon2, ds22])

    nbjoueurs = len(joueurs)
    for i in range(nb_generation_max):
        print("#########################################################################")
        print("Debut du tournoi numero : ", i)
        print("#########################################################################")

        t = Tournoi(joueurs, 5, 200)
        t.debut_tournoi(matrice)
        classement = print_classement(joueurs)

        #changement des strats
        for i in range(mutation):
            classement[nbjoueurs-1 -i].strat = classement[i].strat

        #on reinitialise les points
        for joueur in joueurs :
            joueur.reinitialise_points()


###################                     MAIN                 #########################
def main():

    matrice_choix = False
    while not matrice_choix :
        mat = input("Quelle matrice utiliser ? c ou p (h pour voir les matrices)\n")
        match mat :
            case "h" :
                print("Prison (p) : ", MATRICE_COURS)
                print("Cerf (c) : ", MATRCIE_CERF)
            case "c" :
                matrice = MATRCIE_CERF
                matrice_choix = True
            case "p" :
                matrice = MATRICE_COURS
                matrice_choix = True
            case _ :
                print("h ou c ou p")


    while True :
        double = input("Doubler les pops par stratégies, donc 2 ALL-D etc ? y pour oui q pour quitter, n'importe quoi pour non\n")
        match double :
            case "y" :
                double = True
            case "q" :
                return 0
            case _ :
                double = False
        tournoi = input("Quel tournoi lancer ? (h pour voir les tournoi)\n")
        match tournoi :
            case "h" :
                print("1 : le tournoi classique avec les 5 strats du cours")
                print("2 : le tournoi classique avec les nouvelles stratégies (sans ALL-C)")
                print("3 : le tournoi classique avec les nouvelles stratégies (avec ALL-C)")
                print("4 : lance 10 tournois avec 4 mutations par generation et toutes les stratégies")
                print("5 : lance 25 tournois avec 1 mutaution par generation et toutes les stratégies")
                print("6 : mon propre tournoi de selection (nb de generation et de mutation)")
                print("q : pour quitter le programme")
            case "1" :
                tournoi_classique(matrice, False, False)
            case "2" :
                tournoi_classique(matrice, True, False)
            case "3" :
                tournoi_classique(matrice, True,True)
            case "4" :
                tournoi_selection(matrice, 10, 4, double)
            case "5" :
                tournoi_selection(matrice, 25, 1, double)
            case "6" :
                nbgeneration = int(input("Combien de tournois ? (de generation)\n"))
                nbmutation = int(input("Combien de mutation ? (si x alors les x derniers copieront les strtas des x premiers)\n"))
                tournoi_selection(matrice, nbgeneration, nbmutation, double)
            case "q" :
                return 0
            case _ :
                print("h pour voir les tournois et leurs touches")

main()