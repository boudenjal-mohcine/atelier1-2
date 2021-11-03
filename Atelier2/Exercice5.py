# Une fonction qui verifie si l'element(elem) de la liste se trouve comme value d'un key dans le dictionnaire(dict)
def check(dict,elem):
  
  existe=False
  
  for x in dict:
    if elem==dict[x]:   # Parcorir la liste et verifier l'existance
      existe=True
      break
    
  return existe       # Returner true si element existe dans le dictionnaire ou false s'il n'existe pas
      
    

liste=[47,64, 69, 37, 76, 87 ,99]     # Exemple d'une liste
dict1={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':99}   # Exemple d'un dictionnaire
i=0

print(liste)
print(dict1)

for x in liste:
  if check(dict1,x)==False:
      liste.remove(x) # Supprimer l'élément y s'il n'existe pas comme value d'un key appartient au dictionnaire
print(liste)
