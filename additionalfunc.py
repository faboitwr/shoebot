#additional functions

from dbhelper import update

#quicksort to sort shoe naming alphabetically
def quicksort(lst):
    #base case
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        lower_alph = []
        higher_alph = []
        for i in range(1, len(lst)):
            if lst[i] <= pivot:
                lower_alph.append(lst[i])
            else:
                higher_alph.append(lst[i])
        return quicksort(lower_alph) + [pivot] + quicksort(higher_alph)

#to efficiently find shoe details from sorted list
def binary_s(lst, item):
    def binary_s_sub(lst, item, low, high):
        #midpoint
        midpoint = (low + high) // 2
        if low > high:
            return -1
        elif lst[midpoint][0] == item:
            return midpoint
        elif item > lst[midpoint][0]:
            return binary_s_sub(lst, item, midpoint + 1, high)
        else:
            return binary_s_sub(lst,item, low, midpoint - 1)
    return binary_s_sub(lst, item, 0, len(lst) - 1)

#find the symmetric difference between 2 lists
def symm_difference(rec, upd):
    symDiff = set(i[0] for i in rec) ^ set(i[0] for i in upd)
    #first array to signal from on sale/out of stock -> off sale/in stock
    #second array to signal from off sale/in stock -> on sale/out of stock
    return [[i for i in rec if i[0] in symDiff], [i for i in upd if i[0] in symDiff]]

#stock updater
def stock_update(lst, db):
    #split into stocked & going out of stock
    out_to_in = lst[0]
    in_to_out = lst[1]

    for inS in out_to_in:
        print(inS[0])
        update(inS[0], "Stock", 1, db)

    for outS in in_to_out:
        print(outS[0])
        update(outS[0], "Stock", 0, db)

#sale updater
def sale_update(lst, ref_list, db):
    #split into from sale->retail & retail->sale
    sale_to_ret = lst[0]
    ret_to_sale = lst[1]

    for ret in sale_to_ret:
        print(ret[0])
        indx = binary_s(ref_list, ret[0])
        update(ret[0], "ShoeP", ref_list[indx][1], db)
        update(ret[0], "Sale", 0, db)
        
    for sale in ret_to_sale:
        print(sale[0], sale[1])
        update(sale[0], "ShoeP", sale[1], db)
        update(sale[0], "Sale", 1, db)