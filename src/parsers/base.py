from abc import ABC, abstractmethod
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup


class BaseParser(ABC):

    BASE_URL = ""

    BLACKLIST = frozenset()

    EXCLUDED_EXTENSIONS = frozenset(
        {
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".svg",
            ".webp",
            ".pdf",
            ".zip",
            ".xml",
            ".rss",
        }
    )

    def __init__(self):

        if not self.BASE_URL:
            raise ValueError("BASE_URL must be defined.")

        self.base_domain = urlparse(self.BASE_URL).netloc

    def discover_urls(self, html: str) -> list[str]:

        soup = BeautifulSoup(html, "html.parser")

        discovered = set()

        for anchor in soup.find_all("a", href=True):

            url = self._normalize(anchor["href"])

            if url is None:
                continue

            if not self._is_internal(url):
                continue

            if self._has_excluded_extension(url):
                continue

            if self._is_blacklisted(url):
                continue

            if not self._is_candidate(url):
                continue

            discovered.add(url)

        return sorted(discovered)

    def _normalize(self, href: str) -> str | None:

        href = href.strip()

        if not href:
            return None

        if href.startswith("#"):
            return None

        absolute = urljoin(self.BASE_URL, href)

        absolute = absolute.split("?")[0]
        absolute = absolute.split("#")[0]

        return absolute.rstrip("/")

    def _is_internal(self, url: str) -> bool:

        parsed = urlparse(url)

        return parsed.netloc == self.base_domain

    def _has_excluded_extension(self, url: str) -> bool:

        path = urlparse(url).path.lower()

        return any(path.endswith(ext) for ext in self.EXCLUDED_EXTENSIONS)

    def _is_blacklisted(self, url: str) -> bool:

        url = url.lower()

        return any(item in url for item in self.BLACKLIST)

    def _is_candidate(self, url: str) -> bool:
        """
        Cada periódico puede redefinir esta lógica.
        """
        return True

    @abstractmethod
    def is_article(self, html: str) -> bool:
        pass

    @abstractmethod
    def parse_article(self, html: str):
        pass
