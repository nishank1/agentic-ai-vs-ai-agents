from __future__ import annotations

import logging
from typing import Any

from .config import load_runtime_config


def configure_logging(level: str | None = None) -> None:
    resolved_level = level or load_runtime_config(require_api_key=False).log_level
    numeric_level = getattr(logging, resolved_level.upper(), logging.INFO)

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


def log_event(logger: logging.Logger, event: str, **fields: Any) -> None:
    logger.info(event, extra={"event_fields": fields})
