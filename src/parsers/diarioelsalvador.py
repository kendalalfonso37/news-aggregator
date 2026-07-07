import json
import re

from bs4 import BeautifulSoup

from .base import BaseParser


class DiarioElSalvadorParser(BaseParser):

    BASE_URL = "https://diarioelsalvador.com/"

    BLACKLIST = frozenset(
        {
            "facebook",
            "twitter",
            "instagram",
            "youtube",
            "linkedin",
            "telegram",
            "whatsapp",
            "mailto:",
            "javascript:",
            "/feed",
            "/tag/",
            "/author/",
            "/autor/",
            "/category/",
            "/wp-json/",
            "/wp-admin/",
            "/search/",
            "/buscar/",
            "/contacto",
            "/contactenos",
            "/epaper",
            "/terminos-y-condiciones",
            "/acerca-de-nosotros",
            "/video",
            "/clima",
        }
    )

    ARTICLE_PATTERN = re.compile(r"/\d+$")

    def _is_candidate(self, url: str) -> bool:
        """
        Diario El Salvador suele terminar las noticias
        con un ID numérico.
        """

        return bool(self.ARTICLE_PATTERN.search(url))

    def is_article(self, html: str) -> bool:

        soup = BeautifulSoup(html, "html.parser")

        if soup.find("article"):
            return True

        if soup.find("meta", property="article:published_time"):
            return True

        for script in soup.find_all("script", type="application/ld+json"):

            try:

                data = json.loads(script.string)

            except Exception:
                continue

            if isinstance(data, dict):

                if data.get("@type") == "NewsArticle":
                    return True

            elif isinstance(data, list):

                for item in data:

                    if item.get("@type") == "NewsArticle":
                        return True

        return False

    def parse_article(self, html: str):

        raise NotImplementedError("parse_article() todavía no implementado.")
