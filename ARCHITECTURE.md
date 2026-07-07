# Arquitectura

## Visión general

El proyecto está dividido por responsabilidades para facilitar el mantenimiento y permitir agregar nuevos periódicos sin modificar el núcleo del sistema.

```text
src/

├── cli.py
├── crawler.py
├── registry.py
│
├── config/
│   └── sources.yaml
│
├── models/
│   └── news.py
│
└── parsers/
    ├── base.py
    ├── diarioelsalvador.py
    ├── laprensagrafica.py
    ├── ...
```

---

# Componentes

## CLI

Responsabilidades:

* Leer `sources.yaml`.
* Obtener el parser correspondiente desde `registry.py`.
* Invocar el crawler.
* Mostrar resultados.
* Ejecutar futuras opciones de línea de comandos.

El CLI no contiene lógica de scraping.

---

## Crawler

Responsabilidades:

* Descargar HTML.
* Configurar encabezados HTTP.
* Manejar timeouts.
* Invocar los parsers.
* Manejar errores de red.

El crawler no conoce la estructura HTML de ningún periódico.

---

## Registry

El registry mantiene el mapa entre el identificador definido en `sources.yaml` y la clase correspondiente.

Ejemplo:

```python
PARSERS = {
    "diarioelsalvador": DiarioElSalvadorParser,
}
```

Agregar un nuevo parser requiere:

1. Crear el archivo del parser.
2. Registrarlo en `registry.py`.
3. Agregar la entrada correspondiente en `sources.yaml`.

---

## BaseParser

Todos los parsers heredan de `BaseParser`.

Funcionalidades comunes:

* Normalización de URLs.
* Descubrimiento de enlaces.
* Eliminación de duplicados.
* Validación de dominio.
* Exclusión de extensiones.
* Exclusión mediante blacklist.

Cada parser implementa únicamente la lógica específica del medio.

---

## Parsers

Cada parser conoce exclusivamente un periódico.

Ejemplo:

```text
DiarioElSalvadorParser
```

Responsabilidades:

* Definir `BASE_URL`.
* Definir `BLACKLIST`.
* Implementar `is_article()`.
* Implementar `parse_article()`.
* Sobrescribir `_is_candidate()` cuando sea necesario.

Los parsers nunca realizan solicitudes HTTP.

---

## Sources

Los periódicos se configuran en `config/sources.yaml`.

Ejemplo:

```yaml
sources:

  - name: Diario El Salvador
    html: https://diarioelsalvador.com/
    parser: diarioelsalvador
```

Esto permite agregar nuevos medios sin modificar el CLI.

---

## Modelo News

Representa una noticia completamente parseada.

```python
@dataclass(slots=True)
class News:
    source: str
    title: str
    link: str
    published_at: datetime | None
    scraped_at: datetime
    category: str | None = None
```

En el futuro podrán añadirse:

* author
* summary
* content

sin afectar el flujo principal.

---

# Flujo de ejecución

```text
CLI
 │
 ▼
Leer sources.yaml
 │
 ▼
Registry
 │
 ▼
Instanciar parser
 │
 ▼
Crawler descarga HTML
 │
 ▼
discover_urls()
 │
 ▼
URLs candidatas
 │
 ▼
Descargar cada URL
 │
 ▼
is_article()
 │
 ├── False → descartar
 │
 └── True
        │
        ▼
parse_article()
        │
        ▼
News
        │
        ▼
Exportadores
```

---

# Principios de diseño

* Una única responsabilidad por clase.
* Los parsers no descargan contenido.
* El crawler no interpreta HTML.
* El CLI únicamente orquesta.
* Evitar duplicación de lógica.
* Favorecer la reutilización mediante `BaseParser`.

---

# Evolución prevista

## Corto plazo

* Implementar `parse_article()`.
* Exportación a TXT.
* Exportación a JSONL.

## Mediano plazo

* Playwright como motor de navegación.
* Descubrimiento de páginas adicionales.
* Crawling con profundidad configurable.
* Descarga concurrente.

## Largo plazo

* Base de datos SQLite.
* Índices de búsqueda.
* Clustering semántico.
* Embeddings.
* Detección automática de cobertura y blind spots.
* API REST para consultar noticias.
