seq1 = raw_input("Sequence 1 : ")
seq2 = raw_input("Sequence 2 : ")
seq1 = seq1.upper()
seq2 = seq2.upper()

if len(seq1) != len(seq2) :
	print ("Sequences non valides")
	
l = 0
i = 0

while l < len(seq1) :
	
	if seq1[l] == seq2[l] :
		i = i+1
		
	l = l+1

#~ res = (i/len(seq1)) *100
res = round((i*100)/len(seq1))
print "Identite : " , res
	
