# Evidencia 3: optimización de procesos con GitHub Actions

Continúa las Evidencias 1 (scraping de Tecnoplaza) y 2 (Git, GitHub y flujo DevOps).

## Qué se automatiza

```
push / PR ──► ci.yml ──► lint ║ pruebas (3.11, 3.12)

main / cron / manual ──► deploy.yml
    build (pruebas → scraping → verificación)
      └► deploy (GitHub Pages)
          └► verificar-produccion (HTTP 200 + contenido)
              └► notificar-fallo (issue si algo falló)

tag v* ──► release.yml ──► Release con portatiles.csv
```

## Decisiones

- **Fallar antes de publicar.** `main.py` sale con error si no hay productos y
  `src/verificacion.py` revisa `index.html`, `portatiles.csv` y precios antes de subir el artefacto.
  Si Tecnoplaza cambia su JSON, el sitio anterior sigue en línea.
- **Comprobar producción.** Tras el despliegue se pide la URL publicada, con reintentos, y se
  exige HTTP 200 y el texto «Catálogo».
- **Visibilidad.** Si cualquier job falla, se abre un issue con la etiqueta `despliegue` y el
  enlace a la ejecución (sin duplicarlo si ya hay uno abierto).
- **Eficiencia.** Caché de pip, jobs en paralelo, `concurrency` para cancelar CI obsoleto y
  `timeout-minutes` para que nada quede colgado.
- **Seguridad.** Permisos mínimos por workflow y por job; Dependabot mensual para acciones y pip.
- **Escalabilidad.** Cambiar de colección o de tienda solo implica modificar `COLECCION`/`BASE`
  en `src/scraper.py`; el pipeline no cambia. Los releases por etiqueta dejan versiones
  reproducibles con su CSV.

## Cómo probarlo

1. Abrir un PR desde una rama `feature/...` hacia `main` y ver `ci.yml` en verde.
2. Fusionar y ver `deploy.yml` hasta «Comprobar el sitio publicado».
3. Crear una etiqueta: `git tag -a v1.0.0 -m "Primera versión" && git push origin v1.0.0`.
4. Para ver el aviso de fallo, ejecutar *Deploy* con `COLECCION` apuntando a un handle inexistente
   en una rama de prueba.
