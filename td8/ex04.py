import matplotlib.pyplot as plt

name = raw_input("Entrer un nom de fichier...")
fic = open(name, "r")
name2 = raw_input("Entrer un deuxieme nom de fichier...")
fic2 = open(name2, "r")
tf = input("Entrer une taille de fenetre...")
seuil = input("Entrer un seuil...")

i = 0
n = 0
even = 0
end = 0
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

for j in range(len(seq) - tf):
	for i in range(len(seq2) - tf):
		even = 0
		n = 0
		while n < tf:
			if seq[j+n] == seq2[i+n]:
				even = even + 1
			n = n + 1
		if (even*100.0/tf) >= seuil and i>0 and j>0:
			plt.scatter(i, j, c = "black", s=10)

plt.title("Dot Plot mot a mot avec flou") # titre du graphique
plt.xlabel(name2) # label/nom de l'axe des abscisses
plt.ylabel(name) # label/nom de l'axe des des ordonnees
plt.xlim(0, len(seq2)) # taille/longueur de l'axe des "x"
plt.ylim(0, len(seq))# taille/longueur de l'axe des "y"

plt.show() # affichage du graphique
