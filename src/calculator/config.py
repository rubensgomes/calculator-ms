"""Application configuration loader.

Reads config.yaml and provides access to the server and logging
configuration sections.
"""

import logging.config
import os
from pathlib import Path

import yaml

_DEFAULT_CONFIG_PATH = "config.yaml"

_config: dict = {}


def load_config(config_path: str = _DEFAULT_CONFIG_PATH) -> dict:
    """Load application configuration from a YAML file.

    Reads the YAML file at *config_path*, parses it, and stores the
    result in the module-level ``_config`` dict.  If the file does not
    exist a warning is logged and the config remains empty.

    Args:
        config_path: Filesystem path to the YAML configuration file.

    Returns:
        The parsed configuration dictionary.
    """
    _config.clear()
    config_file = Path(config_path)
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            _config.update(yaml.safe_load(f) or {})
    else:
        logging.warning("Config file %s not found, using defaults", config_path)
    return _config


def get_server_config() -> dict:
    """Return the server configuration section.

    Returns:
        A dict with ``host`` and ``port`` keys.  Falls back to
        ``{"host": "0.0.0.0", "port": 8000}`` when no server section
        is present.
    """
    return _config.get("server", {"host": "0.0.0.0", "port": 8000})


def setup_logging() -> None:
    """Apply the logging configuration section via ``dictConfig``.

    Creates any log directories referenced by file handlers before
    applying the configuration.  Falls back to ``basicConfig`` at INFO
    level when no logging section is present.
    """
    log_config = _config.get("logging")
    if log_config:
        # Ensure the log directory exists for file handlers
        for handler in log_config.get("handlers", {}).values():
            filename = handler.get("filename")
            if filename:
                os.makedirs(os.path.dirname(filename), exist_ok=True)
        logging.config.dictConfig(log_config)
    else:
        logging.basicConfig(level=logging.INFO)
