from dataclasses import dataclass
from datetime import datetime

@dataclass
class News:
    source: str
    title: str
    link: str
    published_at: datetime | None
    scrapped_at: datetime
    category: str | None

