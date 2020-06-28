from pprint import pprint
def cook_book(txt_file):
    cooking = dict()
    with open(txt_file, encoding='utf-8') as book:
        while True:
            dish = book.readline().strip()
            if not dish:
                break
            cooking[dish] = list()
            q_i= book.readline().strip()
            q_i = int(q_i)
            ingredients_unformatted = list()
            for i in range(0,q_i):
                ingredients_unformatted.append(book.readline().strip())
                i +=1
            ingredients_unsplitted = list()
            for ingredient in ingredients_unformatted:
                ingredients_unsplitted.append(ingredient.split(' | '))
            ingredients = list()
            for ingredient_1 in ingredients_unsplitted:
                ingredient_final = dict()
                ingredient_final['ingredient_name'] = ingredient_1[0]
                ingredient_final['quantity'] = ingredient_1[1]
                ingredient_final['measure'] = ingredient_1[2]
                ingredients.append(ingredient_final)
            cooking[dish] = ingredients
            book.readline().strip()
    return(cooking)


a = cook_book('Cooking_Book.txt')

pprint(a)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        if dish in a.keys():
            for value in a[dish]:
                if value['ingredient_name'] not in ingredients.keys():
                    ingredients[value['ingredient_name']] = {'measure': value['measure'], 'quantity': int(value['quantity'])*person_count}
                else:
                    ingredients[value['ingredient_name']]['quantity'] = int(ingredients[value['ingredient_name']]['quantity'])+int(value['quantity'])*person_count
    pprint(ingredients)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)


