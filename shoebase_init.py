#database initialiser

import sqlite3

from dbhelper import ins_func
from scrapers import scrape_init

#database creation
def init_func():
    conn = sqlite3.connect("shoebase.db")
    conn.execute("""
    CREATE TABLE "ShoeD" (
        "ShoeID" INTEGER NOT NULL,
        "ShoeN"	TEXT NOT NULL,
        "ShoeP"	REAL NOT NULL,
        "Stock" BOOL NOT NULL,
        "Sale" BOOL NOT NULL,
        PRIMARY KEY("ShoeID" AUTOINCREMENT)
    );
                """)

    conn.commit()
    conn.close()

#first upload of data to database

init_func()
for i in scrape_init():
    ins_func(i)