def calculate_price(price, discount=0):
    return price - price * discount / 100


print(calculate_price(1000))
print(calculate_price(1000, 20))
