

# noinspection PyUnusedLocal
# skus = unicode string
import math

price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

discount_table = {
    "A": {
        5: 200,
        3: 130,
    },
    "B": {
        2: 45,
    }
}


def calculate_discounted_price(item, quantity):
    discounted_price_total = 0
    quantity_counter = quantity

    for q, discounted_price in discount_table[item].items():    
        remainder_q = quantity_counter % q
        discounted_q = math.floor(quantity_counter / q)
        discounted_price_total += discounted_q * discounted_price
        quantity_counter = remainder_q

    return discounted_price_total, quantity_counter


def checkout(skus):
    if len(skus) == 0:
        return 0

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
        
        quantity_remaining = quantity

        if item in discount_table:
            discounted_price, quantity_remaining = calculate_discounted_price(item, quantity)
            total_checkout_value += discounted_price
        
        total_checkout_value += quantity_remaining * price_table[item]

    return total_checkout_value








