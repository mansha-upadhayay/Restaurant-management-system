import json

with open("menu.json", "r") as file:
    data = json.load(file)

items = data["items"]


def save_menu():
    with open("menu.json", "w") as file:
        json.dump({"items": items}, file, indent=4)


def update_menu():

    print("\nUpdate Menu")
    print("-" * 30)
    print("1. Add Item")
    print("2. Update Item")
    print("3. Remove Item")
    print("4. Go Back")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        item_id = int(input("Enter item ID: "))
        name = input("Enter item name: ")
        price = int(input("Enter item price: "))

        new_item = {
            "id": item_id,
            "name": name,
            "price": price
        }

        items.append(new_item)
        save_menu()

        print("Item added successfully!")

    elif choice == 2:

        item_id = int(input("Enter item ID: "))

        for item in items:
            if item["id"] == item_id:

                print("Item:", item["name"])

                new_name = input("Enter new name: ")
                new_price = int(input("Enter new price: "))

                item["name"] = new_name
                item["price"] = new_price

                save_menu()

                print("Item updated successfully!")
                break

        else:
            print("Item not found.")

    elif choice == 3:

        item_id = int(input("Enter item ID: "))

        for item in items:
            if item["id"] == item_id:

                items.remove(item)
                save_menu()

                print("Item removed successfully!")
                break

        else:
            print("Item not found.")

    elif choice == 4:
        print("Going back...")

    else:
        print("Invalid choice.")
