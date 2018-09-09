import json
import sqlite3 as sql

conn = sql.connect("db.db")
curs = conn.cursor()

curs.execute("""
    CREATE TABLE IF NOT EXISTS spat_subjects (
        sub_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_1 TEXT,
        subject_2 TEXT,
        subject_3 TEXT,
        subject_4 TEXT,
        subject_5 TEXT
    )
""")
curs.execute("""
    CREATE TABLE IF NOT EXISTS spat (
        pid INTEGER PRIMARY KEY,
        image_title TEXT,
        temporal TEXT,
        image_caption TEXT,
        full_name_serv_name TEXT,
        full_name TEXT,
        naa_ident TEXT,
        embark_ship TEXT,
        embark_date TEXT,
        provenance TEXT,
        img_num TEXT,
        source TEXT,
        subjects INTEGER,
        perm_image_link TEXT,
        image_url TEXT,
        FOREIGN KEY(subjects) REFERENCES spat_subjects(sub_id)
    )
""")
conn.commit()

filedata = open("outputs/soldier_portraits_australasian_traveller.json").read()
spat_data = json.loads(filedata)

for obj in spat_data:
    curs.execute("""
        INSERT INTO spat_subjects(
            subject_1,
            subject_2,
            subject_3,
            subject_4,
            subject_5
        ) VALUES (?,?,?,?,?)
    """, tuple(obj["default"]["subjects"]))
    curs.execute("""
        INSERT INTO spat VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        obj["default"]["pid"],
        obj["default"]["image_title"],
        obj["default"]["temporal"],
        obj["default"]["image_caption"],
        obj["default"]["full_name_serv_num"],
        obj["default"]["full_name"],
        obj["default"]["naa_ident"],
        obj["default"]["embark_ship"],
        obj["default"]["embark_date"],
        obj["default"]["provenance"],
        obj["default"]["img_num"],
        obj["default"]["source"],
        curs.lastrowid,
        obj["default"]["perm_image_link"],
        obj["extra"]["image_url"]
    ))

conn.commit()
