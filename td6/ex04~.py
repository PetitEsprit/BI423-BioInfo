f = open(raw_input("Entrer un nom de fichier entre..."), "r");
sub = raw_input("Entrer la sequence recherchee...");
g = open(raw_input("Entrer un nom de fichier sorti..."), "w");
seq = ""
i = f.readline().upper()
while  i != "":
	seq += i[:len(i)-1]
	i = f.readline().upper()

i = 0
while i <(len(seq)-len(sub)):
	mseq = seq[i: i+len(motif)]
	j = 0
	while j < len(motif):
		j = j+1
	if j == len(motif):
		print "Occurren en ", i
print seq
f.close()
g.close()
