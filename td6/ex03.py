f = open(raw_input("Entrer un nom de fichier entre..."), "r");
sub = raw_input("Entrer la sequence recherchee...");
g = open(raw_input("Entrer un nom de fichier sorti..."), "w");
seq = ""
i = f.readline().upper()
while  i != "":
	seq += i[:len(i)-1]
	i = f.readline().upper()
pos = seq.find(sub.upper())

if pos < 0:
	print "Sequence non trouvee"
while pos >= 0:
	print "Sequence a la position ", pos+1
	g.write("Sequence a la position "+str(pos+1)+"\n");
	pos = seq.find(sub.upper(), pos+1)
g.write(seq)
print seq
f.close()
g.close()
