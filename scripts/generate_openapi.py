"""Generate the OpenAPI 3.1 YAML spec file from the FastAPI app.

Run this script before each release to update openapi.yaml with the
current version and endpoint definitions:

    poetry run python scripts/generate_openapi.py
"""

import sys
from pathlib import Path

import yaml

# Ensure the src directory is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from calculator.api import app  # noqa: E402

OUTPUT = Path(__file__).resolve().parent.parent / "openapi.yaml"


def main():
    schema = app.openapi()
    yaml_content = yaml.dump(schema, sort_keys=False, allow_unicode=True)
    OUTPUT.write_text(yaml_content)
    print(f"OpenAPI spec (v{schema['info']['version']}) written to {OUTPUT}")


if __name__ == "__main__":
    main()
