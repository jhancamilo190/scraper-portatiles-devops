from datetime import datetime
from pathlib import Path


def generar_html(df, ruta="site/index.html", articulo="Lenovo V14"):
    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    destacado = df[df["nombre"].str.contains(articulo, case=False, na=False)]
    tabla = df.to_html(index=False, classes="tabla", border=0)
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<title>Precios de portátiles</title>
<style>body{{font-family:sans-serif;margin:2rem}}.tabla td,.tabla th{{padding:4px 8px}}</style>
</head><body>
<h1>Monitoreo de precios de portátiles - Tecnoplaza</h1>
<p>Actualizado: {datetime.now():%Y-%m-%d %H:%M} | Productos: {len(df)}</p>
<h2>Artículo seleccionado: {articulo}</h2>
{destacado.to_html(index=False, border=0) if len(destacado) else "<p>No encontrado hoy.</p>"}
<h2>Catálogo</h2>{tabla}
</body></html>"""
    Path(ruta).write_text(html, encoding="utf-8")
    return ruta
