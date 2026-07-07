from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class News:
    source: str
    title: str
    link: str
    published_at: datetime | None
    scraped_at: datetime
    category: str | None = None
    author: str | None = None
    summary: str | None = None
    content: str | None = None


@dataclass(slots=True)
class DiscoveredUrl:
    source: str
    url: str