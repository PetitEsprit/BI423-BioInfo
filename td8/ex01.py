import matplotlib.pyplot as plt
# importation de la bibliotheque necessaire a la generation de graphiques

plt.title("Graphique") # titre du graphique
plt.xlabel("Axe X") # label/nom de l'axe des abscisses
plt.ylabel("Axe Y") # label/nom de l'axe des des ordonnees
plt.xlim(0, 100) # taille/longueur de l'axe des "x"
plt.ylim(0, 50) # taille/longueur de l'axe des "y"
plt.scatter(10, 20, c = "black", s=10)

# trace un point d'abscisse 10, d'ordonnee 20 (y = 20), de couleur noire (c = 'black'), et
# de taille 10 pixels (s = 10)
plt.scatter(50, 30, c = 'red', s = 20)# trace un point d'abscisse 50,d'ordonnee 30,
# de couleur rouge (c = 'red'), et de taille 20 pixels (s = 20)
plt.scatter(25, 20, c = "black", s=10)
plt.scatter(35, 35, c = "blue", s=10)
plt.scatter(15, 45, c = "green", s=10)
plt.scatter(5, 20, c = "yellow", s=10)
plt.show() # affichage du graphique
