spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    '''Return a list of names of all the spicy foods.'''
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    '''Return a list of spicy foods that have a heat_level greater than 5.'''
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    '''Print each food's name, cuisine, and heat level with 🌶 emojis for heat level.'''
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    '''Return a food item that matches the provided cuisine.'''
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # If no matching food is found

def print_spiciest_foods(spicy_foods):
    '''Print foods with heat_level over 5, formatted with 🌶 emojis for heat level.'''
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    '''Return the average heat level of all the spicy foods.'''
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods) if spicy_foods else 0  # To handle division by zero if list is empty

def create_spicy_food(spicy_foods, spicy_food):
    '''Add a new spicy food to the list and return the updated list.'''
    spicy_foods.append(spicy_food)
    return spicy_foods
