liste1= [11, 45, 8, 23, 14, 12, 78, 45, 89]  # EXEMPLE D'UNE LISTE 

print(liste1)

for i in range(2,len(liste1),3):  # PARCOURIR CHAQUE 3 ELEMENTS DE LA LISTE ON COMMENCANT PAR LE 3eme ELEMENT
 
  print([liste1[i],liste1[i-1],liste1[i-2]],end=' ')  # AFFICHER SUCCESSIVEMENT LE 3EME , 2EME ET 1ERE ELEMENT 
