import time
import requests
from src.limpieza import es_portatil

BASE = "https://tecnoplaza.com.co"
COLECCION = "portatiles"  # usa el mismo handle de URL_LISTADO de tu notebook
HEADERS = {"User-Agent": "Proyecto academico IU Digital - Jhan Moreno"}


def extraer(max_paginas=3, pausa=2):
    registros = []
    for pagina in range(1, max_paginas + 1):
        url = f"{BASE}/collections/{COLECCION}/products.json?limit=250&page={pagina}"
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        productos = r.json().get("products", [])
        if not productos:
            break
        for p in productos:
            v = p["variants"][0]
            registros.append({
                "nombre": p["title"],
                "url": f"{BASE}/products/{p['handle']}",
                "precio_actual": v.get("price"),
                "precio_anterior": v.get("compare_at_price"),
                "disponible": v.get("available"),
            })
        time.sleep(pausa)
    return [r for r in registros if es_portatil(r["nombre"])] or registros
