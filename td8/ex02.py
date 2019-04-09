import matplotlib.pyplot as plt

name = raw_input("Entrer un nom de fichier...")
fic = open(name, "r")
name2 = raw_input("Entrer un deuxieme nom de fichier...")
fic2 = open(name, "r")
lf = input("Entrer une taille de fenetre...")

i = 0
j = 0
seq = ""
seq2 = ""

ligne = fic.readline()
while ligne != "":
	seq =  seq + ligne[0:len(ligne)-1]
	ligne = fic.readline()

ligne = fic2.readline()
while ligne != "":
	seq2 =  seq2 + ligne[0:len(ligne)-1]
	ligne = fic2.readline()

for j in range(len(seq)):
	for i in range(len(seq2)):
		equal = 1 
		if seq[j] == seq2[i]:
			plt.scatter(i+1, j+1, c = "black", s=10)

plt.title("Dot Plot lettre a lettre") # titre du graphique
plt.xlabel(name2) # label/nom de l'axe des abscisses
plt.ylabel(name) # label/nom de l'axe des des ordonnees
plt.xlim(0, len(seq2)) # taille/longueur de l'axe des "x"
plt.ylim(0, len(seq))# taille/longueur de l'axe des "y"

plt.show() # affichage du graphique
