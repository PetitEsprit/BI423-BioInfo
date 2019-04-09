seq1 = raw_input("SEO 1 =").upper();
seq2 = raw_input("SEO 2 =").upper();

i = 0
n = 0.0
while i<len(seq2):
	if seq1[i] == seq2[i]:
		n = n + 1
	i = i + 1
print "nombre identite est = ", n/len(seq1)*100
