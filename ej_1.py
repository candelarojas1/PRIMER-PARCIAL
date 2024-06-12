"""1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
manera inversa al que están cargados. Preferentemente la función solo debe tener un
parámetro que es la lista de elementos."""

def listar_manera_inversa(lista_elementos):
    if len(lista_elementos) == 0:  
        return lista_elementos
    else:
        return [lista_elementos[-1]] + listar_manera_inversa(lista_elementos[:-1])  
    
lista_elementos= [0,1,2] 
print (listar_manera_inversa(lista_elementos))  

