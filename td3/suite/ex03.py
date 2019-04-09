sq = raw_input("Entrer une sequence:").upper()
lensq = len(sq)
i = 0
n = 0

while i < lensq and n < 1:
	if(sq[i] != 'A' and sq[i] != 'T' and sq[i] != 'C' and sq[i] != 'G'):
		n+=1
	i+=1
if n < 1 :
	print "Chaine correcte"
else :
	print "Il y a au moins une erreur"
