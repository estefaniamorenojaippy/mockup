# Jaippy — Tokens de marca (extraído de Brand Guidelines 2025–2026)

## Colores
| Token | Hex | Uso |
|---|---|---|
| Saffron | `#FFA13B` | Acento cálido, hovers, gradiente |
| Amber | `#FFBC27` | **Color primario** (paleta reducida), CTAs, gráficas |
| Sunflower | `#FFD03B` | Acento claro, fondos suaves, gradiente |
| Sunrise Gradient | `#FFA13B → #FFD03B` | Elementos destacados |
| Midnight Gray | `#191919` | Texto principal, elementos oscuros |
| Charcoal Gray | `#232323` | Superficies oscuras secundarias |
| Ivory White | `#F4EEE6` | **Fondo de página** |
| Cotton White | `#FFFCF7` | Tarjetas y superficies claras |

Paleta reducida (UI): Midnight Gray + Amber + Cotton White.
Proporción de uso "Racional" (producto/datos): 40% oscuro, 40% blanco, 20% amber.

## Tipografía
- **Títulos (uso editorial/marca)**: Fraunces (serif, Google Fonts)
- **Cuerpo de texto**: Instrument Sans (Google Fonts)

⚠️ **En el producto (app) NO se usa Fraunces.** Confirmado por el usuario con capturas de la app real (11 ago 2026): toda la interfaz, incluidos los títulos de sección tipo "Análisis de experiencias", va en la sans (Instrument Sans). Fraunces queda reservada para material de marca, no para UI.

## Tokens de UI de la app real — MUESTREADOS PÍXEL A PÍXEL (fuente de verdad)
Extraídos con PIL de capturas reales de la app (11 ago 2026). Prevalecen sobre todo lo anterior.

| Token | Hex | Uso |
|---|---|---|
| Fondo de página | `#f3ede6` | Fondo general |
| Tarjetas y barras | `#FFFFFF` | Blanco puro, radio 24px, sombra suave |
| Navy | `#003B95` | Títulos de sección, subtítulos destacados, badges de puntuación |
| Olive/gris cálido | `#787572` | Etiquetas de nav inactivas, cabeceras de columna, leyendas |
| Amber | `#FFBC27` | Barras de progreso, tiles destacados |
| Saffron activo | `#FFA43B` | Texto e icono de la pestaña activa |
| Píldora activa | `#FFF3E7` | Fondo de la pestaña activa |
| Rojo | `#F0264B` sobre `#FFE6E9` | Deltas negativos y barras de puntuaciones negativas |
| Verde | `#25BE6F` | Deltas positivos |
| Gris delta neutro | `#F0F0F0` | Fondo del delta 0% |
| Gris icono | `#D9D9D9` | Iconos decorativos de KPI en la barra superior |
| Pista de barras | `#F2E8D2` (informes) / `#F0F0F0` (gráficas) | Fondo de barras |
| Amarillo avatar | `#F4C014` | Avatar de usuaria, con punto verde de conexión |
| Texto principal | `#232323` | Cifras y textos en negrita |

## Barra superior (definitiva, replicada de la app real)
Fondo **blanco**. Logo `jaippy` (extraído del brand book pág. 26) · `[11] Hotel Jaippy` + chip gris `ClassOne` + chevron · subtítulo `Objetivo 9,2 - quedan 55 días` · KPIs sin borde, icono gris claro a la izquierda (símbolo "j" de marca, fotos+estrella, tarjetas+10): `9,113` (0% →), `26,18%` (−4,7% ↘), `46,39%` (−0,1% ↘) — deltas en píldora de color con flecha diagonal · badge azul `#003B95` con `9,1` · avatar amarillo `EM` con punto verde.

## Barra de pestañas (definitiva)
Fondo blanco, borde inferior `#f3ede6`, pestañas centradas con radio 9px. Activa: fondo `#FFF3E7`, texto e icono `#FFA43B`. Inactivas: texto e icono `#787572`. Orden acordado con el usuario: **Home (solo icono de casa) · Reseñas (sin icono) · Habitaciones (icono de cama) · Analíticas (icono + chevron) · Informes (icono + chevron)**.

## Logotipo
El wordmark y el símbolo "j" están extraídos del brand book (páginas 26 y 29) e incrustados en el HTML como data URI, además de guardados en `assets/jaippy-logo.png` y `assets/jaippy-mark.png`. **No imitar el logo con tipografía.**

## Iconos
Estilo outline de trazo fino (~1.5–2px), esquinas y remates redondeados, monocolor Midnight. (Estética tipo Lucide/Feather.)

## Estética general de la app actual
- Fondo crema (Ivory), tarjetas blancas (Cotton) con radios grandes (16–20px) y sombras muy suaves.
- Barra superior clara: logo "jaippy" + selector de hotel a la izquierda, chips de KPIs a la derecha.
- Navegación por pestañas tipo píldora; la activa lleva fondo ámbar claro.
- Gráficas dominadas por naranjas/ámbar; chips de estado verdes/rojos para semántica de datos.
- Los colores semánticos (verde éxito, rojo alerta) se permiten en datos, en tonos apagados que armonicen con la paleta.
