def calculate_total(cart):
    for item, price in cart.items():
        if price > 50000:
            discount_amount = price * 5 / 100
            cart[item] = price - discount_amount
        if 10000<price<25000:
            discount_amount=price*2/100
            cart[item]=price-discount_amount
            
    total = sum(cart.values())
    if total > 20000 and total <= 50000:
        discount_amount = total * 10 / 100
        total = total - discount_amount
        return total
    elif total > 50000:
        discount_amount = total * 15 / 100
        total = total - discount_amount
        return total
    else:
        return total
cart = {'laptop': 50000, 'mouse': 9000, 'keyboard': 60000}
print(calculate_total(cart))
