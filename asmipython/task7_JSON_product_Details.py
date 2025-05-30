#Parse a JSON file representing product details(name,price,quantity)and display the details in tabular format.
import json
products=[
    {"name":"Noodles","price":50,"quantity":6},
    {"name":"Biscuits","price":10,"quantity":3},
    {"name":"chocolate","price":100,"quantity":9}   
]
with open("products.json","w") as file:
    json.dump(products,file,indent=4)

with open("products.json","r") as file:
    data=json.load(file)

print("{:<15}{:<15}{:<15}".format("ProductName","Price","Quantity"))
print("-"*38)

for product in products:
    print("{:<15}{:<15}{:<15}".format(product["name"],product["price"],product["quantity"]))