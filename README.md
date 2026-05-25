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
