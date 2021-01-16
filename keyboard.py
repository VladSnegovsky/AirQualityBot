from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import english as eng

# Back
button_Back = KeyboardButton("Back↩")


# Languages
button_Ukrainian = KeyboardButton("Українська")
button_English = KeyboardButton("English󠁧󠁢󠁥󠁮󠁧󠁿")
keyboard_languages = ReplyKeyboardMarkup(resize_keyboard=True).add(button_Ukrainian, button_English)

def new_language(language):
    button_english = KeyboardButton("English")
    button_ukrainian = KeyboardButton("Українська")
    button_back = KeyboardButton(language.button_back)
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_ukrainian, button_english).add(button_back)


def ok_i_read_it(language):
    button_ok_i_read_it = KeyboardButton(language.button_ok_i_read_it)
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_ok_i_read_it)

#Select Location
def main(language):
    button_select_location = KeyboardButton(language.button_select_location)
    button_my_locations = KeyboardButton(language.button_my_locations)
    button_information = KeyboardButton(language.button_about_this_bot)
    button_settings = KeyboardButton(language.button_settings)
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_select_location, button_my_locations).add(button_information, button_settings)


#Add Location
def add_location(language):
    button_find_me = KeyboardButton(language.button_find_me, request_location=True)
    button_select_from_list = KeyboardButton(language.button_select_from_list)
    button_back = KeyboardButton(language.button_back)
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_find_me, button_select_from_list).add(button_back)


# Yes/No
def yes_no(language):
    button_yes = KeyboardButton(language.button_yes)
    button_no = KeyboardButton(language.button_no)
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_yes, button_no)


# Add
def add(language):
    button_add = KeyboardButton(language.button_add)
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_add)


# Change
def change_cancel(language):
    button_change = KeyboardButton(language.button_change)
    button_cancel = KeyboardButton(language.button_cancel)
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_change, button_cancel)


# Step
def step(language):
    button_10 = KeyboardButton("10")
    button_15 = KeyboardButton("15")
    button_20 = KeyboardButton("20")
    button_25 = KeyboardButton("25")
    button_30 = KeyboardButton("30")
    button_35 = KeyboardButton("35")
    button_40 = KeyboardButton("40")
    button_45 = KeyboardButton("45")
    button_50 = KeyboardButton("50")
    button_change = KeyboardButton(language.button_change)
    button_cancel = KeyboardButton(language.button_cancel)
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_10, button_15, button_20).add(button_25, button_30, button_35).add(button_40, button_45, button_50).add(button_change, button_cancel)


# Locations Settings
def generate_location_settings_keyboard(notifications, language):
    button_edit_name = KeyboardButton(language.button_edit_name)
    button_edit_step = KeyboardButton(language.button_edit_step)
    button_notifications_on = KeyboardButton(language.button_notifications_on)
    button_notifications_off = KeyboardButton(language.button_notifications_off)
    button_delete_location = KeyboardButton(language.button_delete_location)
    button_back = KeyboardButton(language.button_back)

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    if notifications:
        keyboard.add(button_edit_name, button_edit_step, button_notifications_off, button_delete_location, button_back)
    else:
        keyboard.add(button_edit_name, button_edit_step, button_notifications_on, button_delete_location, button_back)
    return keyboard


# Generate Keyboard from txt file
checkout_countries_array = []
checkout_cities_array = []

def generate_keyboard(place, language):
    """Generate Keyboard from txt file"""
    place = place.lower()
    if place == "countries":
        file = open(language.translate_country(place) + ".txt", "r")
    else:
        file = open(eng.to_eng(place) + ".txt", "r")
    places_array = []
    for line in file:
        places_array.append(line[:-1])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    temp_buttons = []
    checkout_countries_array.clear()
    checkout_cities_array.clear()
    for i in places_array:
        if place == "countries":
            checkout_countries_array.append(language.translate_country(i))
            temp_buttons.append(KeyboardButton(text=language.translate_country(i)))
        else:
            checkout_cities_array.append(language.translate_city(i))
            temp_buttons.append(KeyboardButton(text=language.translate_city(i)))
    keyboard.add(*temp_buttons)
    button_back = KeyboardButton(language.button_back)
    keyboard.add(button_back)
    return keyboard


# For My Locations
checkout_locations_db = []

def generate_keyboard_locations_db(language):
    """Generate keyboard from db locations"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*checkout_locations_db)
    button_back = KeyboardButton(language.button_back)
    keyboard.add(button_back)
    return keyboard