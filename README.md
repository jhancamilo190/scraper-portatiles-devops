# scraper-portatiles-devops

![CI](https://github.com/jhancamilo190/scraper-portatiles-devops/actions/workflows/ci.yml/badge.svg)

Scraper de precios de portátiles de Tecnoplaza (Shopify) con flujo DevOps: pruebas automáticas con GitHub Actions y publicación diaria en GitHub Pages.

**Página publicada:** https://jhancamilo190.github.io/scraper-portatiles-devops/

## Instalación y ejecución

Ejecuta el proyecto con:

- `python -m venv .venv`
- `pip install -r requirements.txt`
- `python -m pytest -v`
- `python main.py`

## Estructura

- `src/`: scraper, limpieza y reporte
- `tests/`: pruebas con pytest (sin internet)
- `.github/workflows/`: `ci.yml` (lint + pruebas) y `deploy.yml` (Pages)
- `main.py`: punto de entrada

## Flujo DevOps

rama → commit → push → PR → CI (flake8 + pytest) → merge → deploy → GitHub Pages, con ejecución diaria a las 7:00 a. m. (Colombia).

Ramas: `feature/`, `ci/`, `docs/`. Commits: `feat`, `test`, `ci`, `docs`.
