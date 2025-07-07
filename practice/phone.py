# Create a simple address book program that allows users to add,
# view, and delete contacts (name and phone number) using a dictionary
contact = []
# while True:
#    option=input("Do you want toe add, view ,quit,or delete?:")
#    if option == "view":
#       print (contact)
#    elif option == "add":
#       person = {}
#       name = input("enter your name:")
#       phone = input("enter your phone number:")
#       person["name"] = name
#       person["phone"] = phone
#       print("Data was added:", person)
#       contact.append(person)
#    elif option == "delete":
#       delete = input("Delete 'name' or 'phone':")
#       for i in range(len(contact)):
#          profile = contact[i]
#          if profile ["name"] == delete or profile ["phone"] == delete:
#             contact.pop(i)
#    elif option == "quit":
#       break
# cart = []
# print("=== Convenience Store Checkout ===")
# print("Enter item names and prices.")
# print("Type 'checkout' to finish and see the receipt.")
# while True:
#     item_name = input("Item name: ")
#     if item_name == "checkout":
#         break
#     item_price = int(input("Item price: "))
#     cart.append((item_name, item_price))
#     print(f"'{item_name}' has been added to your cart.")
#
# print("=== Receipt ===")
# total = 0
# for item, price in cart:
#     print(f"{item}: {price} won")
#     total += price
# print(f"Total: {total}")
# print("Thank you for shopping!")
# cart = []
# print("=== Convenience Store Checkout ===")
# print("Enter item names and prices.")
# print("Type 'checkout' to finish and see the receipt.")
#
# while True:
#     item_name = input("Item name: ")
#     if item_name.lower() == "checkout":
#         break
#     try:
#         item_price = int(input("Item price: "))
#         item = {"name": item_name, "price": item_price}
#         cart.append(item)
#         print(f"'{item_name}' has been added to your cart.")
#     except ValueError:
#         print("Please enter a valid number for the price.")
#
# print("=== Receipt ===")
# total = 0
# for item in cart:
#     print(f"{item['name']}: {item['price']} won")
#     total += item['price']
# print(f"Total: {total}")
# print("Thank you for shopping!")
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result

