# shopping_cart.py

import os
import pandas as pd
import datetime

def to_usd(my_price):
        return f"${my_price:,.2f}" #> $12,000.71

CSV_FILENAME = "products.csv"
csv_filepath = os.path.join("data",CSV_FILENAME)
data = pd.read_csv(csv_filepath)
data_dict = data.to_dict('records')
products = list(data_dict)

# based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

total_price = 0
selected_ids = []

while True:
      selected_id = input("Please input a product identifier: ")
      if selected_id == "DONE":
          break
      else:        
         selected_ids.append(selected_id)
print("---------------------------------")
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")
print("---------------------------------")
today = datetime.datetime.now()
print("CHECKOUT AT: " + today.strftime("%Y-%m-%d %I:%M %p"))
print("SELECTED PRODUCTS:")
for selected_id in selected_ids:
      matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
      try:
          matching_product = matching_products[0]
      except IndexError as IndexError:
          print("PLEASE USE VALID ID AND START OVER")
          exit()
      matching_product = matching_products[0]
      total_price = total_price + matching_product["price"]
      print(f"... " + str(matching_product["name"]) + " " + str("(") + str(to_usd(matching_product["price"]) + str(")")))
print("---------------------------------")
print(f"SUBTOTAL: " + str(to_usd(total_price)))
tax = total_price * 0.0875
print("TAX: " + str(to_usd(tax)))
print("TOTAL: " + str(to_usd(total_price + tax)))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")

# Example Output
#(shopping-env)  --->> python shopping_cart.py
#Please input a product identifier: 1
#Please input a product identifier: 2
#Please input a product identifier: 3
#Please input a product identifier: 2
#Please input a product identifier: 1
#Please input a product identifier: DONE
#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2020-02-07 03:54 PM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... All-Seasons Salt ($4.99)
#>  ... Robust Golden Unsweetened Oolong Tea ($2.49)
#>  ... All-Seasons Salt ($4.99)
#>  ... Chocolate Sandwich Cookies ($3.50)
#> ---------------------------------
#> SUBTOTAL: $19.47
#> TAX: $1.70
#> TOTAL: $21.17
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------