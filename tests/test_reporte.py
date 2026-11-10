import pandas as pd
from src.reporte import generar_html


def test_generar_html(tmp_path):
    df = pd.DataFrame([{"nombre": "Portátil Lenovo V14", "precio_actual": 1500000}])
    ruta = generar_html(df, ruta=str(tmp_path / "index.html"))
    contenido = open(ruta, encoding="utf-8").read()
    assert "Lenovo V14" in contenido
