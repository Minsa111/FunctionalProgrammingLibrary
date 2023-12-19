# Define dictionaries to store user credentials and roles
users = {
    "admin": "adminpass",
    "user1": "userpass1",
    "user2": "userpass2"
}

user_roles = {
    "admin": True,
    "user1": False,
    "user2": False
}

# Define an empty list to store items
items = []

# Function to perform user login
def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            return username
        else:
            print("Invalid login credentials. Please try again.")

# Function to create a new item
def create_item(item_name):
    items.append(item_name)
    print(f"Item '{item_name}' has been created.")

# Function to read (list) all items
def read_items():
    if items:
        print("Items in the list:")
        for item in items:
            print(item)
    else:
        print("The list is empty.")

# Function to update an existing item
def update_item(old_item, new_item):
    if old_item in items:
        index = items.index(old_item)
        items[index] = new_item
        print(f"Item '{old_item}' has been updated to '{new_item}'.")
    else:
        print(f"Item '{old_item}' not found in the list.")

# Function to delete an item
def delete_item(item_name):
    if item_name in items:
        items.remove(item_name)
        print(f"Item '{item_name}' has been deleted.")
    else:
        print(f"Item '{item_name}' not found in the list.")

# Main program loop
while True:
    print("\nCRUD Menu:")
    print("1. Login")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        username = login()
        is_admin = user_roles.get(username, False)
        role = "admin" if is_admin else "user"
        print(f"Logged in as {role}: {username}")

        if is_admin:
            print("Welcome, admin.")
            while True:
                print("\nAdmin Options:")
                print("1. Create an item")
                print("2. Read items")
                print("3. Update an item")
                print("4. Delete an item")
                print("5. Logout")
                admin_choice = input("Enter your choice (1/2/3/4/5): ")

                if admin_choice == "1":
                    item_name = input("Enter the item name: ")
                    create_item(item_name)
                elif admin_choice == "2":
                    read_items()
                elif admin_choice == "3":
                    old_item = input("Enter the old item name: ")
                    new_item = input("Enter the new item name: ")
                    update_item(old_item, new_item)
                elif admin_choice == "4":
                    item_name = input("Enter the item name to delete: ")
                    delete_item(item_name)
                elif admin_choice == "5":
                    print("Logging out as admin.")
                    break
                else:
                    print("Invalid choice. Please enter a valid option (1/2/3/4/5).")
        else:
            print("Welcome, normal user.")
            while True:
                print("\nUser Options:")
                print("1. Read items")
                print("2. Logout")
                user_choice = input("Enter your choice (1/2): ")

                if user_choice == "1":
                    read_items()
                elif user_choice == "2":
                    print(f"Logging out as {role}: {username}.")
                    break
                else:
                    print("Invalid choice. Please enter a valid option (1/2).")
    elif choice == "2":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2).")
