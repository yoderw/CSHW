price_dollars = int(input("Price dollars? "))
price_cents = int(input("Price cents? "))
tip_percentage = int(input("Tip percentage [0-100]? "))

float_price = (price_dollars + (price_cents / 100))
float_tip = (float_price * tip_percentage) / 100

print(float_tip)
