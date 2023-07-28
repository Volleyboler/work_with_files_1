
class RecipesBook:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.cook_book = self._create_cook_book(self.file_path)

    def _create_cook_book(self, file_path):
        with open(file_path, encoding="utf=8") as file:
            cook_book = {}
            while True:
                try:
                    name_dish = file.readline().strip()
                    amount_lines = int(file.readline())
                    ingredients_list = []
                    while amount_lines != 0:
                        ingredient_list = file.readline().strip().split(" | ")
                        ingredients_list.append({"ingredient_name": ingredient_list[0], "quantity": int(ingredient_list[1]), "measure": ingredient_list[2]})
                        amount_lines -= 1
                    cook_book[name_dish] = ingredients_list
                    file.readline()
                except:
                    break
            return cook_book

    def get_shop_list_by_dishes(self, dishes: list, person_count: int) -> dict:
        ingredients_dict = {}
        for dish in dishes:
            try:
                for ingredient in self.cook_book[dish]:
                    ingredient_name = ingredient['ingredient_name']
                    quantity = ingredient['quantity'] * person_count
                    measure = ingredient['measure']
                    if ingredient_name in ingredients_dict:
                        ingredients_dict[ingredient_name]['quantity'] += quantity
                    else:
                        ingredients_dict[ingredient_name] = {'quantity': quantity, 'measure': measure}
            except:
                print(f"{dish} отсутствует в кулинарной книге! Ингредиенты для этого блюда не посчитаны!")
        return ingredients_dict


recipes_file_path = "recipes.txt"
recipes_book = RecipesBook(recipes_file_path)

dishes_list = ['Запеченный картофель', 'Чай', 'Омлет', 'Фахитос']

print(recipes_book.cook_book)
print(recipes_book.get_shop_list_by_dishes(dishes_list, 4))
