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

from sqlalchemy import select  # noqa: E402

from app.core.database import get_session_factory  # noqa: E402
from app.models.plant import Plant  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Cells that mean "no data" in the census.
MISSING_VALUES = {"", "—", "-", "--", "–", "−"}


def clean(value: str) -> str | None:
    """Return the trimmed value, or None when the cell is empty."""
    text = value.strip()
    if text in MISSING_VALUES:
        return None
    return text


def clean_scientific_name(value: str) -> str | None:
    """Remove the Markdown italics markers around scientific names."""
    text = clean(value)
    if text is None:
        return None
    return text.replace("*", "").strip()


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


def parse_table(data: str) -> list[dict[str, str | None]]:
    """Extract the plant rows from the Markdown table."""
    lines = [line for line in data.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        raise ValueError("No se encontró una tabla válida en el archivo.")

    header = [cell.strip() for cell in lines[0].strip().strip("|").split("|")]
    body = lines[2:]  # skip header and separator

    name_index = header.index("NOMBRE COMÚN")
    scientific_index = header.index("NOMBRE CIENTÍFICO")
    origin_index = header.index("CONTINENTE DE ORIGEN")
    height_index = header.index("ALTURA APROX.")

    rows: list[dict[str, str | None]] = []
    for line in body:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < len(header):
            continue
        rows.append(
            {
                "common_name": clean(cells[name_index]),
                "scientific_name": clean_scientific_name(cells[scientific_index]),
                "origin": clean(cells[origin_index]),
                "height": parse_height(cells[height_index]),
                "qr_code_url": None,
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
        # Clear previous data to keep the import idempotent.
        session.query(Plant).delete()
        session.add_all(Plant(**row) for row in rows)
        session.commit()

    null_names = sum(1 for row in rows if row["common_name"] is None)
    print(f"Archivo: {file_path.name}")
    print(f"Filas leídas: {len(rows)}")
    print(f"Filas insertadas: {len(rows)}")
    print(f"Filas sin nombre común: {null_names}")
    print("Importación completada.")


if __name__ == "__main__":
    main()
