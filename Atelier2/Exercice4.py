set1={23, 42, 65, 57, 78, 83, 29}  # EXEMPLE SET 1 

set2={57, 83, 29, 67, 73, 43, 48}  # EXEMPLE SET 2 

print(set1)

print(set2)

set3=set1&set2  # TROUVER L'INTERSECTION DES DEUX SETS 

print("Intersection ",set3) 
  
set1=set1-set3 # FAIRE LA DIFFERENCE POUR ENLEVER LES ELEMENTS COMMUNS 

print("Set 1 après suppression : ",set1) # AFFICHER SET 1 SANS ELEMENT COMMUNS AVEC SET 2 