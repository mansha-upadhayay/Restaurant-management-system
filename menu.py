import json

with open('menu.json', 'r') as f:
    data = json.load(f)

items = data["items"]


def show_menu():
    print('-' * 40)
    print('ID\tName\t\tPrice')
    print('-' * 40)

    for item in items:
        print(item["id"], '\t', item["name"], '\t\t₹', item["price"])

    print('-' * 40)