from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json

# Messages
def msg_hi_message():
    return "Hi🙋‍♂️! My name is Airo🤖 and I can show you Air Quality☁️ Level in any " \
           "place🗺 you want."

def msg_about_help():
    return "\n\nYou can also see this instruction when you want by sending a bot /help."

def msg_maximum_length_50():
    return "❗️Maximum length of name must be 5️⃣0️⃣. Write new one."

def msg_your_locations():
    return "Here's your locations😎. Click on location📍 to see informationℹ️.\nYou " \
           "also can edit it🧐."

def msg_you_have_no_locations():
    return "You have no locations😞."

def msg_main_message():
    return "Choose what you want to do."

def msg_choose_list_or_location():
    return "Ok🙂. Now you can choose - share your current location📍 or select one " \
           "from 📃."

def msg_geolocation_is_not_available():
    return "By the way🤔, geolocation is not available😔 on the desktop🖥 " \
           "version of telegram."

def msg_list_of_countries():
    return "Here is the list of countries🇬🇧🇩🇪. Choose the country you need🧐."

def msg_do_you_want_to_add_this_location():
    return "Do you want to add this location📍 to your list📄? You will be " \
           "notified if the level🌡 of air💨 pollution rises⚠️."

def msg_do_you_want_to_be_notified():
    return "Do you🤓 want to be notified about air💨 quality when it gets out of order😧?"

def msg_send_me_new_name_add():
    return "Send me new name for this location😁 and then click Add."

def msg_if_you_will_not_send_it(name):
    return "If you won't send📨 it and click <i>Add</i>, the name will be <i><b>" \
           + name + "</b></i>."

def msg_such_name_is_already_exists():
    return "Such name is already exists🙄."

def msg_you_step_for_this_location_is(step):
    return "Step for this location is " + str(step) + "."

def msg_choose_a_city():
    return "Now choose a city🏙 you want to know about🤔."

def msg_no_stations():
    return "Sorry😔! There are no stations yet🗿🗿🗿. Try to use🤔 your location to find " \
           "the nearest one."

def msg_you_have_this_location(name):
    return "Incidentally💁‍♂️, you already have this location <i><b>" + name + "</b></i>."

def msg_write_new_name_change():
    return "Send✍️ new name for this location📍 and click🖱 change."

def msg_select_new_step():
    return "Select new Step on your keyboard⌨️."

def msg_here_is_the_name(name):
    return "Thx😃, here is the name for this location - <i><b>" + name + "</b></i>."

def msg_about_this_bot():
    return "Hi! My name is Vlad.\n\nI created a bot as a course robot and, when I finished, " \
           "I launched it on the server for post-robotic. If you have a mercy, or if you " \
           "are saying, you can write me @snegovskyvlad. You can also be amazed at the " \
           "instructions on how to visit the bot /help."

def msg_change_language():
    return "Please, select new language."

def msg_instructions():
    return "🔘 You can add new location by clicking on <i><b>Select new location</b></i>. There " \
           "you will see two options - <i><b>Share my location</b></i> and <i><b>Select from " \
           "list</b></i>. If you want the bot to find the nearest station to you - click first," \
           "else click second. \nIf you choose <i><b>Select from list</b></i>, there you will see" \
           "the list of countries. Choose the one you need. Then choose the city.\nAfter you have" \
           " chosen the right place or sent your location to the bot, the bot will ask you if you" \
           " want to save this location to your list. Answer as you like.\nIf you answer Yes, bot " \
           "will ask you to choose the name for this location. You can send(be careful to send " \
           "it, not only type) and then click <i><b>Add</b></i>. After - choose if you want to get" \
           "notifications about changing of Air Quality Level.\n\n🔘 If you click <i><b>My " \
           "Locations</b></i>, you will see the list of your saved locations on keyboard or bot will " \
           "say you that you don't know them. If you have at least 1 location, you can click on it and " \
           "get current information about this place. Look at the keyboard, there you will see Settings" \
           "of this location. You can change:\n   Name: click on <i><b>Edit Name</b></i>✍️ and send" \
           "(be careful to send new name, not only type it) new name to bot, then click <i><b>Change</b>" \
           "</i>.\n   Step: at first, you must know that Air Quality Level is measured in AQI units - the " \
           "number that you will see in Information Messages from bot. Step - the number by which" \
           " the air level should change in order for you to receive a notification. To change it - click " \
           "<i><b>Edit Step</b></i>✍️, then choose new Step on the keyboard and after that click <i><b>" \
           "Change</b></i>.\n   Notification: to turn ON/OFF notification click <i><b>Notifications On" \
           "</b></i>🔔/<i><b>Notifications Off</b></i>🔕.\n   To delete location - click <i><b>Delete " \
           "Location</b></i>🗑.\n\n🔘 In <i><b>About this Bot</b></i> you will receive relevant information." \
           "\n\n🔘 In <i><b>Settings</b></i>⚙️ you can change language.\n\n\nIf you find any bug, have a " \
           "question or have any suggestions, you can write to me @snegovskyvlad."


