def fibonacci(n):  # Fonction qui genere la serie Fibonacci 
    if(n <= 1):
        return n   # Stopper si on a arriver a 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2)) # Le dexieme element devient le premier et le dexieme devient la somme
n = int(input("Entrez le nombre de termes que vous voulez (struct positive): "))
for i in range(0,n): # 0 1 (0+1) (0+1+1) (0+1+1+1+2) .....
    print(fibonacci(i) ,end=' ')
