import sqlite3 as sql


def dict_factory(cursor, row):
    """ Produces a dictionary from sqlite results. """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def search_database(name):
    conn = sql.connect("db.db")
    conn.row_factory = dict_factory
    curs = conn.cursor()
    curs.execute("SELECT * FROM spat WHERE full_name LIKE ?",
                 ("%" + name + "%",))
    return curs.fetchall()