# Answer
def compose_a_message(answer):
    """composes answer"""
    answer = answer["data"]
    aqi = answer["aqi"]
    if aqi <= 50:
        return "AQI is <b>" + str(aqi) + "</b>🌡\n\n" \
                                         "🟢 <b>Good</b> 🟢\n" \
                                         "Air quality is considered satisfactory, and air pollution poses little or no risk."
    elif 51 <= aqi <= 100:
        return "AQI is <b>" + str(aqi) + "</b>🌡\n\n" \
                                         "🟡 <b>Moderate</b> 🟢\n" \
                                         "Air quality is acceptable. However, for some pollutants there may be a moderate health " \
                                         "concern for a very small number of people who are unusually sensitive to air pollution.\n\n" \
                                         "Active children and adults, and people with respiratory disease, such as asthma, should " \
                                         "limit prolonged outdoor exertion."
    elif 101 <= aqi <= 150:
        return "AQI is <b>" + str(aqi) + "</b>🌡\n\n" \
                                         "🟡 <b>Unhealthy for Sensitive Groups</b> 🟡\n" \
                                         "Members of sensitive groups may experience health effects. The general public is " \
                                         "not likely to be affected.\n\n" \
                                         "Active children and adults, and people with respiratory disease, such as asthma, " \
                                         "should limit prolonged outdoor exertion."
    elif 151 <= aqi <= 200:
        return "AQI is <b>" + str(aqi) + "</b>🌡\n\n" \
                                         "🟠 <b>Unhealthy</b> 🟠\n" \
                                         "Everyone may begin to experience health effects; members of sensitive " \
                                         "groups may experience more serious health effects.\n\n" \
                                         "Active children and adults, and people with respiratory disease, " \
                                         "such as asthma, should avoid prolonged outdoor exertion. Everyone else, " \
                                         "especially children, should limit prolonged outdoor exertion."
    elif 201 <= aqi <= 300:
        return "AQI is <b>" + str(aqi) + "</b>🌡\n\n" \
                                         "🟠 <b>Very Unhealthy</b> 🔴\n" \
                                         "Health warnings of emergency conditions. The entire " \
                                         "population is more likely to be affected.\n\nActive " \
                                         "children and adults, and people with respiratory disease" \
                                         ", such as asthma, should avoid all outdoor exertion. " \
                                         "Everyone else, especially children, should limit outdoor" \
                                         " exertion."
    elif 301 <= aqi:
        return "AQI is <b>" + str(aqi) + "</b>🌡\n\n" \
                                         "🔴 <b>Hazardous</b> 🔴\n" \
                                         "Health alert: everyone may experience more serious health " \
                                         "effects.\n\nEveryone should avoid all outdoor exertion."


def create_answer(response):
    answer = json.loads(response.text)
    if answer["status"] == "ok":
        return compose_a_message(answer)
    else:
        return "Sorry😔! There are no stations yet🗿🗿🗿. Try to use🤔 your location to find the nearest one."


