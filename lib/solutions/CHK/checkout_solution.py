

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

free_offer_table = {
    "E": {
        2: {
            "B": 2
        }
    }
}


def calculate_discounted_price(item, quantity):
    discounted_price_total = 0
    quantity_remaining = quantity

    for q, discounted_price in discount_table[item].items():    
        discounted_q = math.floor(quantity_remaining / q)
        discounted_price_total += discounted_q * discounted_price
        quantity_remaining = quantity_remaining % q

    return discounted_price_total, quantity_remaining


def calculate_free_offers(item, quantity, basket):
    discount_total = 0
    quantity_remaining = quantity

    for q, free_items in free_offer_table[item].items():
        free_q = math.floor(quantity_remaining / q)
        

    return 0


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
    
    for item, quantity in basket.items():
        if item not in price_table:
            return -1
        
        quantity_remaining = quantity

        if item in discount_table:
            discounted_price, quantity_remaining = calculate_discounted_price(item, quantity)
            total_checkout_value += discounted_price
        
        total_checkout_value += quantity_remaining * price_table[item]

        if item in free_offer_table:
            discount_to_apply = calculate_free_offers(item, quantity, basket)
            total_checkout_value -= discount_to_apply

    return total_checkout_value


