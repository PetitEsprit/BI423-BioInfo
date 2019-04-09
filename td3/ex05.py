sq = raw_input("Entrer une sequence:").upper()
i = 0
lensq = len(sq)
sq2 = ""

while i < lensq :
	if(sq[i] == 'T'):
		sq2 += 'U'
	else:
		sq2 += sq[i]
	i+=1
	
print "ARN :",sq2
