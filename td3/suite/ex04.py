sq = raw_input("Entrer une sequence:")
lensq = len(sq)
i = 0
err = 0

while i < (lensq/2) and err == 0:
	if(sq[i] != sq[lensq - i -1]):
		err = 1
	i+=1

if(err == 1) : print "ERROR"
else : print "YOUHOU"
