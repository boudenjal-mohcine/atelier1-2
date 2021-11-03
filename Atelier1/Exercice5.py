# Fonction qui calcule la somme des chiffres d'un nombre donné :

def somme(a):
 if(a!=0):
  return a%10+somme(int(a/10))  # 245 =  5  + somme(24) = 5 + 4 + somme(2) = 5 + 4 + 2 = 9 
 else:
  return a

# L'utilisateur va saisir un nombre :

n = int(input("Entre un nombre : "))
print("la somme des chiffre de",n,"est :",somme(n))
