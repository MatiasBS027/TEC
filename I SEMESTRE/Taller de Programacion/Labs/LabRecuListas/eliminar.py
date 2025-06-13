def eliminarTodas(num, lista):
    if not lista:
        return []
    if lista[0] == num:
        return eliminarTodas(num, lista[1:])
    else:
        return [lista[0]] + eliminarTodas(num, lista[1:])

print(eliminarTodas(1, [1,2,3,4,1,1]))  
print(eliminarTodas(1, [1,1,1]))        
print(eliminarTodas(4, [1,1,1]))       