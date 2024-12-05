EXCHANGE_RATES = {
    "USD": 1,
    "EUR": 0.9,
    "EGP": 24
}

main_store = {
    "Water": {"price": 10, "stock": 1000},
    "Soda": {"price": 15, "stock": 500},
    "Bread": {"price": 5, "stock": 300},
}

stationary_store = {
    "Pen": {"price": 2, "stock": 200},
    "Notebook": {"price": 10, "stock": 150},
    "Eraser": {"price": 1, "stock": 300},
}

users_db = {
    "user1": {"password": "password123", "attempts": 0}
}

def display_store(store_name, inventory):
    print(f"\n{store_name.upper()} - Products Available:")
    print(f"{'Product':<10} {'Price ($)':<10} {'Stock':<10}")
    print("-" * 30)
    for product, details in inventory.items():
        print(f"{product:<10} {details['price']:<10} {details['stock']:<10}")
    print("-" * 30)

def calculate_discount_main_store(total_units):
    max_discount = 25
    discount = min((total_units // 250) * 5, max_discount)
    return discount

def calculate_discount_stationary_store(total_units):
    return (total_units // 50) * 2

def select_products(store_name, inventory):
    total_cost = 0
    total_units = 0
    while True:
        display_store(store_name, inventory)
        product = input("Enter the product name (or 'done' to finish): ").capitalize()
        if product == "Done":
            break
        if product not in inventory:
            print("Invalid product name! Try again.")
            continue
        
        quantity = int(input(f"Enter quantity for {product}: "))
        if quantity > inventory[product]["stock"]:
            print("Not enough stock! Try a smaller quantity.")
            continue
        
        inventory[product]["stock"] -= quantity
        total_cost += inventory[product]["price"] * quantity
        total_units += quantity
        print(f"Added {quantity} x {product} to your cart.\n")
    
    return total_cost, total_units

def register_user():
    print("\nNo account found. Please create a new account.")
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please choose another one.")
        return None
    password = input("Enter a password: ")
    users_db[username] = {"password": password, "attempts": 0}
    print("Account created successfully!")
    return username

def login():
    print("Welcome! Please log in.")
    username = input("Enter username: ")
    if username not in users_db:
        return register_user()
    
    attempts = 0
    while attempts < 3:
        password = input("Enter password: ")
        if users_db[username]["password"] == password:
            print("Login successful!")
            return username
        else:
            attempts += 1
            print(f"Incorrect password. You have {3 - attempts} attempts left.")
    
    users_db[username]["attempts"] += 1
    print("Too many failed attempts. Your account is now locked.")
    return None

def main():
    username = login()
    if not username:
        print("You cannot proceed without logging in.")
        return
    
    print("Welcome to the Shopping System!")
    total_cost = 0
    total_units = 0

    print("\nShopping in the Main Store:")
    main_cost, main_units = select_products("Main Store", main_store)
    main_discount = calculate_discount_main_store(main_units)
    main_cost_after_discount = main_cost * (1 - main_discount / 100)
    print(f"\nMain Store Total: ${main_cost:.2f} | Discount: {main_discount}% | After Discount: ${main_cost_after_discount:.2f}\n")
    total_cost += main_cost_after_discount
    total_units += main_units

    navigate = input("Would you like to shop in the Stationary Store? (yes/no): ").lower()
    if navigate == "yes":
        print("\nShopping in the Stationary Store:")
        stationary_cost, stationary_units = select_products("Stationary Store", stationary_store)
        stationary_discount = calculate_discount_stationary_store(stationary_units)
        stationary_cost_after_discount = stationary_cost * (1 - stationary_discount / 100)
        print(f"\nStationary Store Total: ${stationary_cost:.2f} | Discount: {stationary_discount}% | After Discount: ${stationary_cost_after_discount:.2f}\n")
        total_cost += stationary_cost_after_discount
        total_units += stationary_units

    print("\nDelivery Options:")
    print("1. Delivery ($200)")
    print("2. Pickup ($50)")
    option = int(input("Choose an option (1 or 2): "))
    if option == 1:
        total_cost += 200
        print("Delivery selected ($200).")
    elif option == 2:
        total_cost += 50
        print("Pickup selected ($50).")

    print("\nCurrency Options:")
    print("1. USD")
    print("2. EUR")
    print("3. EGP")
    currency = int(input("Choose a currency (1/2/3): "))
    if currency == 1:
        currency_name = "USD"
    elif currency == 2:
        currency_name = "EUR"
    elif currency == 3:
        currency_name = "EGP"
    else:
        print("Invalid option! Defaulting to USD.")
        currency_name = "USD"

    converted_total = total_cost * EXCHANGE_RATES[currency_name]
    print(f"\nFinal Total: {converted_total:.2f} {currency_name} (Converted at rate {EXCHANGE_RATES[currency_name]}).\n")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
1
