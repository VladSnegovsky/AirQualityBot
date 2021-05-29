import logging
import json
import requests
from aiogram import Bot, Dispatcher, executor, types
from DataBase import PostgreSQLDataBase
import asyncio
import time
import schedule
from telegram import ParseMode
import datetime

# import languages as lang
import config
import keyboard as kb
import air_info as air_info
import status_hash as status


logging.basicConfig(level=logging.INFO)

# Initialize Bot
bot = Bot(token=config.API_TG_BOT_TOKEN)
dp = Dispatcher(bot)

# Initialize connection with db
import os
import psycopg2

db = PostgreSQLDataBase()

# Languages
import english as eng
import ukrainian as ukr
language = eng


# =================== Notifications
async def send_notification(user_id, item):
    if item[4] == 1:
        response = get_response_by_idx_for_shedule(item[0])
        answer = json.loads(response.text)
        answer = answer["data"]
        new_aqi = answer["aqi"]
        if new_aqi >= item[2] + item[3]:
            _idx = air_info.get_idx(response)
            location = get_location_info_db_idx(user_id, _idx)
            update_last_aqi(user_id, item[0], new_aqi)
            message_notification = language.create_answer_warning(response, location[0][1])
            await bot.send_message(user_id, message_notification, parse_mode=ParseMode.HTML, disable_notification=False)
        elif new_aqi <= item[2] - item[3]:
            _idx = air_info.get_idx(response)
            location = get_location_info_db_idx(user_id, _idx)
            update_last_aqi(user_id, item[0], new_aqi)
            message_notification = language.create_answer_normalized(response, location[0][1])
            await bot.send_message(user_id, message_notification, parse_mode=ParseMode.HTML, disable_notification=False)


async def scheduled():
    while True:
        await asyncio.sleep(20)
        now = datetime.datetime.now()
        if now.minute == 0:
            users = db.get_all_users()
            for user in range(len(users)):
                locations = db.get_all_locations(int(users[user][1]))
                for item in locations:
                    await send_notification(int(users[user][1]), item)


# =================== First Bot Message
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    change_status("Choose language")
    await message.answer("Hi! Before start, p󠁥󠁿lease, choose language. 🇬🇧\n"
                         "Привіт! Перед початком, будь ласка, обери мову. 🇺🇦 ", reply_markup=kb.keyboard_languages)


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.answer(language.msg_instructions(), parse_mode=ParseMode.HTML)


# =================== Last Hash
last_status = ""

def change_status(new_message):
    global last_status
    last_status = status.get_hash(new_message)


# =================== New Name
new_name_str = "empty"
str_no_conflict = False
temp_old_name = ""


# =================== New Step
new_step = 0


# =================== Current response
global_response = requests
idx = 0


# =================== Functions
# Update Last Aqi
def update_last_aqi(user_id, _idx, new_aqi):
    db.update_last_aqi(user_id, _idx, new_aqi)

# Delete Location
def delete_location(message):
    global idx
    db.delete_location(message.from_user.id, idx)

# Update Notifications
def update_notifications(message, status):
    global idx
    db.update_notifications(message.from_user.id, idx, status)

# Update Step
def update_step(message):
    global idx
    global new_step
    db.update_step(message.from_user.id, idx, new_step)

# Update Name
def update_location_name(message, new_name):
    global idx
    db.update_name(message.from_user.id, idx, new_name)

# Get Name from User
async def get_name(message):
    new_name_str_temp = message.text
    global new_name_str

    if new_name_str_temp == "":
        new_name_str = ""
    elif len(new_name_str_temp) > 50:
        await message.answer(language.msg_maximum_length_50(), reply_markup=kb.change_cancel(language), parse_mode=ParseMode.HTML)
    else:
        new_name_str = new_name_str_temp.strip()

# Create Name for location
def create_name(message, name):
    i = 0
    name = name.strip()
    temp_name = name
    while db.name_exists(message.from_user.id, temp_name):
        i += 1
        temp_name = name + " (" + str (i) + ")"
    return temp_name

# Check if name already exists
def check_name_db(message, name):
    return db.name_exists(message.from_user.id, name)

# Check if the location already exists
def check_location_exists(message, _idx):
    return db.location_exists(message.from_user.id, _idx)

# Gets location by idx
def get_location_info_db_idx(user_id, _idx):
    return db.get_location_info_idx(user_id, _idx)

# Gets location by name
def get_location_info_db_name(message, _name):
    return db.get_location_info_name(message.from_user.id, _name)

