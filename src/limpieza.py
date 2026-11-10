import re
import pandas as pd

RE_PORTATIL = re.compile(r"port[aá]til|laptop|notebook", re.I)


def parsear_precio(texto):
    """Convierte '$ 1.899.900' o '1899900.00' en entero (pesos colombianos)."""
    if texto is None:
        return None
    if isinstance(texto, (int, float)):
        return int(texto)
    texto = str(texto).strip()
    if re.fullmatch(r"\d+\.\d{2}", texto):  # formato JSON de Shopify
        return int(float(texto))
    digitos = re.sub(r"[^\d]", "", texto)
    return int(digitos) if digitos else None


def es_portatil(nombre):
    return bool(nombre) and bool(RE_PORTATIL.search(nombre))


def calcular_descuento(actual, anterior):
    if not actual or not anterior or anterior <= actual:
        return 0.0
    return round((anterior - actual) / anterior * 100, 1)


def limpiar(registros):
    df = pd.DataFrame(registros)
    if df.empty:
        return df
    df["precio_actual"] = df["precio_actual"].apply(parsear_precio)
    df["precio_anterior"] = df["precio_anterior"].apply(parsear_precio)
    df = df.dropna(subset=["nombre", "precio_actual"])
    df = df.drop_duplicates(subset=["url"])
    # precio inconsistente (actual > anterior): se descarta el anterior
    mask = df["precio_anterior"].notna() & (df["precio_anterior"] < df["precio_actual"])
    df.loc[mask, "precio_anterior"] = None
    df["descuento_pct"] = [
        calcular_descuento(a, b) for a, b in zip(df["precio_actual"], df["precio_anterior"])
    ]
    return df.sort_values("precio_actual").reset_index(drop=True)
