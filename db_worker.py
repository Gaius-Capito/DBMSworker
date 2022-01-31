import sqlite3


class DbWorker:

    def __init__(self):
        self.__con = sqlite3.connect('/home/capito/Projects/vkbot/concerts.db')
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
        print(table)
        self.__cur.execute("SELECT * FROM '%s'" %(table))
        return self.__cur.fetchall()

    def get_column_names(self):
        self.__cur.execute("PRAGMA table_info(concerts);")
        return self.__cur.fetchall()




