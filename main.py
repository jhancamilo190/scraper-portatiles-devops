import sys
from pathlib import Path

from src.scraper import extraer
from src.limpieza import limpiar
from src.reporte import generar_html

if __name__ == "__main__":
    df = limpiar(extraer())
    if df.empty:
        # Fallar es mejor que publicar un catálogo vacío si el sitio cambió.
        print("ERROR: no se extrajo ningún producto; no se publica nada.")
        sys.exit(1)
    Path("site").mkdir(exist_ok=True)
    df.to_csv("site/portatiles.csv", index=False, encoding="utf-8-sig")
    print(generar_html(df), len(df), "productos")
