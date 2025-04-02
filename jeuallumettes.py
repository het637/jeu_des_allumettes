from random import*

alumette = 21

while alumette >= 1:
    if alumette == 1:
        print("Le joueur a perdu...")
        break
        print("Fin du programme")
    retirage = int(input("Combien d'allumettes retirez-vous ? "))
    assert retirage <= 3, ("On ne peut pas retirer plus de 3 allumettes !")
    assert retirage > 0, ("On ne peut pas retirer un nombre négatif d'allumettes")
    while retirage >= alumette:
        print("On ne peut pas retirer plus d'allumettes que ce qu'il y en a")
        retirage = int(input("Combien d'allumettes retirez-vous ? "))
    alumette = alumette - retirage
    print("Le joueur prend",retirage, "allumettes")
    if alumette >=3:
        ordi = randint(1,3)
    else: ordi = randint(1,alumette)
    print("L'ordinateur prend",ordi, "allumettes")
    alumette = alumette - ordi
    print("Il reste" ,alumette, "allumettes")
    if alumette == 0:
        print("Le joueur a gagné !")
