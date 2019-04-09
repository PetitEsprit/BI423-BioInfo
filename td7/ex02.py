seq = raw_input("SEQ:").upper();
motif = raw_input("MOTIF:").upper();
seuil = input("SEUIL:")
i = 0
while i<=(len(seq2)-len(motif)):
	mseq = seq[i: i+len(motif)]
	n = 0.0
	j = 0
	while j < len(motif):
		if mseq[j] == motif[j]:
			n = n + 1
		j = j + 1
	p = n*len(seq2)/100
	if p >= seuil:
		print "Pos = ", i+1
