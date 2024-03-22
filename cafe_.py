"""
List the items of your menu.
Create a dictionary that contains the amount of items you sell per day.
Create another dictionary that contains the price of each corresponding item. 
Create a for loop that calculates the value of each item.
Then calculate and print the total stock value.
"""

menu_items = ['cupcakes', 'croissants', 'pain au chocolat', 'cinnamon rolls', 'iced latte', 'hot chocolate', 'latte', 'cappucino', 'black coffee']

menu_dict = {'cupcakes' : 800,
         'croissants': 950,
         'pain au chocolat': 950,
         'cinnamon rolls': 700, 
         'iced latte': 1150,
         'hot chocolate': 1500,
         'latte': 1150,
         'cappucino': 1150,
         'black coffee': 1000}

menu_values = menu_dict.values()

price_dict = {'cupcakes' : 0.75,
         'croissants': 1.15,
         'pain au chocolat': 0.99,
         'cinnamon rolls': 1.50, 
         'iced latte': 1.20,
         'hot chocolate': 1.00,
         'latte': 1.20,
         'cappucino': 1.20,
         'black coffee': 1.20}

price_values = price_dict.values()

total_stock = 0

for item in menu_items:
    item_value = stock_dict[item] * price_dict[item]
    total_stock += item_value

print(f"The total stock amount in the cafe per day is £", total_stock)
