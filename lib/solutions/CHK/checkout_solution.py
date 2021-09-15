

# noinspection PyUnusedLocal
# skus = unicode string

price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

discount_table = {
    "A": {
        3: 130,
    },
    "B": {
        2: 45,
    }
}

def checkout(skus):
    basket = {}
    total_checkout_value = 0

    for item in skus:
        if item not in basket:
            basket[item] = 1
        else:
            basket[item] += 1
    
    for item, quantity in basket:
        if item not in price_table:
            return -1
        
        


