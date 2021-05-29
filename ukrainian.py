from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json

# Messages
def msg_hi_message():
    return "Привіт! Мене звати Airo🤖, і я можу показати тобі рівень якості повітря☁️ у будь-якому "\
           "місці🗺."

def msg_about_help():
    return "\n\nТакож ти можешь подивитись цю інструкцію коли захочешь надіславши боту /help."

def msg_maximum_length_50():
    return "❗️Максимальна довжина імені 5️⃣0️⃣. Напиши нове."

def msg_your_locations():
    return "Ось твої локації😎. Натисни на одну📍 щоб отримати інформаціюℹ️.\nТи " \
           "також можеш її редагувати🧐."

def msg_you_have_no_locations():
    return "У тебе немає локацій😞."

def msg_main_message():
    return "Обери що хочеш зробити."

def msg_choose_list_or_location():
    return "Oк🙂. Зараз ти можеш обрати - шукати за місцезнаходженням📍 чи вибрати зі списку 📃."

def msg_geolocation_is_not_available():
    return "До речі🤔, геолокація на десктопній🖥 версії телеграма недоступна😔."

def msg_list_of_countries():
    return "Ось список країн🇬🇧🇩🇪. Обери потрібну🧐."

def msg_do_you_want_to_add_this_location():
    return "Чи хочеш ти додати цю локацію📍 до твого списку📄? Ти будеш повідомлений(-на) " \
           "якщо рівень🌡 забруднення повітря💨 збільшиться⚠️."

def msg_do_you_want_to_be_notified():
    return "Чи хочеш🤓 ти отримувати сповіщення про стан повітря💨 коли він змінюється😧?"

def msg_send_me_new_name_add():
    return "Надішли мені назву😁 та натисни Додати."

def msg_if_you_will_not_send_it(name):
    return "Якщо ти не надішлеш📨 його та натиснеш <i>Додати</i>, назва буде <i><b>" \
           + name + "</b></i>."

def msg_such_name_is_already_exists():
    return "Така назва вже є🙄."

def msg_you_step_for_this_location_is(step):
    return "Крок для цієї локації " + str(step) + "."

def msg_choose_a_city():
    return "Тепер обери місто🏙 про яке хочеш дізнатися🤔."

def msg_no_stations():
    return "Вибач😔! Тут станцій ще немає🗿🗿🗿. Спробуй використати🤔 твоє місцезнаходження щоб знайти найближчу."

def msg_you_have_this_location(name):
    return "До речі💁‍♂️, ти вже маєш цю локацію <i><b>" + name + "</b></i>."

def msg_write_new_name_change():
    return "Напиши✍️ нову назву для цієї локації📍 та натисни🖱 змінити."

def msg_select_new_step():
    return "Обери новий крок на клавіатурі⌨️."

def msg_here_is_the_name(name):
    return "Дякую😃, ось назва для цієї локації - <i><b>" + name + "</b></i>."

def msg_about_this_bot():
    return "Привіт! Мене звати Влад.\n\nЯ зробив цього бота як курсову роботу, яку після" \
           "завершення, я запустив на сервері для постійної роботи.Він написаний на мові " \
           "програмування Python та використовую API(Application Program Interface) для " \
           "отримання інформації про стан повітря.\n\nЯкщо ти виявиш помилку," \
           "або маєш якісь пропозиції, то можеш написати мені @snegovskyvlad. Також ти " \
           "можешь подивитись інструкцію по його використанню надіславши боту /help.\n\n" \
           "Дякую за використання цього бота."

def msg_change_language():
    return "Буль ласка, обери мову."

