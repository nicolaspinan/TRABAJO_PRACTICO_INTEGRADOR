M = [
    [120, 150, 100],  
    [200, 180, 220], 
    [90,  110, 95]   
]

C = [
    [30, 20, 10],  
    [15, 25, 20],  
    [40, 10, 30]   
]

print ("TIEMPO PROMEDIO DE FUNCIONES")

for i in range(3):  
    Ttotal_funcion = 0
    Etotales_funcion = 0
    
    for j in range(3):  
        Ttotal_funcion += M[i][j] * C[i][j]
        Etotales_funcion += C[i][j]
        
    promedio_funcion = Ttotal_funcion / Etotales_funcion
    print(f"Tiempo promedio de la Función {i + 1}: {promedio_funcion:.2f} ms")

#Linea separadora 
print("-" * 40)

for j in range(3):  
    Ttotal_servidor = 0
    Etotales_servidor = 0
    
    for i in range(3): 
        Ttotal_servidor += M[i][j] * C[i][j]
        Etotales_servidor += C[i][j]
        
    promedio_servidor = Ttotal_servidor / Etotales_servidor
    print(f"Tiempo promedio del Servidor {j + 1}: {promedio_servidor:.2f} ms")

#Linea separadora 
print("-" * 40)

Mtranspuesta = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        Mtranspuesta[j][i] = M[i][j]

print("MATRIZ TRANSPUESTA DE M:")
for fila in Mtranspuesta:
    print(fila)
