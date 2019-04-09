f = open(raw_input("Entrer un nom de fichier..."), "r");
sub = raw_input("Entrer la sequence recherchee...");
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
	pos = seq.find(sub.upper(), pos+1)
print seq
f.close()
