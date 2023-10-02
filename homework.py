# Definitions
shopping_cart = []

def display_cart():
    print("\nCurrent Shopping Cart:")
    for item in shopping_cart:
        print(f"- {item['name']} ({item['quantity']}): ${item['price']} each")
    print()

def add_item():
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity: "))

    item = {
        'name': name,
        'price': price,
        'quantity': quantity
    }

    shopping_cart.append(item)
    print(f"{quantity} {name}(s) added to the cart.")

def remove_item():
    display_cart()
    item_index = int(input("Enter the index of the item you want to remove (starting with 0): "))

    if 0 <= item_index < len(shopping_cart):
        removed_item = shopping_cart.pop(item_index)
        print(f"{removed_item['name']} removed from the cart.")
    else:
        print("That item does not exist")

def calculate_total():
    total = sum(item['price'] * item['quantity'] for item in shopping_cart)
    print(f"Total cost: ${total:.2f}")
    #floating point decimal format 

# End definitions

# Cart menu loop
while True:
    print("\nOptions:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Display cart")
    print("4. Calculate total")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    # Menu choice ladder
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        display_cart()
    elif choice == '4':
        calculate_total()
    elif choice == '5':
        break
    else:
        print("That is not a valid command. Use the numbers 1-5 to select a choice")

# Calculate and print the receipt
print("\nReceipt:")
display_cart()
calculate_total()
