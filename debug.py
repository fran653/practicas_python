milista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def recorrer_lista(lista):
    for i in lista:
        for j in i:
            print(j)
            
def recorrer_inv_lista(lista):
    for i in reversed(lista):
        for j in reversed(i):
            print(j)

recorrer_lista(milista)
recorrer_inv_lista(milista)