# News Aggregator - Crawler de noticias (El Salvador)

Este proyecto es un crawler/aggregador de noticias orientado a recopilar artículos y titulares de medios relevantes de El Salvador. Está diseñado para extraer, normalizar y almacenar contenido de forma periódica para su posterior análisis o publicación.

Características principales
- Extracción de titulares, resúmenes, fecha y enlace original.
- Soporte para múltiples fuentes de prensa salvadoreña.
- Normalización básica de contenido (limpieza de HTML, manejo de codificación).
- Programación periódica para crawleo frecuente.
- Salida en formatos comunes (JSON/CSV) y opción para base de datos.

Instalación
1. Clona el repositorio.
2. Crea un entorno virtual (recomendado) e instala dependencias:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Configuración
- Ajusta la lista de medios en el archivo de configuración (`config/sources.yaml`).
- Configura la salida: carpeta de exportación o conexión a la base de datos.
- Establece la frecuencia del crawler (cron, scheduler interno o servicio).

Uso
- Ejecutar el crawler manualmente:

```bash
python run_crawler.py
```

- Para ejecuciones programadas, usar un scheduler (por ejemplo, cron, Windows Task Scheduler o celery/beat).

Buenas prácticas
- Respetar el archivo robots.txt y las políticas de cada medio.
- Evitar solicitudes demasiado frecuentes para no sobrecargar los servidores.
- Incluir user-agent identificable y datos de contacto si se realiza scraping sistemático.

Contribuciones
- Pull requests bienvenidas. Abrir issues para reportar bugs o proponer nuevas fuentes.

Licencia
- Pending...

Contacto
- Kendal Alfonso Sosa Montes (https://github.com/kendalalfonso37)

``` 
