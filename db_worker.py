import sqlite3


class DbWorker:

    def __init__(self):
        self.__con = sqlite3.connect('')
        self.__cur = self.__con.cursor()

    def execute_query(self, query: str):
        result = self.__cur.execute(query).fetchall()
        self.__con.commit()
        if not result: result = None
        return result

    def get_all_tables(self):
        self.__cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self.__cur.fetchall()

    def show_table(self, table):
        try:
            self.__cur.execute("SELECT * FROM '%s'" %(table))
        except Exception:
            return []
        return self.__cur.fetchall()

    def get_column_names(self, table):
        self.__cur.execute("PRAGMA table_info('%s');" %(table))
        return self.__cur.fetchall()

    @property
    def con(self):
        return self.__con

    @con.setter
    def con(self, db):
        self.__con = sqlite3.connect(db)
        self.__cur = self.__con.cursor()
        print(db)
