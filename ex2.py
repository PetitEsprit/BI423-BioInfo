#~ fichier = input("Nom fichier :")
f = open("seq.txt","r")
l = f.readline()
adn = ""

while l != "" : 
	adn = adn + l[: len(l)-1]
	l= f.readline() 
f.close()

seq = raw_input("Codon : ")
seq = seq.upper()
seuil = input("% d'identite : ")
while seuil<50 or seuil>100 :
	seuil = input("% d'identite : ")

fin = len(adn) - len(seq)

x = 0
y = 0
i = 0
j = 0
n = 0
a = 0
tmp = 0
save = ""

fichier = raw_input("Nom fichier sauvegarde : ")
h = open(fichier,"w")

while a <= fin :
	i = a
	
	while j< len(seq) :
		x = adn[i]
		y = seq[j]
		
		if x == y : 
			tmp = tmp+1
		i = i+1
		j = j+1
	
	res = tmp*100/len(seq)
	
	if seq >= seuil:
		h.write(str(i-len(seq))+"\n")
		n = n+1
		
	j = 0
	tmp = 0
	a = a+1
	
print "Il y a ",n," de sequence de plus de ",seuil,"% identique"
h.close()
