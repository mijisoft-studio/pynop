"""
MSSQL DB access via pyodbc. No dependency on settings or sync project.
"""
import pyodbc
from typing import Any, List, Optional

from pynop.config import get_connection_string


class DB:
    """Single MSSQL connection (pyodbc)."""

    _conn: Optional[pyodbc.Connection] = None
    _cursor: Optional[pyodbc.Cursor] = None

    def __init__(
        self,
        connection_dict: Optional[dict[str, Any]] = None,
        *,
        db_server: str = "",
        db_name: str = "",
        db_username: str = "",
        db_password: str = "",
    ):
        if connection_dict is not None:
            conn_str = get_connection_string(connection_dict)
            print(conn_str)
        else:
            print('Using default connection parameters:')
            from pynop.config import PYODBC_MSSQL_CONNECTION_STRING, PYODBC_MSSQL_DRIVER
            conn_str = PYODBC_MSSQL_CONNECTION_STRING.format(
                driver=PYODBC_MSSQL_DRIVER,
                server=db_server,
                database=db_name,
                username=db_username,
                password=db_password,
            )
        self._conn = pyodbc.connect(conn_str)
        self._cursor = self._conn.cursor()

    def close(self) -> None:
        if self._cursor:
            self._cursor.close()
            self._cursor = None
        if self._conn:
            self._conn.close()
            self._conn = None


class AutoDao:
    """
    DAO that uses a single DB connection. Pass a connection dict (from config or env).
    Used by NopTool and by the sync project (sync passes DB_CONFIG[env]['nop'] etc.).
    """

    def __init__(
        self,
        connection_dict: Optional[dict[str, Any]] = None,
        *,
        db_engine: str = "MSSQL",
        db_server: str = "",
        db_name: str = "",
        db_username: str = "",
        db_password: str = "",
    ):
        if connection_dict is not None:
            self.db = DB(connection_dict=connection_dict)
        else:
            self.db = DB(
                db_server=db_server,
                db_name=db_name,
                db_username=db_username,
                db_password=db_password,
            )

    def get_hashmap(self, sql: str, param: Optional[List[Any]] = None) -> dict:
        param = param or []
        result = {}
        self.db._cursor.execute(sql, param)
        for row in self.db._cursor.fetchall():
            result[row[0]] = row[1]
        return result

    def get_hashtable(self, sql: str, param: Optional[List[Any]] = None, key: int = 0) -> dict:
        param = param or []
        result = {}
        self.db._cursor.execute(sql, param)
        rows = self.db._cursor.fetchall()
        if rows:
            cols = [c[0] for c in self.db._cursor.description]
            for row in rows:
                result[row[key]] = dict(zip(cols, row))
        return result

    def get_hasharrtable(self, sql: str, param: Optional[List[Any]] = None, key: int = 0) -> dict:
        param = param or []
        result = {}
        self.db._cursor.execute(sql, param)
        rows = self.db._cursor.fetchall()
        if rows:
            cols = [c[0] for c in self.db._cursor.description]
            for row in rows:
                k = row[key]
                if k not in result:
                    result[k] = []
                result[k].append(dict(zip(cols, row)))
        return result

    def get_rows_and_keys(
        self, sql: str, param: Optional[List[Any]] = None, count: int = 0
    ) -> tuple:
        param = param or []
        self.db._cursor.execute(sql, param)
        rows = self.db._cursor.fetchmany(count) if count else self.db._cursor.fetchall()
        cols = [c[0] for c in self.db._cursor.description]
        return rows, cols

    def get_one_row_dict(self, sql: str, param: Optional[List[Any]] = None) -> Optional[dict]:
        param = param if isinstance(param, list) else ([param] if param is not None else [])
        self.db._cursor.execute(sql, param)
        row = self.db._cursor.fetchone()
        if row:
            cols = [c[0] for c in self.db._cursor.description]
            return dict(zip(cols, row))
        return None

    def get_one_col_list(
        self, sql: str, param: Optional[List[Any]] = None, count: int = 0
    ) -> List[Any]:
        param = param or []
        self.db._cursor.execute(sql, param)
        rows = self.db._cursor.fetchmany(count) if count else self.db._cursor.fetchall()
        return [r[0] for r in rows]

    def get_one_value(self, sql: str, param: Optional[List[Any]] = None) -> Any:
        param = param or []
        self.db._cursor.execute(sql, param)
        row = self.db._cursor.fetchone()
        return row[0] if row else None

    def get_list(self, sql: str, param: Optional[List[Any]] = None) -> List[dict]:
        param = param or []
        self.db._cursor.execute(sql, param)
        rows = self.db._cursor.fetchall()
        if not rows:
            return []
        cols = [c[0] for c in self.db._cursor.description]
        return [dict(zip(cols, row)) for row in rows]

    def update(self, sql: str, param: Optional[List[Any]] = None) -> bool:
        param = param or []
        self.db._cursor.execute(sql, param)
        self.db._cursor.commit()
        return True

    def update_return_rowcount(self, sql: str, param: Optional[List[Any]] = None) -> int:
        param = param or []
        self.db._cursor.execute(sql, param)
        n = self.db._cursor.rowcount
        self.db._cursor.commit()
        return n

    def update_r_dict(self, sql: str, param: Optional[List[Any]] = None) -> Optional[dict]:
        param = param or []
        self.db._cursor.execute(sql, param)
        row = self.db._cursor.fetchone()
        self.db._cursor.commit()
        if row:
            cols = [c[0] for c in self.db._cursor.description]
            return dict(zip(cols, row))
        return None

    def update_r_list(
        self, sql: str, param: Optional[List[Any]] = None
    ) -> tuple:
        param = param or []
        self.db._cursor.execute(sql, param)
        rows = self.db._cursor.fetchall()
        cols = [c[0] for c in self.db._cursor.description]
        self.db._cursor.commit()
        return rows, cols


class Query:
    """Base for SQL query containers (e.g. NopQuery)."""
    pass
