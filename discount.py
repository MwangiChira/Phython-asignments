def calculate_discount(price, discount_percent):
    Args:
price (float): Original price.
discount_percent (float): Discount percentage.
Returns:
float: Final price after applying the discount.
if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price
def calculate_discount(price, discount_percent):
    Calculates the final price after applying a discount.
    Args:
    price (float): Original price.
    discount_percent (float): Discount percentage.
    Returns:
    float: Final price after applying the discount.
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount_percent)
if final_price == original_price:
    print(f"The final price without any discount is ${final_price:.2f}")
else:
    print(f"The final price after applying the discount is ${final_price:.2f}")