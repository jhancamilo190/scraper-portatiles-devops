"""Verificación de la salida antes de publicar (prueba de humo del despliegue)."""
import sys
from pathlib import Path

import pandas as pd


def verificar_salida(carpeta="site", minimo=1):
    """Devuelve una lista de problemas; vacía si la salida es publicable."""
    carpeta = Path(carpeta)
    problemas = []

    index = carpeta / "index.html"
    if not index.exists():
        problemas.append("falta index.html")
    elif "Catálogo" not in index.read_text(encoding="utf-8"):
        problemas.append("index.html no contiene el catálogo")

    csv = carpeta / "portatiles.csv"
    if not csv.exists():
        problemas.append("falta portatiles.csv")
    else:
        df = pd.read_csv(csv, encoding="utf-8-sig")
        if len(df) < minimo:
            problemas.append(f"solo {len(df)} productos (mínimo {minimo})")
        elif df["precio_actual"].isna().any():
            problemas.append("hay productos sin precio_actual")

    return problemas


if __name__ == "__main__":
    errores = verificar_salida(*(sys.argv[1:2] or ["site"]))
    for e in errores:
        print("ERROR:", e)
    if not errores:
        print("Salida verificada: lista para publicar.")
    sys.exit(1 if errores else 0)
