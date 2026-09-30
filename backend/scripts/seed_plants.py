"""Populate the plants table from the census file plantas.md.

Usage (from the backend folder):

    .venv/bin/python scripts/seed_plants.py
    .venv/bin/python scripts/seed_plants.py /ruta/a/otro/plantas.md
"""
from __future__ import annotations

import sys
from pathlib import Path

# Make the "app" package importable regardless of the working directory.
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_DIR))

from app.core.config import settings  # noqa: E402
from app.core.database import get_session_factory  # noqa: E402
from app.models.plant import Plant  # noqa: E402
from sqlalchemy import text  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Cells that mean "no data" in the census.
MISSING_VALUES = {"", "—", "-", "--", "–", "−"}


def clean(value: str) -> str | None:
    """Return the trimmed value, or None when the cell is empty."""
    text = value.strip()
    if text in MISSING_VALUES:
        return None
    return text


def format_common_name(value: str) -> str | None:
    """Convert a common name to Title Case: "MANGO" -> "Mango"."""
    text = clean(value)
    if text is None:
        return None
    return text.title()


def format_scientific_name(value: str) -> str | None:
    """Convert a scientific name to binomial case: "Mangifera indica"."""
    text = clean(value)
    if text is None:
        return None
    text = text.replace("*", "").strip()
    parts = text.split()
    if not parts:
        return None
    return " ".join([parts[0].capitalize()] + [p.lower() for p in parts[1:]])


def format_trunk_shape(value: str) -> str | None:
    """Convert a trunk shape to sentence case: "RECTO" -> "Recto"."""
    text = clean(value)
    if text is None:
        return None
    return text.capitalize()


def parse_float(value: str) -> float | None:
    """Parse a decimal number, returning None for empty cells."""
    text = clean(value)
    if text is None:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_height(value: str) -> float | None:
    """Parse a height like "07 m" or "2.8 m" into meters."""
    text = clean(value)
    if text is None:
        return None
    text = text.replace("m", "").replace("M", "").strip()
    try:
        return float(text)
    except ValueError:
        return None


def parse_int(value: str) -> int | None:
    """Parse an integer, returning None for empty cells."""
    text = clean(value)
    if text is None:
        return None
    try:
        return int(text)
    except ValueError:
        return None


def parse_table(data: str) -> list[dict[str, str | float | None]]:
    """Extract the plant rows from the Markdown table."""
    lines = [line for line in data.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        raise ValueError("No se encontró una tabla válida en el archivo.")

    header = [cell.strip() for cell in lines[0].strip().strip("|").split("|")]
    body = lines[2:]  # skip header and separator

    number_index = header.index("N°")
    name_index = header.index("NOMBRE COMÚN")
    scientific_index = header.index("NOMBRE CIENTÍFICO")
    origin_index = header.index("CONTINENTE DE ORIGEN")
    dap_index = header.index("DAP / cm")
    trunk_index = header.index("FORMA DEL FUSTE")
    height_index = header.index("ALTURA APROX.")

    rows: list[dict[str, str | float | None]] = []
    for line in body:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < len(header):
            continue

        census_number = parse_int(cells[number_index])
        rows.append(
            {
                "census_number": census_number,
                "common_name": format_common_name(cells[name_index]),
                "scientific_name": format_scientific_name(cells[scientific_index]),
                "origin": clean(cells[origin_index]),
                "dap": parse_float(cells[dap_index]),
                "trunk_shape": format_trunk_shape(cells[trunk_index]),
                "height": parse_height(cells[height_index]),
                "qr_code_url": (
                    f"{settings.public_base_url}/planta/{census_number}"
                    if census_number is not None
                    else None
                ),
            }
        )
    return rows


def main() -> None:
    file_path = Path(sys.argv[1]) if len(sys.argv) > 1 else PROJECT_ROOT / "plantas.md"

    if not file_path.exists():
        raise FileNotFoundError(f"No existe el archivo: {file_path}")

    data = file_path.read_text(encoding="utf-8")
    rows = parse_table(data)

    if not rows:
        print("No se encontraron filas para importar.")
        return

    factory = get_session_factory()
    with factory() as session:
        # Clear previous data and reset the id sequence.
        session.execute(text("TRUNCATE TABLE plants RESTART IDENTITY"))
        session.add_all(Plant(**row) for row in rows)
        session.commit()

    null_names = sum(1 for row in rows if row["common_name"] is None)
    print(f"Archivo: {file_path.name}")
    print(f"Filas leídas: {len(rows)}")
    print(f"Filas insertadas: {len(rows)}")
    print(f"Filas sin nombre común: {null_names}")
    print(f"URL base del QR: {settings.public_base_url}")
    print("Importación completada.")


if __name__ == "__main__":
    main()
