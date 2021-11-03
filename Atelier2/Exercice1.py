liste1=[3, 6, 9, 12, 15, 18, 21]   # LISTE 1
liste2=[4, 8, 12, 16, 20, 24, 28]  # LISTE 2
liste3=[]                  #LA LISTE VIDE OU ON VA STOCKER LES ELEMENTS

j=0 

for i in range(0,len(liste1)):   # PARCOURIR LES ELEMENTS DU 1ere LISTE
    if i%2!=0:
      liste3.insert(j,liste1[i])  # AJOUTER LES ELEMENTS IMPAIRES
      j=j+1
    
for i in range(0,len(liste2)):   # PARCOURIR LES ELEMENTS DU 1ere LISTE
    if i%2==0:
      liste3.insert(j,liste2[i])  # AJOUTER LES ELEMENTS IMPAIRES

      j=j+1
# AFFICHER LES 3 LISTES :
print("liste 1 :",liste1)
print("liste 2 (index impair) :",liste2)    
print("liste 3 :(index pair)",liste3)