def msg_instructions():
    return "🔘 Ти можеш добавити нову локацію натиснувши <i><b>Обрати нове місце</b></i>. Там " \
           "буде дві кнопки - <i><b>Моє місцезнаходження</b></i> and <i><b>Обрати зі списку" \
           "</b></i>. Якщо ти хочеш щоб бот сам знайшов найюлижчу станцію до тебе - натисни першу," \
           "інакше обирай другу кнопку. \nЯкщо ти вибереш <i><b>Обрати зі списку</b></i>, там " \
           "ти побачиш список країн - обирай потрібну. Потім обирай місто.\nПісля того як ти" \
           " обрав(-ла) потрібне місто чи відправив(-ла) своє місцезнаходження, бот запитає тебе" \
           " чи не хочеш ти зберегти цю локацію. Відповідай як хочеш.\nЯкщо ти відповів(-ла) Так, " \
           "бот попросить обрати назву для нової локації. Ти можеш відправити(треба обов'язково відправити" \
           " назву, не тільки набрати) і натиснути <i><b>Додати</b></i>. Потім обери чи хочешь ти" \
           "отримувати повідомлення про зміну стану рівня повітря.\n\n🔘 Якщо ти натиснеш <i><b>Мої " \
           "локації</b></i>, ти побачиш список всіх локацій що ти зберіг(-ла) або бот повідомить що їх " \
           "немає. Якщо в тебе є хоча б одна локація, ти можешь натиснути на неї та отримати поточну " \
           "інформацію про неї. Подивись на клавіатуру, там ти побачиш Налаштування цієї локації." \
           " Ти можеш змінити:\n   Назву: натисни на <i><b>Редагувати Ім'я</b></i>✍️ та надішли" \
           "(обов'язково відправити, не тільки набрати) нову назву боту, потім натисни <i><b>Змінити</b>" \
           "</i>.\n   Крок: спочатку, ти повинен(-нна) знати що Рівень Якості Повітря вимірюється в змінних " \
           "AQI - це число яке ти будеш бачити в Інформаційних Повідомлення від бота. Крок - це число" \
           " на яке повинне змінитися AQI щоб ти отримав(-ла) повідомлення. Щоб його змінити - натисни " \
           "<i><b>Редагувати Крок</b></i>✍️, обери новий Крок на клавіатурі і тільки потім натисни <i><b>" \
           "Змінити</b></i>.\n   Повідомлення: щоб ВИКЛ/ВКЛ повідомлення натисни <i><b>Повідомлення Викл" \
           "</b></i>🔕/<i><b>Повідомлення Вкл</b></i>🔔.\n   Щоб видалити локацію - натисни <i><b>Видалити " \
           "Локацію</b></i>🗑.\n\n🔘 У <i><b>Про бота</b></i> ти дізнаєшься відповідну інформацію." \
           "\n\n🔘 У <i><b>Налаштування</b></i>⚙️ ти можешь змінити мову.\n\n\nЯкщо ти виявиш помилку, " \
           "або маєш якісь пропозиції, то можеш написати мені @snegovskyvlad."

