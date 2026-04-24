#scraper functions

import requests
from bs4 import BeautifulSoup

#initial scrape to generate database
def scrape_init():
    #counter to parse through each page
    page_num = 1
    
    #temp data
    complete = False
    temp_l = []

    #connect to website
    while complete is False:
        ref_site = f"https://shop.boulderplanet.sg/collections/climbing-shoes/climbing-shoes?page={page_num}"
        response = requests.get(ref_site)

        #make response usable
        txt = response.text
        cont = response.content
        
        #cleaning via BeautifulSoup
        tidied = BeautifulSoup(cont, "html.parser")
        
        shoe_list = tidied.find()

        shoe_cards = shoe_list.find_all("product-card")

        #check if there are more pages to parse
        
        #case 1: no more pages
        if len(shoe_cards) == 0:
            complete = True
        
        #case 2: more pages to parse
        else:
            for shoe in shoe_cards:
                #default assume in stock
                stock = 1
                sale = 0

                #obtain shoe name
                shoe_n = shoe.select_one("span.product-card__title").get_text(strip = True)

                #check if shoe is on sale, obtain either retail or sale price
                if shoe.select_one("sale-price.text-subdued") == None:
                    shoe_p = float(shoe.select_one("sale-price.text-on-sale").get_text(strip = True)[11:-4])
                else:
                    shoe_p = float(shoe.select_one("sale-price.text-subdued").get_text(strip = True)[11:-4])
                
                #check if shoe is out of stock/on sale
                prod_listing = shoe.select_one("div.product-card__badge-list")

                if prod_listing is not None and prod_listing.get_text(strip = True) == "Sold out":
                    stock = 0

                elif prod_listing is not None and prod_listing.get_text(strip = True)[0:4] == "Save":
                    sale = 1

                temp_l.append((shoe_n, shoe_p, stock, sale))   

            page_num += 1
    
    return temp_l

#daily scrape to parse

from dbhelper import present_check
from additionalfunc import quicksort

#daily scrape to parse
def scrape_daily():
    #counter to parse through each page
    page_num = 1
    
    #temp data
    complete = False

    temp_stock = []
    temp_sale = []
    temp_new = []

    temp_l = []

    #connect to website
    while complete is False:
        ref_site = f"https://shop.boulderplanet.sg/collections/climbing-shoes/climbing-shoes?page={page_num}"
        response = requests.get(ref_site)

        #make response usable
        txt = response.text
        cont = response.content
        
        #cleaning via BeautifulSoup
        tidied = BeautifulSoup(cont, "html.parser")
        
        shoe_list = tidied.find()

        shoe_cards = shoe_list.find_all("product-card")

        #check if there are more pages to parse
        
        #case 1: no more pages
        if len(shoe_cards) == 0:
            complete = True
        
        #case 2: more pages to parse
        else:
            for shoe in shoe_cards:
                #default assume in stock
                stock = 1
                sale = 0

                #obtain shoe name
                shoe_n = shoe.select_one("span.product-card__title").get_text(strip = True)

                presence = present_check("shoebase.db", shoe_n)

                #check if shoe is on sale, obtain either retail or sale price
                if shoe.select_one("sale-price.text-subdued") == None:
                    shoe_p = float(shoe.select_one("sale-price.text-on-sale").get_text(strip = True)[11:-4])
                else:
                    shoe_p = float(shoe.select_one("sale-price.text-subdued").get_text(strip = True)[11:-4])
                
                #check if shoe is out of stock/on sale
                prod_listing = shoe.select_one("div.product-card__badge-list")

                if prod_listing is not None and prod_listing.get_text(strip = True) == "Sold out":
                    stock = 0
                    temp_stock.append((shoe_n, shoe_p, stock, sale))

                elif prod_listing is not None and prod_listing.get_text(strip = True)[0:4] == "Save":
                    sale = 1
                    temp_sale.append((shoe_n, shoe_p, stock, sale))

                if presence == None:
                    temp_new.append((shoe_n, shoe_p, stock, sale)) 
                
                temp_l.append((shoe_n, shoe_p, stock, sale)) 

            page_num += 1
    
    return (temp_stock, temp_sale, temp_new, quicksort(temp_l))