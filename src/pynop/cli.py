"""
CLI entry point for nopcommerce. Use config from env (NOP_DB_*).
"""
import argparse
import os
import sys


def _ensure_config():
    from pynop.config import get_connection_dict_from_env
    conn = get_connection_dict_from_env("NOP_DB")
    if not conn.get("db_server") and not conn.get("db_name"):
        if os.environ.get("NOP_DB_DSN"):
            return conn
        print("Set NOP_DB_SERVER, NOP_DB_NAME, NOP_DB_USERNAME, NOP_DB_PASSWORD (or NOP_DB_DSN).", file=sys.stderr)
        sys.exit(1)
    return conn


def cmd_ping(_args):
    """Test DB connection."""
    from pynop.db import AutoDao
    conn = _ensure_config()
    dao = AutoDao(conn)
    v = dao.get_one_value("SELECT 1")
    print("OK" if v == 1 else "Unexpected result")
    dao.db.close()


def cmd_product_get_by_sku(args):
    """Get product by SKU."""
    from pynop.db import AutoDao
    conn = _ensure_config()
    dao = AutoDao(conn)
    sql = "SELECT * FROM Product WHERE Sku = ?"
    row = dao.get_one_row_dict(sql, [args.sku])
    dao.db.close()
    if not row:
        print("Not found", file=sys.stderr)
        sys.exit(1)
    for k, v in sorted(row.items()):
        print(f"  {k}: {v}")


def cmd_product_list(args):
    """List products (SKU, Id) with optional limit."""
    from pynop.db import AutoDao
    from pynop.nop_sql import NopQuery
    conn = _ensure_config()
    dao = AutoDao(conn)
    rows, cols = dao.get_rows_and_keys(
        "SELECT Id, Sku, Name FROM Product ORDER BY Id",
        count=args.limit or 0
    )
    dao.db.close()
    for row in rows:
        d = dict(zip(cols, row))
        print(d.get("Id"), d.get("Sku"), d.get("Name", "")[:50])


def main():
    print('Hello World')
    parser = argparse.ArgumentParser(prog="nopcommerce", description="NopCommerce DB CLI")
    sub = parser.add_subparsers(dest="command", help="Command")

    p_ping = sub.add_parser("ping", help="Test connection")
    p_ping.set_defaults(func=cmd_ping)

    p_product = sub.add_parser("product", help="Product commands")
    p_product_sub = p_product.add_subparsers(dest="subcommand")
    p_get = p_product_sub.add_parser("get-by-sku", help="Get product by SKU")
    p_get.add_argument("sku", help="Product SKU")
    p_get.set_defaults(func=cmd_product_get_by_sku)
    p_list = p_product_sub.add_parser("list", help="List products")
    p_list.add_argument("--limit", type=int, default=0, help="Max rows (0 = all)")
    p_list.set_defaults(func=cmd_product_list)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    if args.command == "product" and not getattr(args, "subcommand", None):
        p_product.print_help()
        return
    func = getattr(args, "func", None)
    if func:
        func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