# Answer
def compose_a_message(answer):
    """composes answer"""
    answer = answer["data"]
    aqi = answer["aqi"]
    if aqi <= 50:
        return "AQI = <b>" + str(aqi) + "</b>🌡\n\n" \
                                        "🟢 <b>Добре</b> 🟢\n" \
                                        "Якість повітря вважається задовільною, а забруднення повітря становить невеликий ризик або взагалі його не становить."
    elif 51 <= aqi <= 100:
        return "AQI = <b>" + str(aqi) + "</b>🌡\n\n" \
                                        "🟡 <b>Помірний</b> 🟢\n" \
                                        "Якість повітря є прийнятною. Однак деякі забруднюючі речовини можуть " \
                                        "турбувати здоров’я дуже невеликої кількості людей, які надзвичайно чутливі до забруднення " \
                                        "повітря.\n\n" \
                                        "Активні діти та дорослі, а також люди з респіраторними захворюваннями, такими як астма, повинні обмежувати тривалі навантаження на вулиці."
    elif 101 <= aqi <= 150:
        return "AQI = <b>" + str(aqi) + "</b>🌡\n\n" \
                                        "🟡 <b>Шкідливий для чутливих груп</b> 🟡\n" \
                                        "Члени чутливих груп можуть відчувати наслідки для здоров'я. " \
                                        "Населення, швидше за все, не постраждає.\n\n" \
                                        "Активні діти та дорослі, а також люди з респіраторними захворюваннями, такими як астма, повинні обмежувати тривалі навантаження на вулиці."
    elif 151 <= aqi <= 200:
        return "AQI = <b>" + str(aqi) + "</b>🌡\n\n" \
                                        "🟠 <b>Шкідливо</b> 🟠\n" \
                                        "Кожна людина може почати відчувати наслідки для здоров’я. " \
                                        "Члени чутливих груп можуть відчувати більш серйозні наслідки для здоров'я.\n\n" \
                                        "Активні діти та дорослі, а також люди з респіраторними захворюваннями, " \
                                        "таких як астма, слід уникати навантажень на відкритому повітрі. " \
                                        "Всім іншим слід обмежити тривалі навантаження на вулиці."
    elif 201 <= aqi <= 300:
        return "AQI = <b>" + str(aqi) + "</b>🌡\n\n" \
                                        "🟠 <b>Дуже шкідливо</b> 🔴\n" \
                                        "Попередження про надзвичайні умови. Все населення, " \
                                        "швидше за все, постраждає.\n\n" \
                                        "Активні діти та дорослі, а також люди з респіраторними захворюваннями, такі як " \
                                        "астми, слід уникати будь-яких навантажень на вулиці. Усі інші, особливо " \
                                        "дітям, слід обмежити навантаження на вулиці."
    elif 301 <= aqi:
        return "AQI = <b>" + str(aqi) + "</b>🌡\n\n" \
                                        "🔴 <b>Небезпечно</b> 🔴\n" \
                                        "Попередження про стан здоров’я: кожен може відчувати більш серйозні наслідки для здоров’я.\n\n" \
                                        "Кожен повинен уникати будь-яких навантажень на вулиці."


def create_answer(response):
    answer = json.loads(response.text)
    if answer["status"] == "ok":
        return compose_a_message(answer)
    else:
        return "Вибач😔! Тут станцій ще немає🗿🗿🗿. Спробуй використати🤔 твоє місцезнаходження щоб знайти найближчу."


def create_answer_normalized(response, name):
    """composes "normalized" message"""
    answer = json.loads(response.text)
    answer_temp = answer["data"]
    aqi = answer_temp["aqi"]
    if aqi <= 50:
        return "🟢 🔽Повідомлення🔽 🟢\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> нормалізувався!\n\n" \
               + compose_a_message(answer)
    elif 51 <= aqi <= 100:
        return "🟡 🔽Повідомлення🔽 🟢\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> нормалізується!\n\n" \
               + compose_a_message(answer)
    elif 101 <= aqi <= 150:
        return "🟡 🔽Повідомлення🔽 🟡\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> нормалізується!\n\n" \
               + compose_a_message(answer)
    elif 151 <= aqi <= 200:
        return "🟠 🔽Повідомлення🔽 🟠\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> нормалізується!\n\n" \
               + compose_a_message(answer)
    elif 201 <= aqi <= 300:
        return "🟠 🔽Повідомлення🔽 🔴\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> нормалізується!\n\n" \
               + compose_a_message(answer)
    elif 301 <= aqi:
        return "🔴 🔽Повідомлення🔽 🔴\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> нормалізується!\n\n" \
               + compose_a_message(answer)


