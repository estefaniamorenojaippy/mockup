# -*- coding: utf-8 -*-
"""Genera la versión publicable (Artifact) a partir de crm.html.

Hay una sola fuente de verdad: crm.html. El Artifact se publica desde el
archivo derivado, así que cualquier cambio en crm.html se refleja al
volver a ejecutar este script y republicar sobre la misma dirección.

Uso:  python tools/build-artifact.py
"""
import io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN  = os.path.join(RAIZ, "crm.html")
DESTINO = os.path.join(RAIZ, "artifact", "pipe-crm.html")

s = io.open(ORIGEN, encoding="utf-8").read()

# El publicador envuelve el contenido en su propio <!doctype>/<head>/<body>,
# con charset, viewport y un reset mínimo: hay que entregar sólo el interior.
fuera = [
    r"<!doctype html>\s*",
    r"</?html[^>]*>\s*",
    r"</?head>\s*",
    r"</?body>\s*",
    r'<meta charset="utf-8">\s*',
    r'<meta name="viewport"[^>]*>\s*',
]
for patron in fuera:
    s = re.sub(patron, "", s, flags=re.I)

s = s.strip() + "\n"

# Comprobaciones: lo que debe quedar y lo que no debe colarse
for prohibido in ("<!doctype", "<html", "<head", "<body"):
    # \b para no confundir <header> con <head>
    if re.search(re.escape(prohibido) + r"\b", s, flags=re.I):
        sys.exit("ERROR: ha quedado una etiqueta de envoltorio: " + prohibido)
for necesario in ("<title>", "<style>", "<script>", 'id="board"'):
    if necesario not in s:
        sys.exit("ERROR: falta " + necesario)

os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(s)
print("generado:", DESTINO, "·", len(s), "caracteres")
