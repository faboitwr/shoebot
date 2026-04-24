# ClimbShoeBot
ClimbShoeBot is designed to update the user to important changes to climbing shoe availability or prices in the web shoe store of a climbing gym. This is just to shoe the code, climbing gym website has been redacted for privacy.

## Systems Overview
A webscraper will be made to recheck the shop page every day. The bot takes note of the shoes that have gone out of stock, gone on sale, or are new items and can then alert the user via an email/Telegram/Discord message.

## Specifications & Features
- "shoebase_init.py", uses sqlite3
  - "init_func()" to create the SQLite3 database "shoebase.db"
  - Calls "scrape_init()"
  - Calls "ins_func()"
- "scrapers.py", uses requests and BeautifulSoup
  - "scrape_init()" to obtain the initial dataset to be uploaded into "shoebase.db"
  - "scrape_daily()" to obtain the daily dataset and break it into 4 usable lists
    - Calls "present_check()"
    - Calls "quicksort()"
- "dbhelper.py", uses sqlite3
  - "ins_func()" to insert details into the database
  - "present_check()" to check if a shoe is already in the database
  - "db_get()" to get shoes based on whether they are out of stock or on sale from the database
  - "update(): to update a shoe's details based on the daily dataset
- "additionalfunc.py"
  - "quicksort()" to sort arrays
  - "binary_s()" a binary search to find items from the scraped list
  - "symm_difference()" find items that need to be updated
  - "stock_update()" update a shoe's stock detail
    - Calls "update()"
  - "sale_update()" update a shoe's sale details
    - Calls "update()"
- "app.py"
- "app_run()"
  - Updates all changed items and informs user on shoes currently out of stock or on sale, and also new entries into the system
    - Calls "scrape_daily()"
    - Calls "ins_func()", "db_get()"
    - Calls "symm_difference()", "stock_update()", "sale_update()"
