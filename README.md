# pynop-cli

Python NopCommerce CLI and database access for MSSQL (pyodbc). Extracted from the sync project for standalone use.

## Features

- **DB layer**: `AutoDao` and `DB` for MSSQL (pyodbc) with parameterized queries.
- **NopCommerce helpers**: `NopTool`, `NopData`, `NopQuery` for product, category, picture, manufacturer, and related Nop entities.
- **CLI**: `nopcommerce` command for quick queries and inspections.

## Installation

```bash
pip install -e .
# or from PyPI (when published): pip install pynop-cli
```

Requires **ODBC Driver 17 for SQL Server** (or compatible) and a working MSSQL instance.

## Configuration

Connection is via a config dict or environment variables.

**Config dict** (e.g. when used from another app):

```python
from pynop import AutoDao, NopTool, NopData

config = {
    "db_engine": "MSSQL",
    "db_server": "your-server",
    "db_name": "NOPCommerce",
    "db_username": "sa",
    "db_password": "secret",
}
dao = AutoDao(config)
# Optional: set as default for NopTool
NopTool.set_dao(dao)
```

**Environment variables** (for CLI or standalone scripts):

- `NOP_DB_SERVER`, `NOP_DB_NAME`, `NOP_DB_USERNAME`, `NOP_DB_PASSWORD`
- Or `NOP_DB_DSN` for DSN-based connection.

## CLI

```bash
nopcommerce product get-by-sku MY-SKU
nopcommerce product list --limit 10
nopcommerce ping
```

## Use from sync project

In the sync repo, install this package and use a thin adapter in `core/db.py` that imports `AutoDao` from `pynop` and passes `DB_CONFIG[env][db_type]` so existing `AutoDao("nop")` / `AutoDao("staging")` calls keep working.

## License

MIT
