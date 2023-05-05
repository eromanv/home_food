import requests
from bs4 import BeautifulSoup
import lxml
import re


url = 'https://fitstars.ru/recipes'

RECIPRE_URLS = []
RECIPE_RUSSIAN_NAMES_OR = []
RECIPES_TO_WORK_WITH = {}
RECIPE_STEP_BY_STEP = []
ALL_INGREDIENTS = []
HEADERS = {
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537'
}
FOOD_TO_BUY = []


def get_data(url):

    req = requests.get(url, HEADERS)
    req.encoding = 'utf-8'
    src = req.text

    # with open('food_from_fitstars2.html', 'w',  encoding='utf-8') as file:
    # file.write(req.text)

    # with open('food_from_fitstars2.html', encoding='utf-8') as file:
    # src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    recipies = soup.find_all('section', class_='main-card diet-card')
    for recipe in recipies:
        recipre_url = 'https://fitstars.ru' + recipe.find('a').get('href')
        RECIPRE_URLS.append(recipre_url)

    soup = BeautifulSoup(src, 'lxml')
    recipe_russian_names = soup.find_all(
        'p', class_='main-card__title diet-card__title line-clamp line-clamp--2')
    # print(recipe_russian_names)
    for russian_name in recipe_russian_names:
        russian_name_or = russian_name.get('title')
        RECIPE_RUSSIAN_NAMES_OR.append(russian_name_or)

    # recipe_russian_names.append(recipe_russian_name)

    # print(recipre_urls, recipe_russian_names_or)
    # recipes_all_list = {}
    # for record in recipes_all_list():
    #     record[]

    #     {
    #         'Имя продукта': recipe_russian_name,
    #         'Cсылка на продукт': recipe_url,
    #     }
    # )

    # print(recipes_all_list)

    tuple_list = [(x, y)
                  for x, y in zip(RECIPRE_URLS, RECIPE_RUSSIAN_NAMES_OR)]
    return tuple_list

    # for record in range(len(RECIPE_RUSSIAN_NAMES_OR)):
    #     RECIPES_TO_WORK_WITH[RECIPRE_URLS[record]
    #                          ] = RECIPE_RUSSIAN_NAMES_OR[record]
    # return RECIPES_TO_WORK_WITH

    # print(recipes_to_work_w


def get_reciept(link):
    # for link in RECIPRE_URLS:
    RECIPE_STEP_BY_STEP = []
    link_get = requests.get(link, HEADERS)
    link_get.encoding = 'utf-8'
    link_src = link_get.text
    soup = BeautifulSoup(link_src, 'lxml')
    steps = soup.find_all(
        'div', class_='recipe__item-txt')
    # print(steps)
    for step in steps:
        each_step = step.text
        # each_step_nobreaks = each_step.replace('\n', '.')
        RECIPE_STEP_BY_STEP.append(each_step)
    RECIPE_STEP_BY_STEP_for_sql = ' '.join(RECIPE_STEP_BY_STEP)
    # print(each_step)
    # print(each_step_nobreaks)
    # print(RECIPE_STEP_BY_STEP)

    print(RECIPE_STEP_BY_STEP_for_sql)
    return RECIPE_STEP_BY_STEP_for_sql


def get_ingredients(link):
    # ALL_INGREDIENTS = []
    link_get = requests.get(link, HEADERS)
    link_get.encoding = 'utf-8'
    link_src = link_get.text
    soup = BeautifulSoup(link_src, 'lxml')
    ingredients = soup.find_all(
        'ul', class_='recipe__main-list')
    for ingredient in ingredients:
        each_ingredient = ingredient.text
        each_ingredient_nobreaks = each_ingredient.split('\n')
        ALL_INGREDIENTS = ' '.join(each_ingredient_nobreaks)
        # ALL_INGREDIENTS.append(each_ingredient_nobreaks)
        # ALL_INGREDIENTS_for_sql = ALL_INGREDIENTS.split('\n')
   #  print(each_ingredient_nobreaks)
   #  print(ALL_INGREDIENTS_for_sql)
   # print(type(ALL_INGREDIENTS_for_sql))
    # print(ALL_INGREDIENTS)
    # print(type(ALL_INGREDIENTS))
    # return each_ingredient_nobreaks
    # print('ingredients are added')
    return ALL_INGREDIENTS


