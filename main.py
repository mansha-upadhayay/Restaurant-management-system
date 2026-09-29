import json
import update_menu
import reviews

with open('menu.json', 'r') as f:
    data = json.load(f)
    items = data.get('items', [])

while True:
    print("\nWelcome to our restaurant!")
    print("-" * 30)
    print("1. Show Menu")
    print("2. Order Items")
    print("3. Update Menu")
    print("4. Add reviews")
    print("5. Exit")
    print("-" * 30)
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print('ID\tName\tPrice')
        for item in items:
            print(f"{item.get('id')}\t{item.get('name')}\t{item.get('price')}")
            
    elif choice == 2:
        order_item = input("Which item you want to try? (Enter ID): ")
        for item in items:
            if str(item.get('id')) == order_item:
                print(f"{item.get('name')} - {item.get('price')}")
                print(f"Total Amount: {item.get('price')}")
                
    elif choice == 3:
        update_menu.update_menu()
        
    elif choice == 4:
        print("Add Reviews")
        reviews.add_review()
        
    elif choice == 5:
        print("Thankyouu for visiting our restraunt!!")
        break