# Returns message with all locations
def show_all_locations(message):
    change_status("My Locations")
    locations = db.get_all_locations(message.from_user.id)
    empty = True
    locations_db = []
    for item in locations:
        locations_db.append(item[1])
        empty = False
    if not empty:
        kb.checkout_locations_db = locations_db
        return language.msg_your_locations()
    else:
        return language.msg_you_have_no_locations()

def string_in_array_strip(string, array):
    result = False
    for item in array:
        if string == item.strip():
            result = True
    return result


# =================== Response from API
def get_response_by_idx_for_shedule(_idx):
    return requests.get("https://api.waqi.info/feed/@" + str (_idx) + "/?token=" + config.API_AIR_TOKEN)

def get_response_by_idx(_idx):
    global global_response
    global_response = requests.get("https://api.waqi.info/feed/@" + str (_idx) + "/?token=" + config.API_AIR_TOKEN)
    return global_response

def get_response_by_location(_latitude, _longitude):
    global global_response
    print(_latitude)
    print(_longitude)
    print("https://api.waqi.info/feed/geo:" + _latitude + ";" + _longitude + "/?token=" + config.API_AIR_TOKEN)
    global_response = requests.get("https://api.waqi.info/feed/geo:" + _latitude + ";" + _longitude + "/?token=" + config.API_AIR_TOKEN)
    return global_response

def get_response_by_city(_name):
    global global_response
    global_response = requests.get("https://api.waqi.info/feed/" + _name + "/?token=" + config.API_AIR_TOKEN)
    return global_response

# === temp
# =================== Messages
# After pushing ...
# First Message after choosing language
async def say_hi_to_user(message):
    await message.answer(language.msg_hi_message(), parse_mode=ParseMode.HTML)
    change_status("Instructions")
    await message.answer(language.msg_instructions() + language.msg_about_help(), reply_markup=kb.ok_i_read_it(language), parse_mode=ParseMode.HTML)

# Main Menu
# hash "Main"
async def msg_main(message):
    change_status("Main")
    await message.answer(language.msg_main_message(), reply_markup=kb.main(language))
    # await message.answer("Choose what you want to do.", reply_markup=kb.kb_main(eng))

# Change Language
# hash "Change language"
async def msg_change_language(message):
    change_status("Change language")
    await message.answer(language.msg_change_language(), reply_markup=kb.new_language(language))

# Select New Location
# hash "Select new location"
async def msg_select_new_location(message):
    change_status("Select new location")
    await message.answer(language.msg_choose_list_or_location(), reply_markup=kb.add_location(language))
    await message.answer(language.msg_geolocation_is_not_available())

# Select from list
# hash "Select from list"
async def msg_select_from_list(message):
    change_status("Select from list")
    await message.answer(language.msg_list_of_countries(), reply_markup=kb.generate_keyboard("countries", language))

# Add location
# hash "Add new location"
async def msg_add_location(message):
    change_status("Add new location")
    await message.answer(language.msg_do_you_want_to_add_this_location(), reply_markup=kb.yes_no_loc(language))

# Get notification
# hash "Get notification"
async def msg_get_notification(message):
    change_status("Get notification")
    await message.answer(language.msg_do_you_want_to_be_notified(), reply_markup=kb.yes_no(language))


# Enter location name
# hash "Enter location name"
async def msg_enter_location_name(message):
    await message.answer(language.msg_send_me_new_name_add())
    # await message.answer("Send me new name for this location😁 and then click Add.")
    change_status("Enter location name")
    global global_response
    global new_name_str
    new_name_str = create_name(message, air_info.get_city_country(global_response))
    await message.answer(language.msg_if_you_will_not_send_it(new_name_str), parse_mode=ParseMode.HTML, reply_markup=kb.add(language))

async def get_location_name(message):
    global new_name_str
    global str_no_conflict
    new_name_str_temp = message.text
    if len(new_name_str_temp) > 50:
        await message.answer(language.msg_maximum_length_50(), reply_markup=kb.add(language))
    elif check_name_db(message, new_name_str_temp):
        await message.answer(language.msg_such_name_is_already_exists())
    else:
        if new_name_str_temp == language.button_add:
            str_no_conflict = True
        else:
            new_name_str = new_name_str_temp
            str_no_conflict = True

# My locations
# hash "My Locations"
async def msg_my_locations(message):
    change_status("My Locations")
    temp_message = show_all_locations(message)
    if temp_message != language.msg_you_have_no_locations():
        await message.answer(temp_message, reply_markup=kb.generate_keyboard_locations_db(language))
    else:
        await message.answer(temp_message)
        await msg_main(message)