def get_calories(link):
    link_get = requests.get(link, HEADERS)
    link_get.encoding = 'utf-8'
    link_src = link_get.text
    soup = BeautifulSoup(link_src, 'lxml')
    calories = soup.find_all('span', itemprop='calories')
    proteins = soup.find_all('span', itemprop='proteinContent')
    carbs = soup.find_all('span', itemprop='carbohydrateContent')
    fats = soup.find_all('span', itemprop='fatContent')
    for calorie in calories:
        each_calorie = calorie.string
    for carb in carbs:
        each_carb = carb.string
    for protein in proteins:
        each_protein = protein.string
    for fat in fats:
        each_fat = fat.string
    print('Калории добавлены')
    total_energy = 'К {} БЖУ{} {} {}'.format(
        each_calorie, each_protein, each_fat, each_carb)
    # print(total_energy)
    return total_energy
    # print(each_calorie, each_protein, each_fat, each_carb)
   # return each_calorie, each_protein, each_fat, each_carb


def get_big_recipe(link):
    names, quantities, measures = [], [], []
    i = 0
    link_get = requests.get(link, HEADERS)
    link_get.encoding = 'utf-8'
    link_src = link_get.text
    soup = BeautifulSoup(link_src, 'lxml')
    ingredients_to_buy = soup.find_all('li', itemprop="recipeIngredient")
    for food in ingredients_to_buy:
        food_item = food.text
        name = re.findall(r'[А-ЯЁ()][а-яё ]/%*|[А-ЯЁ()][а-яё ]*', food_item)
        print(name)
        for item in name:
            each_name = item
        quantity = re.findall(
            r'[\d]{1,3}-[\d]{1,3}|[\d]{1,3}/[\d]{1,3}|[\d]{1,3}', food_item)
        for number in quantity:
            each_quantity = number
        if each_quantity == '1/2':
            each_quantity = 0.5
        if each_quantity == '1-2':
            each_quantity = 1.5
        if each_quantity == '1/4':
            each_quantity = 0.25
        if each_quantity == '1/3':
            each_quantity = 0.3
        if each_quantity == '5-1':
            each_quantity = 10
        if each_quantity == '3-5':
            each_quantity = 4
        if each_quantity == '3-4':
            each_quantity = 3
        if each_quantity == '2-3':
            each_quantity = 2
        # each_quantity = int(each_quantity)
        print(each_quantity)
        measure = re.findall(r'[\D]{1,5}$', food_item)
        if measure == ['кусу ']:
            each_quantity = 0.5
            measure = ['шт.']
        if measure == ['учок ']:
            each_quantity = 0.5
            measure = ['шт.']
        for unit in measure:
            each_measure = unit
        names.append(each_name)
        quantities.append(each_quantity)
        measures.append(each_measure)
    # FOOD_TO_BUY.append(food_item)
    # print(names, quantities, measures)
    return names, quantities, measures
    # FOOD_TO_BUY_in_one = ' '.join(FOOD_TO_BUY)
    # food_item_nobr = food_item.split()
    # FOOD_TO_BUY = '/n'.join(food_item)
    # ingredients_list_split = ingredients_list.split()
    # for food_st in FOOD_TO_BUY_in_one:
    # FOOD_TO_BUY_in_one_str = ', '.join(food_st)
    # FOOD_TO_BUY_list = re.findall(r'[А-ЯЁ()][а-яё\W\d]*', FOOD_TO_BUY[0][0])
    # ingredients_total = '\n'.join(ingredients_ul)
    # print(ingredients_to_buy)
    # print(FOOD_TO_BUY_in_one)
    # print(type(FOOD_TO_BUY_in_one))


# get_big_recipe(
#     'https://fitstars.ru/recipes/zapechyonnye-kurinye-yajca-v-tortili')
