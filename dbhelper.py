#db helper functions

import sqlite3

#getter function
def db_get(salestock, blean):
    conn = sqlite3.connect("shoebase.db")
    
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
def update(item, value, new_val):
    conn = sqlite3.connect("shoebase.db")
    
    curs = conn.cursor()

    curs.execute(f"""
                UPDATE "Spending"
                SET {value} = '{new_val}'
                WHERE "ShoeN" = ?
                 """, (item, ))

    conn.commit()
    conn.close()