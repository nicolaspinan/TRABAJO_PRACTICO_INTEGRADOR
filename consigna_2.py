# Consigna 2 - Trabajo Practico  

# Importacion de libreria Matplotlib para poder graficar las funciones
import matplotlib.pyplot as plt

# Definicion de funciones
def A(x): 
    return 40 * x + 200

def B(x):
    return 70 * x + 50

def C(x):
    return -2 * x**2 + 80 * x + 100

# Graficacion del intervalo
valores = [0,5,10,15,20,25,30,40,50]

# Evaluacion de las funciones
print('|', 'x', '|', 'Plan A', '|', 'Plan B', '|', 'Plan C' '|')
for x in valores:
    print('|', x, '|', A(x), '|', B(x), '|', C(x), '|')

# Determinar cual es el plan mas economico
def plan_economico(x):
    a = A(x)
    b = B(x)
    c = C(x)

    if a <= b and a <= c:
        return 'Plan A'
    elif b <= a and b <= c:
        return 'Plan B'
    else:
        return 'Plan C'

# Comparativa de costos
print('-'*30,'\nCostos por horas')
for x in valores:
    print(x,'->',plan_economico(x))

# Graficos
x_valores = list(range(0, 51))

y_A = []
y_B = []
y_C = []

for x in x_valores:
    y_A.append(A(x))
    y_B.append(B(x))
    y_C.append(C(x))

plt.plot(x_valores, y_A, label='Plan A')
plt.plot(x_valores, y_B, label='Plan B')
plt.plot(x_valores, y_C, label='Plan C')

plt.xlabel('Horas')
plt.ylabel('Costo')
plt.title('Comparativa de planes')
plt.legend()
plt.grid(True)
plt.show()