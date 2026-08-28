# Pestaña "Reseñas" — Checklist funcional (del boceto del usuario)

El mockup (index.html) debe contener TODOS estos elementos, adaptados al diseño Jaippy (ver BRAND.md). Es un mockup interactivo: los controles deben funcionar con datos de ejemplo.

## Barra superior (replica la herramienta actual)
- [ ] Logo "jaippy" (izquierda).
- [ ] Selector de hotel: "[5] Hotel Jaippy" con desplegable, y subtítulo con objetivo ("Objetivo: 9,0 · quedan XXX días").
- [ ] Chips de KPIs a la derecha: 8,71 (delta verde), 20,53% (delta roja), 40,96 € (delta verde), badge de nota "8,7", avatar de usuaria "EM".
- [ ] Fila de navegación por pestañas (pestañas nuevas; por ahora solo "Reseñas" activa con píldora destacada).

## Cabecera de la vista
- [ ] Título "Reseñas" (h1).
- [ ] Contador de reseñas del periodo filtrado: "30 reseñas" (se actualiza al filtrar).
- [ ] Filtro de fuente: segmentado Booking / Google (con opción de ver todas).
- [ ] Selector de periodo con opciones: "Hoy", "Últimos 7 días", "Últimos 30 días" (funcional: filtra los datos).

## Escala de puntuación (0–10)
- [ ] Barra horizontal de escala 0 a 10 con tramos de color (rojo → ámbar → verde).
- [ ] Números 0–10 visibles a lo largo de la escala y extremos 0 y 10 en círculos.
- [ ] Marcadores/burbujas de referencia en valores intermedios (4,0 · 5,5 · 7,0 · 8,0 · 9,0; el "10" es el propio círculo del extremo derecho).
- [ ] Marcador oscuro destacado "Tu hotel · 8,7" posicionado sobre la escala (se recalcula con el filtro).

## Gestión de Respuestas (tarjeta con gauge)
- [ ] Título "Gestión de Respuestas".
- [ ] Donut/gauge con porcentaje grande (p. ej. 63,6%).
- [ ] Cifra secundaria de variación debajo (p. ej. −36,4).
- [ ] Se recalcula al filtrar o al marcar reseñas como respondidas.

## Tarjeta "Reseñas recientes"
- [ ] Título "Reseñas recientes" + subtítulo "Gestiona el contacto y la respuesta por separado."
- [ ] Leyenda superior derecha: Contacto · Respuesta · Ver reseña.
- [ ] Lista/tabla de reseñas con columnas: Huésped (avatar con inicial de la fuente + nombre + "Booking · Habitación NNN" o "Google"), Fecha, Nota (chip de color: verde alta, ámbar media, roja baja; formato "10 / 10" en Booking y "5 / 5" en Google), Contacto, Respuesta, chevron para expandir.
- [ ] Botón "Contactar" por fila → al pulsarlo pasa a estado "Contactado" (chip azulado con check).
- [ ] Estado de respuesta por fila: chip "Pendiente" → pasa a "Respondida" (chip verde) al marcarla.
- [ ] Las filas se expanden (chevron o clic) mostrando el detalle de la reseña.

## Detalle de reseña expandido
- [ ] Título de la reseña con icono de enlace externo.
- [ ] Texto completo de la reseña.
- [ ] Barra de acciones: "Responder en Google/Booking" (según fuente), "Marcar como respondida", "Crear caso", "Publicar", y menú "⋯".
- [ ] Las acciones dan feedback (toast) y actualizan estados/gauge donde aplique.

## Datos de ejemplo
- [ ] ~30 reseñas repartidas en los últimos 30 días (algunas de hoy), mezcla Booking/Google, notas variadas (altas, medias y bajas), textos realistas en español.

## Estilo
- [ ] Todo adaptado a BRAND.md: fondo Ivory, tarjetas Cotton radios grandes, primario Amber, texto Midnight, títulos Fraunces, cuerpo Instrument Sans, iconos outline finos.
