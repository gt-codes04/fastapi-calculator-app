import logging
from logging.config import dictConfig

def configure_logging(level: str = "INFO") -> None:
    dictConfig({
        "version": 1,
        "formatters": {
            "std": {"format": "%(asctime)s %(levelname)s [%(name)s] %(message)s"}
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "std"}
        },
        "root": {"level": level, "handlers": ["console"]},
        "disable_existing_loggers": False,
    })
