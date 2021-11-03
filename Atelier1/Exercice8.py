def occu(string,char):  # DEUX ARGUMENTS : LA CHAINE ET LE CHARACTERE A CHERCHER
  k=0  # INITIALISER LE NOMBRE D'OCCURANCE
  i=0
  while(i<len(string)):  # PARCORIR CHAQUE CHARACTERE DE LA CHAINE 
    if string[i]==char:
      k=k+1     # INCRIMENTATION DU NOMBRE D'OCCURENCE
    i=i+1   # CHARACHTERE SUIVANT DU CHAINE
  return k  

chaine=('Faculte de science et technique Tanger')
print(chaine)
print("Occurence du 'e' est : ",occu(chaine,'e'))
