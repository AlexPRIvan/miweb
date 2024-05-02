def torre_hanoi(n, origen, destino, auxiliar):
    if n==1:
        print ("Mover disco 1 de torre ", origen, " a torre ", destino)
        return 
    torre_hanoi(n-1, origen, auxiliar, destino)
    print("Mover disco ", n, " a torre ", origen, " a torre ", destino)
    torre_hanoi(n-1, auxiliar, destino, origen)

n=3

torre_hanoi(n, 'A', 'B', 'C')




