def torre_hanoi(n, origen, destino, auxiliar):
    if n==1:
        print("mover disco ", n, " de ", origen, " a ", destino)
    return
    torre_hanoi(n-1, origen, auxiliar, destino)
    print("mover disco ", n, " de ", origen, " a ", destino)
    torre_hanoi(n-1, auxiliar, destino, origen) 
n = 3
torre_hanoi(n, 'A', 'B', 'C')
