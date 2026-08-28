# Pestaña "Informes" — Contenido a replicar

> Estado: replicada y auditada (2 pasadas, 11-ago-2026). Los datos de la barra superior y las 5 pestañas de navegación difieren adrede de la captura de referencia: el usuario dictó después la barra definitiva ([11] Hotel Jaippy + ClassOne, KPIs 9,113/26,18%/46,39%, badge 9,1) y el orden de pestañas. La referencia parece tener una tarjeta más al fondo, cortada por el borde de la captura — pendiente de una captura completa para replicarla.

Fuente: captura de la app real `C:\Users\emore\Downloads\Menú perfil.png` (1366x1452). Objetivo: réplica literal del contenido y del diseño.

## Barra de herramientas
- [ ] Campo "Plan" (etiqueta flotante, borde ámbar) con chip verde `reportsucommon.ao…` y texto `Objetivo 9,2 (18 de mayo de 2026 – 4 de octubre de 2026)` + chevron.
- [ ] Campo "Rango por semanas" con placeholder `18/05/26 – 09/08/26` + icono de calendario.
- [ ] Botón `EXPORTAR PDF` en mayúsculas con icono.

## Informe
- [ ] Cabecera: `Informe por semanas de Hotel Jaippy` + logotipo jaippy a la derecha.
- [ ] `Periodo del informe` + píldora `18 de mayo de 2026 – 9 de agosto de 2026`.
- [ ] Fila de 22 marcas ovaladas, 13 en ámbar (semanas transcurridas) y 9 en crema.
- [ ] Texto en cursiva: "Tu puntuación en Booking muestra una tendencia negativa. Aunque tienes indicadores positivos en cuanto a porcentaje de reseñas de 10, necesitas enfocarte en mejorar la experiencia global para revertir la tendencia y acercarte al 9,2."

### Tres KPIs comparados (cada uno: título, icono, valor, delta, gráfica de 2 barras, pie explicativo)
- [ ] **Índice Jaippy** — símbolo "j" · `9,113` · delta `−0,05%` rojo · barras `9,118` (periodo anterior, beige) y `9,113` (periodo actual, ámbar), eje 0–10 paso 2 · pie: "Métrica que muestra, con 3 decimales de precisión, la puntuación de Booking.com"
- [ ] **Conversión** — icono fotos+estrella · `26,18%` · delta `−16,4%` rojo · barras `31,3 %` y `26,2 %`, eje 0–100 % paso 20 · pie: "Porcentaje de reservas que dejan una reseña en Booking.com"
- [ ] **Consistencia** — icono tarjetas+10 · `46,39%` · delta `+2,02%` verde · barras `45,5 %` y `46,4 %` · pie: "Probabilidad de que un huésped te ponga una reseña de 10."
- [ ] Etiquetas de eje X: `Periodo anterior` / `Periodo actual`.

### Progreso y valoración por día
- [ ] `Progreso del plan hasta la fecha seleccionada` + sub "Porcentaje de progreso y grado de éxito de la ejecución del plan."
- [ ] Tile ámbar: `% del plan completado` / `60%` + mensaje "¡Ups! Vas 15 semanas por detrás de lo previsto."
- [ ] `Valoración media por día de la semana` + sub "Días de la semana que tienen más puntuaciones obtenidas."
- [ ] 7 tiles: L `9` · M `9,17` · X `9,07` · J `8,98` · **V `9,23` (destacado en ámbar)** · S `9,1` · D `9,06`

### Puntuaciones positivas
- [ ] Título + subtítulo azul `Objetivo propuesto del periodo seleccionado` + "Se ha obtenido un 70% de reseñas del plan para las puntuaciones de 10"
- [ ] Columna `Obtenida`; fila: badge oscuro `10`, barra ámbar al 70%, `70%` en ámbar, `423` / `obj. 607`

### Puntuaciones negativas
- [ ] Título + subtítulo azul `Máximo permitido` + "Se han superado el máximo de reseñas de 1 y 9 para este periodo"
- [ ] 9 filas (badge gris, barra roja, % rojo, obtenida/máximo):
  | Nota | % | Obtenida | Máx. |
  |---|---|---|---|
  | 9 | (icono ⚠ en vez de %) | 311 | 296 |
  | 8 | 79% | 169 | 213 |
  | 7 | 75% | 44 | 59 |
  | 6 | 58% | 7 | 12 |
  | 5 | 40% | 4 | 10 |
  | 4 | 29% | 2 | 7 |
  | 3 | 100% | 1 | 1 |
  | 2 | 100% | 1 | 1 |
  | 1 | 0% | 2 | 0 |

### Evolución de iniciativas
- [ ] Título + píldora `18 may - 9 ago 2026` + `Nº etiquetas utilizadas → 15`
- [ ] Columnas: Etiqueta · Reservas · Conversión · Puntuación media
  | Etiqueta (chip) | Reservas | % del total | Conversión | Puntuación |
  |---|---|---|---|---|
  | todo bien (verde) | 578 | 15,4 % | 36,33% ↗ | 9,2 ↗ |
  | Queso idiazabal (amarillo) + sub naranja "Mejor conversión" | 54 | 1,4 % | 53,7% ↗ | 9,2 ↗ |
  | LLAMADA IN (lavanda) | 53 | 1,4 % | 33,96% ↗ | 9,3 ↗ |
  | chocolate (topo) | 43 | 1,1 % | 30,23% ↗ | 9,5 ↗ |
  | FREE UPGRADE (amarillo claro) | 25 | 0,7 % | 28% ↗ | 8,1 ↘ rojo |
  | TARTA CUMPLE EN… (rosa) | 12 | 0,3 % | 33,33% ↗ | 9 ↘ rojo |

## Dos tarjetas inferiores
- [ ] **Top empleados mencionados**: barras horizontales ámbar sobre pista gris, nombres anonimizados, valores 67, 54, 22, 14, 11, 9, 5, 4, 4, 3; eje X 0–80 paso 20.
- [ ] **Evolución del número de menciones** + sub "En un rango acumulativo de 365 días atrás": línea ámbar descendente (~1.560 → ~1.230), eje Y 0–1.800 paso 300, etiquetas X en diagonal (11/08/25 … 18/07/26), leyenda "Todos".
