sq = raw_input("Entrer une sequence:").upper()
i = 0
n = 0

while i < len(sq) :
	if(sq[i] == 'M'):
		n+=1
	if(sq[i] == 'C'):
		n+=1
	i = i+1
print n
