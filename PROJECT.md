# SV News Aggregator

## Descripción

SV News Aggregator es un proyecto desarrollado en Python cuyo objetivo es recopilar noticias de medios digitales salvadoreños mediante crawling y scraping HTML.

A diferencia de un lector RSS, este proyecto navega directamente por los sitios web para descubrir artículos publicados, permitiendo trabajar incluso con medios que no ofrecen feeds RSS o cuyos feeds son incompletos.

El objetivo final es construir una base de datos unificada de noticias para realizar análisis posteriores sobre cobertura mediática y detección de blind spots (sesgos de cobertura).

---

# Objetivos

## Fase 1

* Descubrir artículos publicados por cada medio.
* Extraer:

  * Fuente
  * Título
  * Enlace
  * Fecha de publicación
  * Categoría
* Filtrar noticias por fecha.
* Filtrar noticias por palabras clave.
* Exportar resultados a TXT.
* Exportar resultados a JSONL.

## Fase 2

* Extraer contenido completo de cada noticia.
* Almacenar históricos.
* Normalizar categorías.
* Detectar noticias duplicadas.

## Fase 3

* Clustering de noticias.
* Embeddings.
* Comparación de cobertura entre medios.
* Detección de blind spots.
* Estadísticas de cobertura por tema.

---

# Principios del proyecto

Este proyecto prioriza:

* Simplicidad.
* Código limpio.
* Bajo acoplamiento.
* Alta cohesión.
* Arquitectura incremental.
* Parsers independientes.
* Fácil incorporación de nuevos medios.

Se evita la sobreingeniería.

No se utilizarán patrones complejos mientras no aporten un beneficio claro.

---

# Stack tecnológico

* Python 3.13
* Requests (temporalmente)
* BeautifulSoup4
* PyYAML
* Dataclasses
* datetime

Futuro:

* Playwright
* Typer
* SQLite
* JSONL
* Pandas
* Sentence Transformers
* OpenAI Embeddings

---

# Organización del proyecto

Cada periódico tiene su propio parser.

Todos los parsers heredan de una clase base común.

El crawler es independiente de los parsers.

Los parsers no realizan solicitudes HTTP.

La lógica HTTP pertenece únicamente al crawler.

---

# Modelo principal

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

---

# Flujo general

```text
Sources (sources.yaml)
        │
        ▼
Crawler
        │
        ▼
Descarga HTML
        │
        ▼
Parser.discover_urls()
        │
        ▼
URLs candidatas
        │
        ▼
Parser.is_article()
        │
        ▼
Parser.parse_article()
        │
        ▼
News
        │
        ▼
Exportadores
```

---

# Convenciones

* Cada parser debe ser autocontenido.
* No duplicar lógica entre parsers.
* Todo código reutilizable debe vivir en BaseParser.
* Mantener métodos pequeños y especializados.
* Los parsers reciben HTML y producen objetos; nunca descargan páginas.

---

# Estado actual

Actualmente el proyecto implementa:

* BaseParser
* DiarioElSalvadorParser
* Registry de parsers
* Crawler básico
* CLI inicial
* Descubrimiento de URLs

Las siguientes etapas consisten en implementar la detección de artículos y el parseo completo de cada noticia.
