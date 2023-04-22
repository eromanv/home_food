import requests
from bs4 import BeautifulSoup
import lxml


url = 'https://fitstars.ru/recipes'

RECIPRE_URLS = []
RECIPE_RUSSIAN_NAMES_OR = []
RECIPES_TO_WORK_WITH = {}
RECIPE_STEP_BY_STEP = []
ALL_INGREDIENTS = []
HEADERS = {
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537'
}


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

    tuple_list = [(x, y) for x, y in zip(RECIPRE_URLS, RECIPE_RUSSIAN_NAMES_OR)]
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
    RECIPE_STEP_BY_STEP_for_sql = '; '.join(RECIPE_STEP_BY_STEP)
    # print(each_step)
    # print(each_step_nobreaks)
    # print(RECIPE_STEP_BY_STEP)

   #  print(RECIPE_STEP_BY_STEP_for_sql)
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
        ALL_INGREDIENTS = '; '.join(each_ingredient_nobreaks)
        # ALL_INGREDIENTS.append(each_ingredient_nobreaks)
        # ALL_INGREDIENTS_for_sql = ALL_INGREDIENTS.split('\n')
   #  print(each_ingredient_nobreaks)
   #  print(ALL_INGREDIENTS_for_sql)
   # print(type(ALL_INGREDIENTS_for_sql))
    #print(ALL_INGREDIENTS)
    #print(type(ALL_INGREDIENTS))
    #return each_ingredient_nobreaks
    return ALL_INGREDIENTS

get_reciept ('https://fitstars.ru/recipes/zapechyonnye-kurinye-yajca-v-tortili')