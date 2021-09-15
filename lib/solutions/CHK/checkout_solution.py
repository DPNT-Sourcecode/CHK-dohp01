

# noinspection PyUnusedLocal
# skus = unicode string
import math

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


def calculate_discounted_price(item, quantity):
    discounted_price = 0

    for q, discounted_price in discount_table[item]:
        

    non_discounted_quantity = quantity % discount_table[item]
    discounted_quantity = math.floor(quantity % discount_table[item])
    return non_discounted_quantity * price_table[item] + discounted_quantity * discount_table[item]


def checkout(skus):
    if len(skus) == 0:
        return -1

    basket = {}
    total_checkout_value = 0

    for item in skus:
        if item not in basket:
            basket[item] = 1
        else:
            basket[item] += 1

    print(basket)
    
    for item, quantity in basket.items():
        if item not in price_table:
            return -1
        
        if item in discount_table:
            total_checkout_value += calculate_discounted_price(item, quantity)
        else:
            total_checkout_value += quantity * price_table[item]

    return total_checkout_value







