# Pestaña "Habitaciones" — Panel de estado de habitaciones

Fuente: `C:\Users\emore\Downloads\Mockup.png` (1366x906). Estado: replicada (11-ago-2026).

## Barra de herramientas (tarjeta blanca)
- Botón circular con icono de marcador (izquierda).
- Segmentado de tamaño de letra `aa / Aa / AA` (activo con fondo #2A2A2A) — funcional: escala el número de las tarjetas.
- Tres botones cuadrados a la derecha, filtros de estado (toggle): naranja `#FEA039` check-in (campana), azul `#689FFF` estancia (cama), morado `#AE78AA` check-out (mano/salida).

## Panel de habitaciones
- Cuadrícula de 11 columnas centrada (tarjetas 78px, gap 12, última fila centrada).
- Tarjeta = cabecera de estado + número grande:
  - **Estancia**: cabecera `#8FB4DE`, cuerpo `#E9F2FB`
  - **Check-in**: cabecera `#FDA03B`, cuerpo `#FFF1D7`
  - **Check-out**: cabecera `#AE78AA`, cuerpo `#F7D9F5`
- Una habitación puede aparecer varias veces (segmentos: salida + entrada el mismo día).
- Badge `B.` (Booking) blanco en la esquina inferior derecha de algunas tarjetas; la 116 lleva badge de marcador `🔖 1`.
- Plantas 1, 2 y 8 transcritas literalmente de la captura; las plantas 3–7 (fuera del encuadre) se generan con el mismo patrón.

## FAB de búsqueda
- Botón flotante negro con lupa (abajo derecha); al pulsarlo se abre un campo que filtra por número de habitación en vivo.
