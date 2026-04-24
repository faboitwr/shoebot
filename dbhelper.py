#db helper functions

import sqlite3

#inserter function
def ins_func(s_det):
    #assume s_det takes format of (date 0, vendid 1, vendname 2, spendid 3, cost 4, comments 5, class 6)
    conn = sqlite3.connect("shoebase.db")
    
    print(s_det)

    curs = conn.cursor()

    #insert spending data into the 2 tables established via initiation.py
    curs.execute("INSERT INTO 'ShoeD'('ShoeID', 'ShoeN', 'ShoeP', 'Stock', 'Sale') VALUES(?, ?, ?, ?, ?)", (None, s_det[0], s_det[1], s_det[2], s_det[3], ))

    conn.commit()
    conn.close()

#check if present
def present_check(db, shoeN):
    conn = sqlite3.connect(db)
    
    curs = conn.cursor()
    
    curs.execute(f"""
        SELECT "ShoeN", "ShoeP", "Stock", "Sale" FROM "ShoeD"
        WHERE ShoeN = ?
                """, (shoeN,))

    shoe_pres = curs.fetchone()

    conn.commit()
    conn.close()

    return shoe_pres

#getter function
def db_get(salestock, blean, db):
    conn = sqlite3.connect(db)
    
    curs = conn.cursor()
    
    curs.execute(f"""
        SELECT "ShoeN", "ShoeP", "Stock", "Sale" FROM "ShoeD"
        WHERE {salestock} = ?
                """, (blean, ))

    lst_unstock = curs.fetchall()

    conn.commit()
    conn.close()

    return lst_unstock

#updater
def update(item, value, new_val, db):
    conn = sqlite3.connect(db)
    
    curs = conn.cursor()

    curs.execute(f"""
                UPDATE "ShoeD"
                SET {value} = '{new_val}'
                WHERE "ShoeN" = ?
                 """, (item, ))

    conn.commit()
    conn.close()