# scraper-portatiles-devops

![CI](https://github.com/jhancamilo190/scraper-portatiles-devops/actions/workflows/ci.yml/badge.svg)
![Deploy](https://github.com/jhancamilo190/scraper-portatiles-devops/actions/workflows/deploy.yml/badge.svg)

Scraper de precios de portátiles de Tecnoplaza (Shopify) con flujo DevOps: pruebas automáticas con GitHub Actions y publicación diaria en GitHub Pages.

**Página publicada:** https://jhancamilo190.github.io/scraper-portatiles-devops/

## Instalación y ejecución

```bash
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -v              # pruebas (sin internet)
python main.py                   # scraping -> carpeta site/
python -m src.verificacion site  # comprueba que la salida es publicable
```

## Estructura

- `src/`: scraper, limpieza, reporte y verificación de la salida
- `tests/`: pruebas con pytest (sin internet)
- `.github/workflows/`: `ci.yml`, `deploy.yml` y `release.yml`
- `main.py`: punto de entrada (termina con error si no extrae productos)

## Flujo DevOps

rama → commit → push → PR → CI (flake8 + pytest) → merge → deploy → GitHub Pages, con ejecución diaria a las 7:00 a. m. (Colombia).

Ramas: `feature/`, `ci/`, `docs/`, `chore/`. Commits: `feat`, `test`, `ci`, `docs`, `chore`.

## Automatización con GitHub Actions

| Workflow | Cuándo corre | Qué hace |
|---|---|---|
| `ci.yml` | Cada push y cada PR hacia `main` | `flake8` y `pytest` en jobs paralelos (Python 3.11 y 3.12), caché de pip, cancela ejecuciones obsoletas |
| `deploy.yml` | Push a `main`, a diario 7:00 a. m. y manual | Pruebas → scraping → verificación → publicación en Pages → comprobación del sitio publicado → issue automático si algo falla |
| `release.yml` | Al crear una etiqueta `v*` | Pruebas, scraping y Release de GitHub con el CSV adjunto |

Más detalle en [`docs/evidencia-3.md`](docs/evidencia-3.md).