def create_answer_normalized(response, name):
    """composes "normalized" message"""
    answer = json.loads(response.text)
    answer_temp = answer["data"]
    aqi = answer_temp["aqi"]
    if aqi <= 50:
        return "🟢 🔽Notification🔽 🟢\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> normalized!\n\n" \
               + compose_a_message(answer)
    elif 51 <= aqi <= 100:
        return "🟡 🔽Notification🔽 🟢\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" \
               + compose_a_message(answer)
    elif 101 <= aqi <= 150:
        return "🟡 🔽Notification🔽 🟡\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" \
               + compose_a_message(answer)
    elif 151 <= aqi <= 200:
        return "🟠 🔽Notification🔽 🟠\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" \
               + compose_a_message(answer)
    elif 201 <= aqi <= 300:
        return "🟠 🔽Notification🔽 🔴\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" \
               + compose_a_message(answer)
    elif 301 <= aqi:
        return "🔴 🔽Notification🔽 🔴\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" \
               + compose_a_message(answer)


def create_answer_warning(response, name):
    """composes warning message"""
    answer = json.loads(response.text)
    answer_temp = answer["data"]
    aqi = answer_temp["aqi"]
    if aqi <= 50:
        return "🟢 🔼Warning🔼 🟢\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" \
               + compose_a_message(answer)
    elif 51 <= aqi <= 100:
        return "🟡 🔼Warning🔼 🟢\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" \
               + compose_a_message(answer)
    elif 101 <= aqi <= 150:
        return "🟡 🔼Warning🔼 🟡\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" \
               + compose_a_message(answer)
    elif 151 <= aqi <= 200:
        return "🟠 🔼Warning🔼 🟠\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" \
               + compose_a_message(answer)
    elif 201 <= aqi <= 300:
        return "🟠 🔼Warning🔼 🔴\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" \
               + compose_a_message(answer)
    elif 301 <= aqi:
        return "🔴 🔼Warning🔼 🔴\n\n" \
               "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" \
               + compose_a_message(answer)

# Buttons
button_back = "Back↩"
button_select_location = "Select new location"
button_my_locations = "My Locations"
button_about_this_bot = "About this Bot"
button_find_me = "Share my location"
button_select_from_list = "Select from list"
button_yes = "Yes✅"
button_no = "No❌"
button_add = "Add"
button_change = "Change"
button_cancel = "Cancel"
button_edit_name = "Edit Name✍️"
button_edit_step = "Edit Step✍️"
button_notifications_on = "Notifications On🔔"
button_notifications_off = "Notifications Off🔕"
button_delete_location = "Delete Location🗑"
button_settings = "Settings⚙️"
button_ok_i_read_it = "Ok, I have read it."

# Countries
def translate_country(country_eng):
    return country_eng

# Cities
def translate_city(city_eng):
    return city_eng

def to_eng(place):
    """translate place to english"""
    # =============== Ukraine
    if place == "україна":
        return "ukraine"
    elif place == "countries":
        return "countries"
    elif place == "Львів":
        return "Lviv"
    elif place == "Сімферополь":
        return "Simferopol"
    elif place == "Луганськ":
        return "Luhansk"
    elif place == "Донецьк":
        return "Donetsk"
    elif place == "Чернігів":
        return "Chernihiv"
    elif place == "Херсон":
        return "Kherson"
    elif place == "Миколаїв":
        return "Mykolaiv"
    elif place == "Івано-Франківськ":
        return "Ivano-Frankivsk"
    elif place == "Київ":
        return "Kyiv"
    elif place == "Тернопіль":
        return "Ternopil"
    elif place == "Рівне":
        return "Rivne"
    elif place == "Луцьк":
        return "Lutsk"
    elif place == "Одеса":
        return "Odessa"
    elif place == "Запоріжжя":
        return "Zaporizhzhya"
    elif place == "Суми":
        return "Sumy"
    elif place == "Дніпро":
        return "Dnipro"
    elif place == "Кропивницький":
        return "Kropyvnytskyi"
    elif place == "Вінниця":
        return "Vinnytsia"
    elif place == "Харків":
        return "Kharkiv"
    elif place == "Хмельницький":
        return "Khmelnytsky"
    elif place == "Чернівці":
        return "Chernivtsi"
    elif place == "Житомир":
        return "Zhytomyr"
    elif place == "Черкаси":
        return "Cherkasy"
    elif place == "Полтава":
        return "Poltava"
    elif place == "Ужгород":
        return "Uzhhorod"
    # =======================