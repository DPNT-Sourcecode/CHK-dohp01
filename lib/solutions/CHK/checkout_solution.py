

# noinspection PyUnusedLocal
# skus = unicode string
import math
import copy

price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
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
            "B": 1
        }
    },
    "F": {
        2: {
            "F": 1
        }
    }
}


def calculate_discounted_price(item, quantity):
    """calculates discount to be applied, and remaining quantity of items where discount doesn't apply"""
    discounted_price_total = 0
    quantity_remaining = quantity

    for q, discounted_price in discount_table[item].items():    
        discounted_q = math.floor(quantity_remaining / q)
        discounted_price_total += discounted_q * discounted_price
        quantity_remaining = quantity_remaining % q

    return discounted_price_total, quantity_remaining


def calculate_free_offers(item, quantity, basket):
    """removes discounted items from basket"""

    discounted_price_total = 0
    quantity_remaining = quantity

    for q, free_item_basket in free_offer_table[item].items():
        free_multiples = math.floor(quantity_remaining / q)
        print(free_multiples)
        for free_item, free_quantity in free_item_basket.items():
            if free_item in basket:
                q_to_discount = min(free_quantity * free_multiples, basket[free_item])
                discounted_price_total += q_to_discount * price_table[free_item]
                basket[free_item] -= q_to_discount

    return None


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

    basket_remaining = copy.deepcopy(basket)

    for item, quantity in basket_remaining.items():
        if item in free_offer_table:
            calculate_free_offers(item, quantity, basket_remaining)

    print(basket_remaining)

    for item, quantity in basket_remaining.items():
        quantity_remaining = quantity

        if item in discount_table:
            discounted_price, quantity_remaining = calculate_discounted_price(item, quantity)
            total_checkout_value += discounted_price
        
        total_checkout_value += quantity_remaining * price_table[item]



    return total_checkout_value


