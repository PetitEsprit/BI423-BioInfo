s = raw_input("Entrer un nom de fichier...");
f = open(s, "r");
countA = 0.0
length = 0.0

i = f.readline().upper()
while  i != "":
	l = len(i) - 1
	countA += i[:l].count("A")
	length += l
	i = f.readline().upper()
res = round(countA*100.0/length, 2)
print "Le prourcentage de A est ", res ," %"
f.close();

s = raw_input("Entrer un nom de fichier de sauvegarde...");
f = open(s, "w")
f.write("longeur = " + str(length) + "\n");
f.write("Pourcentage de A : " + str(res) + " %\n");
f.close()
