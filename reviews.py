import json

with open('menu.json', 'r') as f:
    data = json.load(f)

reviews = data.get('reviews', [])


def add_review():

    print('Add Reviews')
    print('_' * 30)

    name = input('Enter your name: ')
    item_id = int(input('Enter item ID to review: '))
    rating = int(input('Enter rating (1-5): '))
    review = input('Enter your review: ')

    new_review = {
        'name': name,
        'item_id': item_id,
        'rating': rating,
        'review': review
    }

    reviews.append(new_review)

    data['reviews'] = reviews

    with open('menu.json', 'w') as f:
        json.dump(data, f, indent=4)

    print('Review added successfully!')