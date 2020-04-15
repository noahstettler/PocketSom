import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


def nutr_scrape(nfact_str):
    nutr_facts = []
    nums = "\d+\.?\d?"
    x = nfact_str
    calories = re.findall(f"{nums} calories", x)
    calories = re.findall(nums, calories[0])
    nutr_facts.append(calories[0])

    sodium = re.findall(f"{nums} mg sodium\.", x)
    sodium = re.findall(nums, sodium[0])
    nutr_facts.append(sodium[0])

    fat = re.findall(f"{nums} g fat | {nums} g total fat", x)
    fat = re.findall(nums, fat[0])
    nutr_facts.append(fat[0])

    cholesterol = re.findall(f"{nums} mg cholesterol", x)
    cholesterol = re.findall(nums, cholesterol[0])
    nutr_facts.append(cholesterol[0])

    carbs = re.findall(f"{nums} g carbohydrates", x)
    carbs = re.findall(nums, carbs[0])
    nutr_facts.append(carbs[0])

    protein = re.findall(f"{nums} g protein", x)
    protein = re.findall(nums, protein[0])
    nutr_facts.append(protein[0])
    return nutr_facts


def recipe_info(url):
    info_dict = {}
    recipe_search = requests.get(url).text
    soup_recipe = BeautifulSoup(recipe_search, "html.parser")
    # recipe name
    try:
        r_title = soup_recipe.find("h1", class_="headline heading-content").text
        ingr_soup = soup_recipe.find_all("span", class_="ingredients-item-name")
        nfacts = soup_recipe.find("div", class_="partial recipe-nutrition-section").text
    except:
        r_title = soup_recipe.find("h1", class_="recipe-summary__h1").text
        ingr_soup = soup_recipe.find_all("span", class_="recipe-ingred_txt added")
        nfacts = soup_recipe.find("div", class_="nutrition-summary-facts").text

    nfacts_clean = x = nfacts.replace("\n", "").replace(";", " ").replace("  ", " ")
    info_dict["Recipe"] = r_title
    info_dict["Nutrition"] = nfacts_clean
    ## ingredients
    ing_list = []
    for i in ingr_soup:
        ing = i.text
        ing_clean = ing.strip()
        ing_list.append(ing_clean)
    info_dict["Ingredients"] = ing_list
    ## nutrition values for model
    nfacts_list = [nutr_scrape(nfacts_clean)]
    info_dict["nfactsList"] = nfacts_list
    return info_dict


# z = recipe_info("https://www.allrecipes.com/recipe/65147/roasted-duck/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202")
# z = recipe_info("https://www.allrecipes.com/recipe/7736/dark-chocolate-cake-i/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202")
# print(z)


# t = nutr_scrape("https://www.allrecipes.com/recipe/65147/roasted-duck/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202")
# print(t)

# recipe_nutrition.append(nfacts)
# nutr_dict = {}
# x = nutr_scrape("https://www.allrecipes.com/recipe/7736/dark-chocolate-cake-i/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202")
# #x = nutr_scrape("https://www.allrecipes.com/recipe/65147/roasted-duck/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202")
# x = x.replace("\n", "").replace(";", " ").replace("  ", " ")
# nums = '\d+\.?\d?'
# calories = re.findall(f'{nums} calories', x)
# nutr_dict['calories'] = re.findall(nums, calories[0])
# sodium = re.findall(f'{nums} mg sodium\.', x)
# nutr_dict['sodium'] = re.findall(nums, sodium[0])
# fat = re.findall(f'{nums} g fat | {nums} g total fat', x)
# nutr_dict['fat'] = re.findall(nums, fat[0])
# cholesterol = re.findall(f'{nums} mg cholesterol', x)
# nutr_dict['cholesterol'] = re.findall(nums, cholesterol[0])
# carbs = re.findall(f'{nums} g carbohydrates', x)
# nutr_dict['carbs'] = re.findall(nums, carbs[0])
# class="nutrition-summary-facts"
# protein = re.findall(f'{nums} g protein', x)
# nutr_dict['protein'] = re.findall(nums, protein[0])
# print(recipe_nutrition)
# filepath = 'recipeScraped2.html'
# with open(filepath, "w+") as f:
#    f.write(recipe_search)


# print(soup_recipe)
