# Administrar encuestas — Constructor de encuestas

Se abre desde el menú de usuario (avatar EM) → **Administrar encuestas**. Objetivo: que el hotel diseñe la encuesta que reciben sus huéspedes al terminar la estancia.

## Diseño de marca
- [ ] **Logo**: subir el propio (queda incrustado como data URI) y botón "Quitar" para volver al de Jaippy.
- [ ] **Tipografía**: Instrument Sans, Fraunces, Georgia, Arial o Trebuchet.
- [ ] **Color principal**: selector de color. Tiñe estrellas, asteriscos de obligatoriedad, placeholders, píldoras seleccionadas y el botón de envío; el texto del botón se calcula (blanco o negro) según la luminancia para mantener el contraste.
- [ ] NO hay título de encuesta ni color de fondo configurable (decisión del usuario, 11-ago-2026).

## Preguntas
No hay preguntas fijas: **todas son editables y eliminables**, incluidas el NPS y la de calificación.

- [ ] Cada fila: texto de la pregunta + tipo + **asterisco de obligatoria** (gris apagado, ámbar activo) + eliminar. El asterisco va a la derecha, junto al eliminar.
- [ ] Tipos disponibles: Texto libre · Opciones (respuestas separadas por comas) · Sí/No · Escala 1–5 · **Estrellas 1–10** · **NPS 0–10**.
- [ ] Las de tipo **Estrellas** llevan su umbral: "Mostrar la pregunta condicionada si la nota es menor que **[5]** de 10" (por defecto 5, editable de 1 a 10).
- [ ] Cualquier pregunta situada después de una de estrellas puede marcarse con el interruptor **"Mostrar solo si la nota es baja"**; entonces aparece únicamente si la nota es inferior al umbral.
- [ ] Botón "Añadir pregunta".

### Preguntas de referencia (set definitivo dictado por el usuario, 12-ago-2026)
| # | Pregunta | Tipo | Obligatoria |
|---|---|---|---|
| 1 | En global, ¿Cómo calificaría su estancia en el HOTEL JAIPPY? | Estrellas 1–10 (umbral 5) | Sí |
| 2 | Cuéntanos qué ha pasado para que podamos mejorar | Texto libre · **condicionada** al umbral | Sí |
| 3 | ¿Cómo de probable es que recomiendes este hotel a otras personas? | NPS 0–10 | Sí |
| 4 | ¿Cómo nos ha conocido? | Opciones: Redes sociales · Sitio Web · Amigos o familiares · Otros | Sí |
| 5 | ¿Cómo ha sido la atención en Recepción? (Opcional) | Estrellas 1–5 | No |
| 6 | Puntúa nuestra limpieza (Opcional) | Estrellas 1–5 | No |
| 7 | Puntúa nuestro desayuno (Opcional) | Estrellas 1–5 | No |
| 8 | Restaurante (Opcional) | Estrellas 1–5 | No |
| 9 | SPA (Opcional) | Estrellas 1–5 | No |
| 10 | ¿Ha tenido algún problema durante su estancia? (Opcional) | Sí / No | Sí |

### Estilo de la encuesta (muestreado de las capturas del usuario)
- Cada pregunta va numerada con un **badge cuadrado** del color de marca.
- **NPS**: 11 tiles casi cuadrados, fondo crema (color de marca al 7%), número en el color de marca, radio 8px, sin borde; etiquetas "Nada probable" / "Extremadamente probable" en `#333333`.
- **Estrellas**: contorno fino (grosor 1) del color de marca, numeradas debajo en `#333333` peso normal. Las de 1–5 ocupan la mitad del ancho.
- **Opciones y Sí/No**: lista vertical de filas con fondo crema y **badge de letra A/B/C/D**, texto en el color de marca; al seleccionar, el fondo se refuerza al 22%.
- **Texto libre**: campo subrayado + ayuda "Pulsa Shift ⇧ + Intro ↵…".

## Vista previa del huésped (panel derecho, interactiva)
- [ ] Logo arriba; cada pregunta con su subtítulo en cursiva "Descripción (opcional)" y asterisco si es obligatoria.
- [ ] NPS: 11 botones 0–10 con etiquetas "Nada probable" / "Muy probable".
- [ ] Estrellas: 10 estrellas numeradas que se rellenan al puntuar.
- [ ] Texto libre: campo subrayado con placeholder "Escribe aquí tu respuesta..." y la ayuda "Pulsa **Shift ⇧** + **Intro ↵** para añadir un salto de línea".
- [ ] La pregunta condicionada aparece/desaparece en vivo según la nota y el umbral.
- [ ] "Enviar respuestas" valida solo las preguntas marcadas como obligatorias (y las condicionadas solo si están visibles).

## Cabecera
- [ ] Botones "Copiar enlace" y "Enviar a huéspedes".
