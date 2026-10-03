def cart_size(total_price):
    total = 0
    
    for total_calculate in total_price:
        total = total + total_calculate

    return total

total_price = [100, 250, 399]
total = cart_size(total_price)
print(total)