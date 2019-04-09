sq = raw_input("Entrer une sequence:").upper()
lensq = len(sq)
i = 0
pA = 0
pT = 0
pG = 0
pC = 0
pX = 0

while i < lensq :
	if(sq[i] == 'A'):
		pA+=1
	elif(sq[i] == 'T'):
		pT+=1
	elif(sq[i] == 'C'):
		pC+=1
	elif(sq[i] == 'G'):
		pG+=1
	else :
		pX+=1
	i+=1

pA = round(pA * 100.0 / lensq, 2)
pT = round(pT * 100.0 / lensq, 2)
pC = round(pC * 100.0 / lensq, 2)
pG = round(pG * 100.0 / lensq, 2)
pX = round(pX * 100.0 / lensq, 2)
print "Pourcentage de A :",pA
print "Pourcentage de T :",pT
print "Pourcentage de C :",pC
print "Pourcentage de G :",pG
print "Pourcentage de gene inconnu :",pX
