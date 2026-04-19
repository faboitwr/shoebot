import sqlite3

from shoebot import scraper

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
def ins_func(s_det):
    #assume s_det takes format of (date 0, vendid 1, vendname 2, spendid 3, cost 4, comments 5, class 6)
    conn = sqlite3.connect("shoebase.db")
    
    print(s_det)

    curs = conn.cursor()

    #insert spending data into the 2 tables established via initiation.py
    curs.execute("INSERT INTO 'ShoeD'('ShoeID', 'ShoeN', 'ShoeP', 'Stock', 'Sale') VALUES(?, ?, ?, ?, ?)", (None, s_det[0], s_det[1], s_det[2], s_det[3], ))

    conn.commit()
    conn.close()

init_func()
for i in scraper():
    ins_func(i)