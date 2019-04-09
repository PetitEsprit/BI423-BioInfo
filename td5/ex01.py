s = raw_input("Entrer un nom de fichier...");
f = open(s, "r");
seq = ""
i = f.readline()
while  i != "":
	seq += i[:len(i)-1]
	i = f.readline()
print seq
f.close();
