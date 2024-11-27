import csv
import datetime

def read_product(filename):
    products = {}
    with open(filename, mode="r", newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
           key = row[0]
           prod_desc = row[1]
           prod_price = row[2]
           products[key] = [prod_desc, prod_price]

        return products

def read_product_csv(filename):
  products_id =[]
  quantities = []
  with open(filename, "rt") as csv_request:
    reader = csv.reader(csv_request)
    next(reader)

    for row in reader:
      products_id.append(row[0])
      quantities.append(row[1])

  return products_id, quantities

def main():
  products = read_product("products (1).csv")
  products_id = read_product_csv("request.csv")[0]
  order_quantities = read_product_csv("/content/request.csv")[1]

  print()
  print("Mini super Python")
  print()

  subtotal = 0
  total_item = 0

  for i in range (len(products_id)):
    product = products[products_id[i]]
    name = product[0]
    price = float(product[1])
    quantity = order_quantities[i]
    print(f"{name}: {price} x {quantity}")
    subtotal += price * int(quantity)

  print()
  print(f"Subtotal: ${subtotal:.2f}")
  print(f"Total item: {int(total_item)}")
  print(f"Tax: ${subtotal * 0.06:.2f}")
  print(f"Total: ${subtotal * 1.06:.2f}")

  print()
  payment = float(input("Payment: $"))
  Change = payment - (subtotal * 1.06)
  if Change < 0:
    print("You need more money")
  elif Change >= 0:
    print(f"Your change is: ${Change:.2f}")

main()