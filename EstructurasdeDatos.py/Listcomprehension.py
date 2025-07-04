lista = [1,2,3,4,5]

#Ciclo for normal

cuadrados = []
for x in range (1, 6):         #Esto es lo mismo que lo de abajo. 
    if x % 2  == 0:
        cuadrados.append(x**2)
    

#List Comprehension
cuadrados = [x**2 for x in lista if x % 2 == 0]    #Mismo que lo de arriba pero en una sola línea de código
print(cuadrados)

