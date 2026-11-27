import pandas as pd

from src.reporte import generar_html
from src.verificacion import verificar_salida


def _salida_valida(carpeta, filas=2):
    df = pd.DataFrame([
        {"nombre": f"Portátil {i}", "precio_actual": 1000000 + i} for i in range(filas)
    ])
    generar_html(df, ruta=str(carpeta / "index.html"))
    df.to_csv(carpeta / "portatiles.csv", index=False, encoding="utf-8-sig")


def test_salida_valida_no_tiene_problemas(tmp_path):
    _salida_valida(tmp_path)
    assert verificar_salida(tmp_path) == []


def test_carpeta_vacia_reporta_archivos_faltantes(tmp_path):
    problemas = verificar_salida(tmp_path)
    assert "falta index.html" in problemas
    assert "falta portatiles.csv" in problemas


def test_pocos_productos_es_un_problema(tmp_path):
    _salida_valida(tmp_path, filas=1)
    assert any("mínimo" in p for p in verificar_salida(tmp_path, minimo=5))


def test_producto_sin_precio_es_un_problema(tmp_path):
    _salida_valida(tmp_path)
    csv = tmp_path / "portatiles.csv"
    pd.DataFrame([{"nombre": "X", "precio_actual": None}]).to_csv(csv, index=False)
    assert "hay productos sin precio_actual" in verificar_salida(tmp_path)
