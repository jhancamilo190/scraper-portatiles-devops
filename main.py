from pathlib import Path
from src.scraper import extraer
from src.limpieza import limpiar
from src.reporte import generar_html

if __name__ == "__main__":
    df = limpiar(extraer())
    Path("site").mkdir(exist_ok=True)
    df.to_csv("site/portatiles.csv", index=False, encoding="utf-8-sig")
    print(generar_html(df), len(df), "productos")
