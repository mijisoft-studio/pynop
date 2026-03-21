import pyodbc
from pymongo import MongoClient
from .config import *
from .settings.db import DB_CONFIG


class DB:
    _conn = None
    _cursor = None

    def __init__(self, db_engine, db_server, db_name, db_username, db_password):
        if db_engine == "MONGO":
            self._conn = MongoClient(PYMONGO_CONNECTION_STRING.format(server=db_server))
            self._cursor = self._conn[db_name]
        else:
            conn_str = ""

            if db_engine == "MSSQL":
                conn_str = PYODBC_MSSQL_CONNECTION_STRING % (
                    db_server,
                    db_name,
                    db_username,
                    db_password,
                )
            elif db_engine == "MYSQL":
                conn_str = PYODBC_MYSQL_CONNECTION_STRING % (
                    db_server,
                    db_name,
                    db_username,
                    db_password,
                )
            elif db_engine == "DSN":
                conn_str = db_server

            self._conn = pyodbc.connect(conn_str)
            self._cursor = self._conn.cursor()

        return


class AutoDao:
    def __init__(self, db_type="", db_engine="", db_server="", db_name="", db_username="", db_password=""):
        env = DB_CONFIG["env"]

        if db_type and db_type in DB_CONFIG[env].keys():
            self.db = DB(
                DB_CONFIG[env][db_type]["db_engine"],
                DB_CONFIG[env][db_type]["db_server"],
                DB_CONFIG[env][db_type]["db_name"],
                DB_CONFIG[env][db_type]["db_username"],
                DB_CONFIG[env][db_type]["db_password"],
            )
        else:
            self.db = DB(db_type, db_server, db_name, db_username, db_password)

    def get_hashmap(self, sql, param=[]):
        result = {}
        self.db._cursor.execute(sql, param)
        for a in self.db._cursor.fetchall():
            result[a[0]] = a[1]
        return result

    def get_hashtable(self, sql, param=[], key=0):
        result = {}
        self.db._cursor.execute(sql, param)
        result_rows = self.db._cursor.fetchall()
        if result_rows:
            result_cols = [column[0] for column in self.db._cursor.description]
            for row in result_rows:
                result[row[key]] = dict(zip(result_cols, row))
        return result

    def get_hasharrtable(self, sql, param=[], key=0):
        result = {}
        self.db._cursor.execute(sql, param)
        result_rows = self.db._cursor.fetchall()
        if result_rows:
            result_cols = [column[0] for column in self.db._cursor.description]
            for row in result_rows:
                row_key = row[key]
                if row_key not in result:
                    result[row_key] = []
                result[row_key].append(dict(zip(result_cols, row)))
        return result

    def get_rows_and_keys(self, sql, param=[], count=0):
        self.db._cursor.execute(sql, param)
        if count:
            result = self.db._cursor.fetchmany(count)
        else:
            result = self.db._cursor.fetchall()

        result_cols = [column[0] for column in self.db._cursor.description]
        return result, result_cols

    def get_one_row_dict(self, sql, param=[]):
        self.db._cursor.execute(sql, param)
        result = self.db._cursor.fetchone()
        if result:
            result_cols = [column[0] for column in self.db._cursor.description]
            result = dict(zip(result_cols, result))
        return result

    def get_one_col_list(self, sql, param=[], count=0):
        self.db._cursor.execute(sql, param)
        result = []
        if count:
            result = self.db._cursor.fetchmany(count)
        else:
            result = self.db._cursor.fetchall()
        return [row[0] for row in result]

    def get_one_value(self, sql, param=[]):
        self.db._cursor.execute(sql, param)
        result = self.db._cursor.fetchone()
        if result:
            result = result[0]
        return result

    def get_list(self, sql, param=[]):
        result = []
        self.db._cursor.execute(sql, param)
        result_rows = self.db._cursor.fetchall()
        if result_rows:
            result_cols = [column[0] for column in self.db._cursor.description]
            for row in result_rows:
                result.append(dict(zip(result_cols, row)))
        return result

    def update(self, sql, param=[]):
        self.db._cursor.execute(sql, param)
        self.db._cursor.commit()
        return True

    def update_return_rowcount(self, sql, param=[]):
        self.db._cursor.execute(sql, param)
        n = self.db._cursor.rowcount
        self.db._cursor.commit()
        return n

    def update_r_dict(self, sql, param=[]):
        self.db._cursor.execute(sql, param)
        result = self.db._cursor.fetchone()
        if result:
            result_cols = [column[0] for column in self.db._cursor.description]
            result = dict(zip(result_cols, result))
        self.db._cursor.commit()
        return result

    def update_r_list(self, sql, param=[]):
        self.db._cursor.execute(sql, param)
        result = self.db._cursor.fetchall()
        result_cols = [column[0] for column in self.db._cursor.description]
        self.db._cursor.commit()
        return result, result_cols


class Query:
    pass

