sq = raw_input("Entrer une sequence:").upper()
lensq = len(sq)
i = 0
n = 0


while i < lensq:
	if(sq[i] != 'A' and sq[i] != 'T' and sq[i] != 'C' and sq[i] != 'G'):
		print "erreur en position", i+1; n+=1
	i+=1

print "nb erreurs :",n
