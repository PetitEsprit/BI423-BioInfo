import matplotlib.pyplot as plt

# name = raw_input("Entrer un nom de fichier...")
tf = input("Entrer une taille de fenetre...")
f = open("sequence.fasta", "r")
ligne = ""
seq = ""
i = 0
countC = 0
countG = 0
skew = 0
tmpskew = 0
minSkew = 0
maxSkew = 0

f.readline()
ligne = f.readline()
while ligne != "":
	seq =  seq + ligne[0:len(ligne)-1]
	ligne = f.readline()

while i < len(seq):
	if(seq[i] == "C"):
		countC = countC + 1
	if(seq[i] == "G"):
		countG = countG + 1
	if(i % tf == 0):
		if(countC != 0 or countG !=0):
			# la base du prog
			tmpskew = float(countG - countC)/ float(countC + countG)
			plt.scatter(i, skew, c = "black", s=10)
			
			if skew > maxSkew:
				maxSkew = skew
			if skew < minSkew:
				minSkew = skew
		else:
			skew = 0
		countC = countG = 0
		skew += tmpskew
		print "skew: ", skew
	i = i + 1

if(countC != 0 or countG !=0):
			tmpskew = float(countG - countC)/ float(countC + countG)
			skew += tmpskew
			plt.scatter(i, skew, c = "black", s=10)


plt.title("GC Skew Cumul") # titre du graphique
plt.xlabel("Position") # label/nom de l'axe des abscisses
plt.ylabel("Skew") # label/nom de l'axe des des ordonnees
plt.xlim(0, len(seq)) # taille/longueur de l'axe des "x"
plt.ylim(minSkew, maxSkew)# taille/longueur de l'axe des "y"

plt.show() # affichage du graphique
