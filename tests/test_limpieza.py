from src.limpieza import parsear_precio, es_portatil, calcular_descuento, limpiar


def test_parsear_precio_formatos():
    assert parsear_precio("$ 1.899.900") == 1899900
    assert parsear_precio("1899900.00") == 1899900
    assert parsear_precio(None) is None


def test_es_portatil():
    assert es_portatil("Portátil Lenovo V14")
    assert not es_portatil("Mouse inalámbrico")


def test_descuento():
    assert calcular_descuento(900, 1000) == 10.0
    assert calcular_descuento(1000, 900) == 0.0


def test_limpiar_quita_duplicados_e_inconsistencias():
    datos = [
        {"nombre": "Laptop A", "url": "u1", "precio_actual": "$ 1.000", "precio_anterior": "$ 900"},
        {"nombre": "Laptop A", "url": "u1", "precio_actual": "$ 1.000", "precio_anterior": None},
        {"nombre": "Laptop B", "url": "u2", "precio_actual": "$ 2.000", "precio_anterior": "$ 2.500"},
    ]
    df = limpiar(datos)
    assert len(df) == 2
    assert df["url"].is_unique
    assert (df["precio_anterior"].isna() | (df["precio_anterior"] >= df["precio_actual"])).all()
