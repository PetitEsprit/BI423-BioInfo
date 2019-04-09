sq = raw_input("Entrer une sequence:")
lensq = len(sq)
i = 0
err = 0

while i < (lensq/2) and err == 0:
	if(sq[i] == 'A' and sq[lensq - i - 1] != 'T'):
		err = 1
	if(sq[i] == 'T' and sq[lensq - i - 1] != 'A'):
		err = 1
	if(sq[i] == 'C' and sq[lensq - i - 1] != 'G'):
		err = 1
	if(sq[i] == 'G' and sq[lensq - i - 1] != 'C'):
		err = 1
	i+=1

if(err == 1) : print "ERROR"
else : print "YOUHOU"
