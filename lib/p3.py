import math

def total_flour(large_thick, large_thin, medium_thick, medium_thin):
    '''
    This function will calculate total flour needed for the orders
    :param large_thick: a number (int)
    :param large_thin: a number (int)
    :param medium_thick: a number (int)
    :param medium_thin: a number (int)
    :return: amount of flour (int)
    '''
    flour_needed = (0.550 * large_thick + 0.5 * large_thin + 0.45 * medium_thick + 0.4 * medium_thin) * 1.06
    result = math.ceil((float(flour_needed)))
    if result % 2 == 1:
        result += 1
    return result

def shop_A(a,b,c,d):
    '''
    This function will calculate how much money do we have to pay if we buy from shop A
    :param a: a number (int)
    :param b: a number (int)
    :param c: a number (int)
    :param d: a number (int)
    :return: money needed to pay for the flour in shop A (int)
    '''
    priceA = total_flour(a,b,c,d) * 30000
    if total_flour(a,b,c,d) < 30:
        priceA = priceA - (priceA * 0.03)
    else:
        priceA = priceA - (priceA * 0.05)
    return int(priceA)

def shop_B(a,b,c,d):
    '''
    This function wil calculate how much money do we have to pay if we buy from shop B
    :param a: a number (int)
    :param b: a number (int)
    :param c: a number (int)
    :param d: a number (int)
    :return: money needed to pay for the flour in shop B (int)
    '''
    priceB = total_flour(a,b,c,d) * 31000
    if total_flour(a,b,c,d) < 40:
        priceB = priceB - (priceB * 0.05)
    else:
        priceB = priceB - (priceB * 0.1)
    return int(priceB)

def flour_order(large_thick, large_thin, medium_thick, medium_thin):
    '''
    This function will calculate how many kg of flour needed to order and determine which store should we order from
    :param large_thick: a number (int)
    :param large_thin: a number (int)
    :param medium_thick: a number (int)
    :param medium_thin: a number (int)
    :return: result (list)
    '''
    costA = shop_A(large_thick, large_thin, medium_thick, medium_thin)
    costB = shop_B(large_thick, large_thin, medium_thick, medium_thin)
    if costA > costB:
        print("We choose provider B")
    elif costA == costB:
        print("We choose provider A because he more friendly")
    else:
        print("We choose provider A")
    return "\nWe need to order: " + str(total_flour(large_thick, large_thin, medium_thick, medium_thin)) + "KG of flour, which cost " + str(costA) + " VND if we buy form A and " + str(costB) + " VND if we buy from B"



def flour_order_2(large_thick, large_thin, medium_thick, medium_thin):
    total_flour = math.ceil((0.55 * large_thick) + (0.5 * large_thin) +  (0.45 * medium_thick) + (0.4* medium_thin))

    if total_flour % 2 == 1:
        total_flour = total_flour + 1

    shop_a_price = 30000
    shop_b_price = 31000

    cost_a = 0
    cost_b = 0
    # Shop A - Calculation
    if total_flour >= 30:
        cost_a = total_flour * shop_a_price * 0.95
    else:
        cost_a = total_flour * shop_a_price * 0.97

    # Shop B - Calculation
    if total_flour >= 40:
        cost_b = total_flour * shop_b_price * 0.9
    else:
        cost_b = total_flour * shop_b_price * 0.95

    print "We need to order %dkg of flour, which costs %fVND if we buy from A and %fVND if we buy from B."%(total_flour, cost_a, cost_b)

    selected_provider = ""
    total_cost = 0
    if cost_a <= cost_b:
        selected_provider = "A"
        total_cost = cost_a
    else:
        selected_provider = "B"
        total_cost = cost_b

    return total_flour, selected_provider, total_cost
