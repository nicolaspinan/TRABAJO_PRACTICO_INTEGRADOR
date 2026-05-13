#Parte A: Analisis con conjuntos
A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]

#1:Calculo de los ususarios 
ambas_plataformas = []
una_plataforma = [] 
sin_errores = []
unica_plataforma = []
en_C_no_en_AB = []
universo_usuarios = set(A + B + C)

for usuario in universo_usuarios:
    #Ambas plataformas 
    if usuario in A and usuario in B:
        ambas_plataformas.append(usuario)
    
    #Al menos una plataforma
    if usuario in A or usuario in B:
        una_plataforma.append(usuario)
    
    #No genera errores
    if (usuario in A or usuario in B) and usuario not in C:
        sin_errores.append(usuario)
    
    #Una sola plataforma
    if (usuario in A and usuario not in B) or (usuario in B and usuario not in A):
        unica_plataforma.append(usuario)

print(f"Ambas plataformas: {ambas_plataformas}\nAl menos una plataforma: {una_plataforma}\nNo generaron errores: {sin_errores}\nUna sola plataforma: {unica_plataforma}")


#2: Expresion con Compresion de Conjuntos
print("\n---RESULTADOS USANDO COMPRENSION DE CONJUNTOS---")
print("Usuarios que usan al menos una plataforma = {x|x ∈ A ∨ x ∈ B}")
print("Usuarios que usan ambas plataformas = {x|x ∈ A ∧ x ∈ B}")

#3: Usuarios en 𝐶 pero no en 𝐴 ∪ 𝐵
for estudiante in C:
    if estudiante not in A and estudiante not in B:
        en_C_no_en_AB.append(estudiante)
print(f"\nUsuarios que aparecen en C pero no en 𝐴 ∪ 𝐵: {en_C_no_en_AB}")

#Parte B - Lógica proposicional
#4: 
p = A
q = B
r = C

#5: Tabla de verdad - (p ∨ q) ∧ r
print("\n TABLA DE VERDAD ")
print("-" * 55)
print(f"  {'p':<6} {'q':<6} {'r':<6} {'p ∨ q':<10} {'(p ∨ q) ∧ r'}")
print("-" * 55)

valores = [True, False]
for P in valores:
    for Q in valores:
        for R in valores:
            P_o_Q = P or Q
            resultado_logico = P_o_Q and R
            print(f"  {str(P):<6} {str(Q):<6} {str(R):<6} {str(P_o_Q):<10} {resultado_logico}")
print("-" * 55)

#6: Función para determinar si un usuario es crítico
def es_critico(usuario_id):
    p = usuario_id in A   
    q = usuario_id in B   
    r = usuario_id in C   
    return (p or q) and r

#7: Clasificación de usuarios
criticos = []
no_criticos = []

for usuario in universo_usuarios:
    if es_critico(usuario):
        criticos.append(usuario)
    else:
        no_criticos.append(usuario)

print("\n---CLASIFICACION DE USUARIOS---")
print(f"Usuarios Críticos:    {criticos}")
print(f"Usuarios No Críticos: {no_criticos}")

