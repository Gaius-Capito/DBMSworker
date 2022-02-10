import sqlite3
import psycopg2
from tkinter import messagebox as mbox
from abc import ABC, abstractmethod
from config import host_name, user_name, password, db_name


class DbWorker(ABC):

    @abstractmethod
    def execute_query(self, query: str):
        pass

    @abstractmethod
    def execute_select_query(self, select_query: str):
        pass

    @abstractmethod
    def get_all_tables(self):
        pass

    @abstractmethod
    def show_table(self, table):
        pass

    @abstractmethod
    def get_column_names(self):
        pass


class SQLiteWorker(DbWorker):

    def __init__(self):
        self.__con = sqlite3.connect('')
        self.__cur = self.__con.cursor()

    def execute_query(self, query: str):
        result = self.__cur.execute(query).fetchall()
        self.__con.commit()
        if not result: result = None
        return result

    def execute_select_query(self, select_query: str):
        self.__cur.execute("""%s""" % select_query)
        return self.__cur.fetchall()

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


class PostgreSQL():

    def __init__(self, user_name=user_name, password=password, host_name=host_name, db_name=db_name):
        try:
            self.con = psycopg2.connect(database=db_name, user=user_name, password=password, host=host_name,
                                        port="5432")
            self.cur = self.con.cursor()
            mbox.showinfo('', "Connection to PostgreSQL DB successful")
        except Exception as e:
            mbox.showerror('', f"The error '{e}' occurred")

    def execute_query(self, query: str):
        self.cur.execute("""%s""" % query)
        self.con.commit()

    def get_all_tables(self):
        self.cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public'""")
        return self.cur.fetchall()

    def get_column_names(self):
        self.cur.execute("SELECT * FROM users LIMIT 0")
        return self.cur.description

    def get_sql_select(self, select_request: str):
        self.cur.execute("""%s""" % select_request)
        return self.cur.fetchall()


if __name__ == '__main__':
    print(PostgreSQL().get_all_tables())