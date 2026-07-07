import yaml

from crawler import Crawler
from registry import PARSERS

def load_sources():

    with open(
        "config/sources.yaml",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)["sources"]

def main():

    crawler = Crawler()
    sources = load_sources()

    for source in sources:
        parser_name = source["parser"]
        
        try:
            parser_class = PARSERS[parser_name]
        except KeyError:
            print(
                f"[WARNING] "
                f"No existe un parser registrado para "
                f"'{parser_name}'. "
                f"Se omitirá '{source['name']}'."
            )
            continue

        parser = parser_class()

        try:
            urls = crawler.crawl(source, parser)
            for url in urls:
                # TODO: Almacenar resultados usando el modelo DiscoveredUrl para posteriormente construir un objeto News.
                print(f"  • {url}")
        except Exception as ex:
            print(
                f"[ERROR] "
                f"{source['name']}: {ex}"
            )
        
        # TODO: Implementar la lógica para almacenar los resultados de las URLs descubiertas y posteriormente construir objetos News a partir de ellas.


if __name__ == "__main__":
    main()