#Location settings
#hash "Location Settings"
async def msg_location_settings(message, _name):
    global idx
    idx = 0
    change_status("Location Settings")
    temp_location = get_location_info_db_name(message, str(_name))
    idx = temp_location[0][0]
    temp_response = get_response_by_idx(idx)
    update_last_aqi(message.from_user.id, air_info.get_idx(temp_response), air_info.get_aqi(temp_response))
    if temp_location[0][4] == 1:
        await message.answer(language.create_answer(temp_response), parse_mode=ParseMode.HTML,
                             reply_markup=kb.generate_location_settings_keyboard(True, language))
    else:
        await message.answer(language.create_answer(temp_response), parse_mode=ParseMode.HTML,
                             reply_markup=kb.generate_location_settings_keyboard(False, language))
    await message.answer(language.msg_you_step_for_this_location_is(temp_location[0][3]))



# =================== Text Handler
@dp.message_handler(content_types=["text"])
async def answered(message):
    global global_response
    global new_name_str
    global str_no_conflict
    global idx
    global temp_old_name
    global new_step
    global language
    global last_status

    # ================================================================= Back ====================
    if message.text == language.button_back_to_menu:
        await msg_main(message)
    elif last_status == language.button_back_to_menu:
        await msg_main(message)
    elif message.text == language.button_back_to_menu:
        await msg_main(message)
    elif message.text == language.button_back_to_select:
        await msg_select_new_location(message)
    elif message.text == language.button_back_to_select:
        await msg_select_from_list(message)
    elif message.text == language.button_back_to_locations:
        await msg_my_locations(message)
    # ===========================================================================================

    # ================================================================= Ok ======================
    if message.text == language.button_ok_i_read_it:
        await msg_main(message)
    # ===========================================================================================

    # ================================================================= Select new location =====
    elif message.text == language.button_select_location:
        await msg_select_new_location(message)
    # ===========================================================================================

    # ================================================================= Countries ===============
    # Countries List
    elif message.text == language.button_select_from_list:
        await msg_select_from_list(message)

    # Cities List
    elif string_in_array_strip(message.text, kb.checkout_countries_array):
        kb.checkout_countries_array.clear()
        await message.answer(language.msg_choose_a_city(), reply_markup=kb.generate_keyboard(message.text, language))

    # Info
    elif string_in_array_strip(message.text, kb.checkout_cities_array):
        temp_response = get_response_by_city(message.text)
        if language.create_answer(temp_response) != language.msg_no_stations():
            if check_location_exists(message, air_info.get_idx(temp_response)):
                await message.answer(language.create_answer(temp_response), parse_mode=ParseMode.HTML)
                await message.answer(language.msg_you_have_this_location(get_location_info_db_idx(message.from_user.id, air_info.get_idx(temp_response))[0][1]), parse_mode=ParseMode.HTML)
                answer = json.loads(temp_response.text)
                answer = answer["data"]
                new_aqi = answer["aqi"]
                update_last_aqi(message.from_user.id, air_info.get_idx(temp_response), new_aqi)
                kb.checkout_cities_array.clear()
                await msg_main(message)
            else:
                await message.answer(language.create_answer(temp_response), parse_mode=ParseMode.HTML)
                new_name_str = air_info.get_city_country(temp_response)
                idx = air_info.get_idx(temp_response)
                kb.checkout_cities_array.clear()
                global_response = temp_response
                await msg_add_location(message)
            kb.checkout_cities_array.clear()
        else:
            await message.answer(language.create_answer(temp_response))
            kb.checkout_cities_array.clear()
            await msg_select_new_location(message)
        kb.checkout_cities_array.clear()
    # ===========================================================================================

    # ================================================================= Yes/No ==================
    # No
    elif message.text == language.button_no_loc:
        await msg_main(message)

    elif message.text == language.button_no:
        _idx = air_info.get_idx(global_response)
        _last_aqi = air_info.get_aqi(global_response)
        db.add_location(message.from_user.id, _idx, new_name_str, _last_aqi, False)
        await msg_main(message)

    # Yes
    elif message.text == language.button_yes_loc:
        await msg_enter_location_name(message)

    elif message.text == language.button_yes:
        _idx = air_info.get_idx(global_response)
        _last_aqi = air_info.get_aqi(global_response)
        _last_aqi = air_info.get_aqi(global_response)
        db.add_location(message.from_user.id, _idx, new_name_str, _last_aqi, True)
        await msg_main(message)
    # ===========================================================================================

    # ================================================================= My locations ============
    elif message.text == language.button_my_locations:
        await msg_my_locations(message)

    elif string_in_array_strip(message.text, kb.checkout_locations_db):
        temp_old_name = message.text
        new_name_str = temp_old_name
        await msg_location_settings(message, message.text)

    elif message.text == language.button_edit_name:
        last_status = status.get_hash("Enter location name")
        await message.answer(language.msg_write_new_name_change(), reply_markup=kb.change_cancel(language))

    elif message.text == language.button_edit_step:
        last_status = status.get_hash("Edit Step")
        await message.answer(language.msg_select_new_step(), reply_markup=kb.step(language))

    elif message.text == language.button_notifications_on:
        update_notifications(message, True)
        await msg_location_settings(message, new_name_str)

    elif message.text == language.button_notifications_off:
        update_notifications(message, False)
        await msg_location_settings(message, new_name_str)

    elif message.text == language.button_delete_location:
        delete_location(message)
        idx = 0
        temp_old_name = ""
        new_name_str = ""
        new_step = 0
        await msg_my_locations(message)
    # ===========================================================================================

    # ================================================================= Change ==================
    elif message.text == language.button_change:
        if new_name_str == "":
            new_name_str = temp_old_name
            await msg_location_settings(message, temp_old_name)
        else:
            update_location_name(message, new_name_str)
            await msg_location_settings(message, new_name_str)

    elif message.text == language.button_change_step:
        update_step(message)
        await msg_location_settings(message, new_name_str)

    # ===========================================================================================

    # ================================================================= Cancel ==================
    elif message.text == language.button_cancel:
        new_name_str = temp_old_name
        await msg_location_settings(message, temp_old_name)

    elif message.text == language.button_cancel_step:
        await msg_location_settings(message, new_name_str)
    # ===========================================================================================

    # ================================================================= Add =====================
    elif message.text == language.button_add:
        if not str_no_conflict:
            await get_location_name(message)
        await message.answer(language.msg_here_is_the_name(new_name_str), parse_mode=ParseMode.HTML)
        await msg_get_notification(message)
    # ===========================================================================================

    # ================================================================= About this Bot ==========
    elif message.text == language.button_about_this_bot:
        await message.answer(language.msg_about_this_bot(), parse_mode=ParseMode.HTML)
        await msg_main(message)
    # ===========================================================================================

    # ================================================================= Settings ================
    elif message.text == language.button_settings:
        last_status = status.get_hash("Change language")
        await msg_change_language(message)
    # ===========================================================================================

    # ================================================================= Other ===================
    else:
        if last_status == status.get_hash("Enter location name"):
            await get_location_name(message)

        elif last_status == status.get_hash("Choose language"):
            if message.text == "Українська":
                language = ukr
                await say_hi_to_user(message)
            if message.text == "English󠁧󠁢󠁥󠁮󠁧󠁿":
                language = eng
                await say_hi_to_user(message)

        elif last_status == status.get_hash("Change language"):
            if message.text == "Українська":
                language = ukr
                await msg_main(message)
            if message.text == "English":
                language = eng
                await msg_main(message)

        elif last_status == status.get_hash("Edit Name"):
            await get_name(message)

        elif last_status == status.get_hash("Edit Step"):
            if message.text == "10":
                new_step = 10
            elif message.text == "15":
                new_step = 15
            elif message.text == "20":
                new_step = 20
            elif message.text == "25":
                new_step = 25
            elif message.text == "30":
                new_step = 30
            elif message.text == "35":
                new_step = 35
            elif message.text == "40":
                new_step = 40
            elif message.text == "45":
                new_step = 45
            elif message.text == "50":
                new_step = 50
    # ===========================================================================================


# =================== Location Handler
@dp.message_handler(content_types=['location'])
async def check_loc(message):
    global global_response
    global new_name_str
    global idx
    temp_response = get_response_by_location(str(message.location.latitude), str(message.location.longitude))
    global_response = temp_response
    new_name_str = air_info.get_city_country(temp_response)
    idx = air_info.get_idx(temp_response)
    await message.answer(language.create_answer(temp_response), parse_mode=ParseMode.HTML)
    if check_location_exists(message, air_info.get_idx(temp_response)):
        await message.answer(language.msg_you_have_this_location(get_location_info_db_idx(message.from_user.id, air_info.get_idx(temp_response))[0][1]), parse_mode=ParseMode.HTML)
        answer = json.loads(temp_response.text)
        answer = answer["data"]
        new_aqi = answer["aqi"]
        update_last_aqi(message.from_user.id, language.get_idx(temp_response), new_aqi)
        kb.checkout_cities_array.clear()
        await msg_main(message)
    else:
        await msg_add_location(message)




# =================== Long Polling
if __name__ == '__main__':
    task = asyncio.ensure_future(scheduled())
    task
    executor.start_polling(dp, skip_updates=True)