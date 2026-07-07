import requests

class Crawler:

    def __init__(self, timeout=30):
        self.timeout = timeout

    def get(self, url: str) -> str:
        """
        Descarga el HTML de una página.
        """

        response = requests.get(
            url,
            timeout=self.timeout,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(X11; Linux x86_64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/138.0 Safari/537.36"
                )
            }
        )

        response.raise_for_status()

        return response.text

    def crawl(self, source: dict, parser):
        """
        Ejecuta el crawler para una fuente específica.
        """

        print(f"\n[{source['name']}]")

        html = self.get(source["html"])

        urls = parser.discover_urls(html)

        print(f"Se encontraron {len(urls)} URLs.")

        return urls