def create_answer_warning(response, name):
    """composes warning message"""
    answer = json.loads(response.text)
    answer_temp = answer["data"]
    aqi = answer_temp["aqi"]
    if aqi <= 50:
        return "🟢 🔼Попередження🔼 🟢\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> погіршився!\n\n" \
               + compose_a_message(answer)
    elif 51 <= aqi <= 100:
        return "🟡 🔼Попередження🔼 🟢\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> погіршився!\n\n" \
               + compose_a_message(answer)
    elif 101 <= aqi <= 150:
        return "🟡 🔼Попередження🔼 🟡\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> погіршився!\n\n" \
               + compose_a_message(answer)
    elif 151 <= aqi <= 200:
        return "🟠 🔼Попередження🔼 🟠\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> погіршився!\n\n" \
               + compose_a_message(answer)
    elif 201 <= aqi <= 300:
        return "🟠 🔼Попередження🔼 🔴\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> погіршився!\n\n" \
               + compose_a_message(answer)
    elif 301 <= aqi:
        return "🔴 🔼Попередження🔼 🔴\n\n" \
               "Стан якості повітря у локації <i><b>" + name + "</b></i> погіршився!\n\n" \
               + compose_a_message(answer)

# Buttons
button_select_location = "Обрати нове місце"
button_my_locations = "Мої локації"
button_about_this_bot = "Про бота"
button_find_me = "Моє місцезнаходження"
button_select_from_list = "Обрати зі списку"
button_yes = "Так✅"
button_no = "Ні❌"
button_add = "Додати"
button_change = "Змінити"
button_cancel = "Відмінити"
button_edit_name = "Редагувати Ім'я✍️"
button_edit_step = "Редагувати Крок✍️"
button_notifications_on = "Повідомлення Вкл🔔"
button_notifications_off = "Повідомлення Викл🔕"
button_delete_location = "Видалити Локацію🗑"
button_settings = "Налаштування⚙️"
button_ok_i_read_it = "Так, я прочитав(-ла) це."

# Countries
def translate_country(country_eng):
    if country_eng == "Ukraine":
        return "Україна"
    elif country_eng == "countries":
        return "countries"

# Cities
def translate_city(city_eng):
    # =============== Ukraine
    if city_eng == "Lviv":
        return "Львів"
    elif city_eng == "Simferopol":
        return "Сімферополь"
    elif city_eng == "Luhansk":
        return "Луганськ"
    elif city_eng == "Donetsk":
        return "Донецьк"
    elif city_eng == "Chernihiv":
        return "Чернігів"
    elif city_eng == "Kherson":
        return "Херсон"
    elif city_eng == "Mykolaiv":
        return "Миколаїв"
    elif city_eng == "Ivano-Frankivsk":
        return "Івано-Франківськ"
    elif city_eng == "Kyiv":
        return "Київ"
    elif city_eng == "Ternopil":
        return "Тернопіль"
    elif city_eng == "Rivne":
        return "Рівне"
    elif city_eng == "Lutsk":
        return "Луцьк"
    elif city_eng == "Odessa":
        return "Одеса"
    elif city_eng == "Zaporizhzhya":
        return "Запоріжжя"
    elif city_eng == "Sumy":
        return "Суми"
    elif city_eng == "Dnipro":
        return "Дніпро"
    elif city_eng == "Kropyvnytskyi":
        return "Кропивницький"
    elif city_eng == "Vinnytsia":
        return "Вінниця"
    elif city_eng == "Kharkiv":
        return "Харків"
    elif city_eng == "Khmelnytsky":
        return "Хмельницький"
    elif city_eng == "Chernivtsi":
        return "Чернівці"
    elif city_eng == "Zhytomyr":
        return "Житомир"
    elif city_eng == "Cherkasy":
        return "Черкаси"
    elif city_eng == "Poltava":
        return "Полтава"
    elif city_eng == "Uzhhorod":
        return "Ужгород"

button_back_to_select = "↩ Повернутися до вибору місця"
button_back_to_menu = "↩ До меню"
button_back_to_locations = "↩ Повернутися до локацій"
button_change_step = "Змінити Крок"
button_cancel_step = "Відмінити зміну Кроку"
button_yes_loc = "✅Так, додати"
button_no_loc = "❌Ні, не треба"