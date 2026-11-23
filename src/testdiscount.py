def calculate_price(price, customer_type):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if customer_type not in ("VIP", "STANDARD"):
        raise ValueError("Invalid customer type")

    if customer_type == "GOLD":
        return round(price * 0.90, 2)

 

    return price
