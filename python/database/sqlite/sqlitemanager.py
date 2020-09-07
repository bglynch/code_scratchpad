import sqlite3
from sqlite3 import Error


# =========================================
# -------- BUILDING A DATABASE ----------
# =========================================
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def add_column_to_table(connection, table_name, new_column_name, col_type):
    try:
        sql_statement = f"ALTER TABLE {table_name} ADD {new_column_name} {col_type};"
        cur = connection.cursor()
        cur.execute(sql_statement)
    except sqlite3.Error as e:
        print(e, " error creating column")


# =================================================
# -------- INTERACTING WITH A DATABASE-- ----------
# =================================================
def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    print("..sucessful connection to: " + db_file.split("/")[-1])
    return connection


def check_table_for_column(connection, table_name, column_name):
    cur = connection.cursor()
    cur.execute(f"PRAGMA table_info({table_name})")
    list_of_table_columns = [x[1] for x in cur]
    return column_name in list_of_table_columns


def close_connection(connection):
    connection.close()
    print("...connection closed")