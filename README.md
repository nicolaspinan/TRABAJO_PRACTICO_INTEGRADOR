# Trabajo Práctico Integrador I
### Tecnicatura Universitaria en Programación — Matemática 2026
**UTN Villa María**

Integrantes:

	- Briguera, Mateo
	- Grando, Fidel
	- Piñan, Nicolas 
	- Urgaregui, Julian
	- Villosio, Luciano

---

## Descripción

Este repositorio contiene la resolución computacional del Trabajo Práctico Integrador I de la materia Matemática, correspondiente a la Tecnicatura Universitaria en Programación.

El trabajo articula conceptos matemáticos con implementaciones en Python, abordando problemas inspirados en situaciones reales del ámbito de la programación.

---

## Consigna 1 — Validación de usuarios y análisis de consistencia del sistema

**Temas:** Teoría de conjuntos + Lógica proposicional

Una empresa de desarrollo analiza el comportamiento de usuarios de su plataforma a partir de registros de IDs según distintas actividades:

- `A`: usuarios que acceden a través de la API
- `B`: usuarios que acceden a través de la web
- `C`: usuarios que han generado errores

### Contenido
- Operaciones con conjuntos (intersección, unión, diferencia)
- Comprensión de conjuntos
- Modelado lógico con proposiciones p, q, r
- Tabla de verdad
- Clasificación de usuarios críticos mediante la expresión `(p ∨ q) ∧ r`

---

## Consigna 2 — Análisis y optimización de costos de desarrollo

**Temas:** Funciones lineales y cuadrática + Programación + Toma de decisiones

Una empresa de software ofrece distintos planes de contratación de horas. El objetivo es analizar cuál conviene según la cantidad de horas utilizadas mensualmente.

Los modelos de costo son:

```
A(x) = 40x + 200
B(x) = 70x + 50
C(x) = -2x² + 80x + 100
```

Dominio: `0 ≤ x ≤ 50`

### Contenido
- Implementación de las tres funciones en Python
- Evaluación para valores `x = [0, 5, 10, 15, 20, 25, 30, 40, 50]`
- Función `plan_economico(x)` que determina el plan más conveniente para un valor dado
- Visualización gráfica mediante **matplotlib**
- Análisis de rangos de conveniencia por plan
- Detección y explicación de valores negativos en C(x)

### Librería utilizada
Se utilizó **matplotlib** para la generación del gráfico comparativo de los tres planes. Esta librería no forma parte del contenido visto en clase y fue incorporada como proceso de investigación, conforme a lo indicado en la consigna.

---

### Consigna 3 — Análisis de rendimiento en sistemas distribuidos
**Temas**: Matrices + Operaciones matriciales
Una empresa de tecnología opera un sistema distribuido donde distintas funcionalidades del backend se ejecutan en múltiples servidores. Para analizar el rendimiento y detectar cuellos de botella, se registran métricas de ejecución representadas en dos matrices:

M: tiempos promedio de ejecución (en ms) de cada función en cada servidor
C: cantidad de ejecuciones registradas por función y servidor

```
M = | 120  150  100 |        C = | 30  20  10 |
    | 200  180  220 |            | 15  25  20 |
    |  90  110   95 |            | 40  10  30 |
```

Donde cada fila representa una función del sistema (autenticación, procesamiento de datos, generación de reportes) y cada columna representa un servidor distinto.
Contenido

Cálculo del tiempo promedio de ejecución por función (promedio por fila)
Cálculo del tiempo promedio de ejecución por servidor (promedio por columna)
Cálculo de la matriz transpuesta de M y análisis de su interpretación en contexto
