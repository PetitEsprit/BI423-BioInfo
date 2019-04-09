seq = raw_input("entrez une seq: ")
choix = raw_input("extraire (p)remiers ou (d)erniers ?")
n = input("combien de lettres ?");

if choix == 'p':
	seq2 = seq[0:n]
	print seq2
elif choix == 'd':
	seq2 = seq[len(seq)-n:]
	print seq2
else:
	print "ERREUR!"
	
