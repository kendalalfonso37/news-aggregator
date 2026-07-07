
import feedparser
from models import News
from dateutil import parser


def collect_rss(source_name: str, rss_url: str):

    feed = feedparser.parse(rss_url)

    news = []

    for entry in feed.entries:

        try:

            published = parser.parse(
                entry.get("published", "")
            )

        except Exception:
            continue

        news.append(
            News(
                title=entry.title,
                link=entry.link,
                published=published,
                source=source_name
            )
        )

    return news