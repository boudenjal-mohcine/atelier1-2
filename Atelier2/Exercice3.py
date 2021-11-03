liste1=[11, 45, 8, 11, 23, 45, 23, 45, 89]   # EXEMPLE D'UNE LISTE 
dict1={}     # UN DICTIONNAIRE VIDE

print(liste1)

for x in liste1:
  dict1[x]=liste1.count(x) # CHAQUE ELEMENT VA AVOIR SON OCCURANCE COMME MOT CLE 

print(dict1)  # AFFICHER LE DICTIONNAIRE
