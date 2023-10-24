import os
import time
import random

larg, hauteur = 5, 4

while True:
    os.system("clear" if os.name == "posix" else "cls") 

    aleatoire = random.randint(0,larg-1)

    for b in range(hauteur):
        afficher = ""
        for a in range(larg):
            if b % 2 == 0:
                if b // 2 == 0 and a == aleatoire:
                    afficher += "*" *(larg)
                elif b // 2 == 1 and a == aleatoire:
                    afficher += "|"*(larg)
                elif b // 2 == 2 and a == aleatoire:
                    afficher += "+"*(larg)
                else:
                    afficher += " "*(larg)
            else:
                afficher += " "*(larg)
        print(afficher)
        time.sleep(0.3) 
    time.sleep(0.3)  