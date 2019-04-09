c = 0
seq = ""
seqf = ""
while c != 3 :
	s = raw_input("Entrer un nom de fichier...");
	f = open(s, "r");
	
	c = input("Entrer un choix...")
	ss = raw_input("Entrer un nom de fichier de sauvegarde...");
	seq = ""
	seqf = ""
	i = f.readline().upper()
	while  i != "":
		seq += i[:len(i)-1];
		i = f.readline().upper()
	f.close()
	
	g = open(ss, "w");
	
	if c == 1:
		seqf = seq.replace("T","U");
		print "Voici le transcript : ", seqf
		g.write("Transcript :" + seqf + "\n");
		g.close();
	
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
		g.close()
	elif c == 3:
		print "Vous quittez le rogramme\n"
	else:
		print "Choix incorrect ! Recommencez\n"
