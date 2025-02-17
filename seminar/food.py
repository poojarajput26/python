# Food items and their prices
menu = {
    "Pizza": 10.0,
    "Burger": 5.0,
    "Pasta": 7.5,
    "Fries": 2.5,
    "Coke": 1.5,
    "Ice Cream": 3.0
}

# Function to display the menu
def display_menu():
    print("Welcome to the Food Shop! 🍔🍕🍝")
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

# Function to generate the bill
def generate_bill(selected_items):
    print("\n------ Bill ------")
    total_cost = 0
    for item, quantity in selected_items.items():
        price = menu[item]
        cost = price * quantity
        total_cost += cost
        print(f"{item} x{quantity}: ${cost:.2f}")
    print("-----------------")
    print(f"Total: ${total_cost:.2f}")
    print("Thank you for shopping with us! 😄")

# Function to take the customer's order
def take_order():
    selected_items = {}
    while True:
        display_menu()
        item = input("\nEnter the food item you want to order (or type 'done' to finish): ").capitalize()

        if item == "Done":
            break
        elif item not in menu:
            print("Sorry, we don't have that item on the menu. Please choose a valid item.")
        else:
            quantity = int(input(f"How many {item}s would you like to order? "))
            selected_items[item] = selected_items.get(item, 0) + quantity

    # Generate the bill
    generate_bill(selected_items)

# Start the order process
take_order()
