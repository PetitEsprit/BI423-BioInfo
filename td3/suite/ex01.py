sq = raw_input("Entrer une sequence:").upper()
sq2 = ""

""" Version 1
i = len(sq) -1
while i >= 0:
	if(sq[i] == 'A'):
		sq2 += 'T'
	if(sq[i] == 'T'):
		sq2 += 'A'
	if(sq[i] == 'C'):
		sq2 += 'G'
	if(sq[i] == 'G'):
		sq2 += 'C'
	i-=1


"""

"""Version 2"""
i = 0
while i < len(sq):
	if(sq[i] == 'A'):
		sq2 = 'T' + sq2
	if(sq[i] == 'T'):
		sq2 = 'A' + sq2
	if(sq[i] == 'C'):
		sq2 = 'G' + sq2
	if(sq[i] == 'G'):
		sq2 = 'C' + sq2
	i+=1

print "INV COMPL :",sq2
