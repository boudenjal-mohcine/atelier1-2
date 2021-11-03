#Fonction qui converie un nombre binaire au decimal 

def convertissement(decimal):
  base=1
  binaire=0
  while(decimal>0) : #devision succéssive sur 2
     reste = decimal%2 
     binaire = binaire + ( reste * base )
     decimal=int(decimal/2) 
     base=base*10 #base 10 , 100 , 1000 ...
  return binaire 

#L'utilisateur va saisir un nombre pour le converti :  
n = int(input("Entrer un nombre : "))
print(n,"en binaire : ",convertissement(n))
