items=["pencil", "eraser", "notebook", "ruler"]
stock=[10, 0, 15, 7]

inventory = dict(zip(items, stock))
print("Full Inventory:", inventory)

in_stock_items = {item: quantity for item, quantity in inventory.items() if quantity > 0}
print("Items in Stock:", in_stock_items)

chosen_items=input("Enter the items you want to buy: ")

if chosen_items not in in_stock_items:
    print(f"Sorry, {chosen_items} is not available in stock.")
    exit()

Original_Prices=[9,10,3,4]
print("Original Prices:", Original_Prices)
markup_price=int(input("Enter the markup price: "))

marked_up_prices = list(map(lambda price: price + markup_price, Original_Prices))
print("Marked Up Prices:", marked_up_prices)

item_index=items.index(chosen_items)
final_price=marked_up_prices[item_index]
print(f"Final Price for {chosen_items}: {final_price}")

inventory[chosen_items] -= 1
print("Updated Inventory:", inventory)

print("Thank you for your purchase!")