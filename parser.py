import requests
from bs4 import BeautifulSoup
import lxml


url = 'https://fitstars.ru/recipes'

def get_data(url):
    headers = {
        'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537'
    }
    req = requests.get(url, headers)
    req.encoding = 'utf-8'
    src = req.text

    # with open('food_from_fitstars2.html', 'w',  encoding='utf-8') as file:
        # file.write(req.text)

    # with open('food_from_fitstars2.html', encoding='utf-8') as file:
        # src = file.read()

    recipre_urls = []
    recipe_russian_names_or = []
    recipes_to_work_with = {}

    soup = BeautifulSoup(src, 'lxml')
    recipies = soup.find_all('section', class_='main-card diet-card')
    for recipe in recipies:
        recipre_url = 'https://fitstars.ru' + recipe.find('a').get('href')
        recipre_urls.append(recipre_url)

    soup = BeautifulSoup(src, 'lxml')
    recipe_russian_names = soup.find_all(
        'p', class_='main-card__title diet-card__title line-clamp line-clamp--2')
    # print(recipe_russian_names)
    for russian_name in recipe_russian_names:
        russian_name_or = russian_name.get('title')
        recipe_russian_names_or.append(russian_name_or)

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
    for record in range(len(recipe_russian_names_or)):
        recipes_to_work_with[recipre_urls[record]] = recipe_russian_names_or[record]
    
    print(recipes_to_work_with)


get_data('https://fitstars.ru/recipes')
