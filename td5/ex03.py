s = raw_input("Entrer un nom de fichier...");
c = input("Entrer un choix...")
ss = raw_input("Entrer un nom de fichier de sauvegarde...");
seq = ""
seqf = ""
f = open(s, "r");
g = open(ss, "w");

i = f.readline().upper()
while  i != "":
	seq += i[:len(i)-1];
	i = f.readline().upper()

if c == 1:
	seqf = seq.replace("T","U");
	print "Voici le transcript : ", seqf
	g.write("Transcript :" + seqf + "\n");
	
elif c == 2:
	i = 0
	while i < len(seq):
		if(seq[i]) == "A":
			seqf = "T" + seqf 
		if(seq[i] == "T"):
			seqf = "A" + seqf 
		if(seq[i] == "C"):
			seqf = "G" + seqf 
		if(seq[i] == "G"):
			seqf = "C" + seqf
		i = i + 1
	print "Voici l'inverse compl. : ", seqf
	g.write("Inverse compl: " + seqf + "\n");
else:
	print "Choix incorrect !"
f.close()
g.close()
