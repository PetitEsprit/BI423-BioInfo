seq = raw_input("entrez votre sequence: ").lower()
lseq = len(seq)
countA = seq.count('a')
countT = seq.count('t')
countC = seq.count('c')
countG = seq.count('g')
countX = lseq - (countA + countT + countC + countG)

print "poucentage en A:",round(countA*100.0/lseq, 2),"%"
print "poucentage en T:",round(countT*100.0/lseq, 2),"%"
print "poucentage en C:",round(countC*100.0/lseq, 2),"%"
print "poucentage en G:",round(countG*100.0/lseq, 2),"%"

print "pourcentage de non reconnu:",round(countX*100.0/lseq, 2),"%"

