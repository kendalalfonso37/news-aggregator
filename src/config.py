from pathlib import Path
from typing import Any

import yaml


DEFAULT_SOURCES_PATH = Path("config/sources.yaml")


def load_sources(path: str | Path = DEFAULT_SOURCES_PATH) -> list[dict[str, str]]:
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("Sources config must be a YAML mapping.")

    sources = config.get("sources")
    if not isinstance(sources, list):
        raise ValueError("Sources config must include a 'sources' list.")

    return [_validate_source(source, index) for index, source in enumerate(sources)]


def _validate_source(source: Any, index: int) -> dict[str, str]:
    if not isinstance(source, dict):
        raise ValueError(f"Source at index {index} must be a mapping.")

    name = source.get("name")
    html = source.get("html")

    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"Source at index {index} must include a non-empty 'name'.")

    if not isinstance(html, str) or not html.strip():
        raise ValueError(f"Source at index {index} must include a non-empty 'html'.")

    return {"name": name, "html": html}
