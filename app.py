#final program, consolidate all functions

from scrapers import scrape_daily
from dbhelper import ins_func, db_get
from additionalfunc import symm_difference, stock_update, sale_update

#app code
def app_run():
    #1: grab all needed lists through a daily scrape
    out_oSt, on_Sl, new_Sh, full_lst = scrape_daily()[0], scrape_daily()[1], scrape_daily()[2], scrape_daily()[3]

    #2: check for new shoes
    #if no new shoes -> skip
    if new_Sh == []:
        print("No new shoes.")
    #if new shoes -> add to db
    else:
        for new_shoe in new_Sh:
            ins_func(new_shoe)
        print("New shoes added.")

    #3: finding the symmetric difference between record and today
    #create lists of recorded out-of-stocks
    db_noSt = db_get("Stock", 0, "shoebase.db")
    db_onSL = db_get("Sale", 1, "shoebase.db")

    stock_change = symm_difference(out_oSt, db_noSt)
    sale_change = symm_difference(on_Sl, db_onSL)

    stock_update(stock_change, "debugcopy.db")
    sale_update(sale_change, full_lst, "debugcopy.db")

    outoS = ""
    onSl = ""
    new = ""

    for shoe in out_oSt:
        outoS += shoe[0] + "\n"
    
    for shoe in on_Sl:
        onSl += f"{shoe[0]}, ${shoe[1]}" + "\n"
    
    for shoe in new_Sh:
        new += f"{shoe[0]}, ${shoe[1]}" + "\n"

    output = f"""
Shoe(s) out of stock are:
{outoS}
Shoe(s) on sale are: 
{onSl}
New shoe(s) are:
{new}
"""
    
    print(output)

    return output

app_run()

run = True
while run == True:
    brk = input("Input anything to break: ")
    if brk != None:
        run = False