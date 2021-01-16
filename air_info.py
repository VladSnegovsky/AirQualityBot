import json
#
# # composes a message
# def compose_a_message(answer):
#     answer = answer["data"]
#     aqi = answer["aqi"]
#     if aqi <= 50:
#         return "AQI is <b>" + str (aqi) + "</b>🌡\n\n" \
#                "🟢 <b>Good</b> 🟢\n" \
#                "Air quality is considered satisfactory, and air pollution poses little or no risk."
#     elif 51 <= aqi <= 100:
#         return "AQI is <b>" + str (aqi) + "</b>🌡\n\n" \
#                "🟡 <b>Moderate</b> 🟢\n" \
#                "Air quality is acceptable. However, for some pollutants there may be a moderate health " \
#                     "concern for a very small number of people who are unusually sensitive to air pollution.\n\n" \
#                "Active children and adults, and people with respiratory disease, such as asthma, should " \
#                     "limit prolonged outdoor exertion."
#     elif 101 <= aqi <= 150:
#         return "AQI is <b>" + str (aqi) + "</b>🌡\n\n" \
#                "🟡 <b>Unhealthy for Sensitive Groups</b> 🟡\n" \
#                "Members of sensitive groups may experience health effects. The general public is " \
#                     "not likely to be affected.\n\n" \
#                "Active children and adults, and people with respiratory disease, such as asthma, " \
#                     "should limit prolonged outdoor exertion."
#     elif 151 <= aqi <= 200:
#         return "AQI is <b>" + str (aqi) + "</b>🌡\n\n" \
#                "🟠 <b>Unhealthy</b> 🟠\n" \
#                "Everyone may begin to experience health effects; members of sensitive " \
#                     "groups may experience more serious health effects.\n\n" \
#                "Active children and adults, and people with respiratory disease, " \
#                     "such as asthma, should avoid prolonged outdoor exertion. Everyone else, " \
#                     "especially children, should limit prolonged outdoor exertion."
#     elif 201 <= aqi <= 300:
#         return "AQI is <b>" + str (aqi) + "</b>🌡\n\n" \
#                "🟠 <b>Very Unhealthy</b> 🔴\n" \
#                "Health warnings of emergency conditions. The entire population is " \
#                "more likely to be affected.\n\n" \
#                "Active children and adults, and people with respiratory disease, such as " \
#                "asthma, should avoid all outdoor exertion. Everyone else, especially " \
#                "children, should limit outdoor exertion."
#     elif 301 <= aqi:
#         return "AQI is <b>" + str (aqi) + "</b>🌡\n\n" \
#                "🔴 <b>Hazardous</b> 🔴\n" \
#                "Health alert: everyone may experience more serious health effects.\n\n" \
#                "Everyone should avoid all outdoor exertion."
#
#
# # returns message
# def create_answer(response):
#     answer = json.loads(response.text)
#     if answer["status"] == "ok":
#         return compose_a_message(answer)
#     else:
#         return "Sorry😔! There are no stations yet🗿🗿🗿. Try to use🤔 your location to find the nearest one."
#
# # composes warning message
# def create_answer_warning(response, name):
#     answer = json.loads(response.text)
#     answer_temp = answer["data"]
#     aqi = answer_temp["aqi"]
#     if aqi <= 50:
#         return "🟢 🔼Warning🔼 🟢\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" + compose_a_message(answer)
#     elif 51 <= aqi <= 100:
#         return "🟡 🔼Warning🔼 🟢\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" + compose_a_message(answer)
#     elif 101 <= aqi <= 150:
#         return "🟡 🔼Warning🔼 🟡\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" + compose_a_message(answer)
#     elif 151 <= aqi <= 200:
#         return "🟠 🔼Warning🔼 🟠\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" + compose_a_message(answer)
#     elif 201 <= aqi <= 300:
#         return "🟠 🔼Warning🔼 🔴\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" + compose_a_message(answer)
#     elif 301 <= aqi:
#         return "🔴 🔼Warning🔼 🔴\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> has risen!\n\n" + compose_a_message(answer)
#
#
# # composes "normalized" message
# def create_answer_normalized(response, name):
#     answer = json.loads(response.text)
#     answer_temp = answer["data"]
#     aqi = answer_temp["aqi"]
#     if aqi <= 50:
#         return "🟢 🔽Notification🔽 🟢\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> normalized!\n\n" + compose_a_message(answer)
#     elif 51 <= aqi <= 100:
#         return "🟡 🔽Notification🔽 🟢\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" + compose_a_message(answer)
#     elif 101 <= aqi <= 150:
#         return "🟡 🔽Notification🔽 🟡\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" + compose_a_message(answer)
#     elif 151 <= aqi <= 200:
#         return "🟠 🔽Notification🔽 🟠\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" + compose_a_message(answer)
#     elif 201 <= aqi <= 300:
#         return "🟠 🔽Notification🔽 🔴\n\n" \
#                "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" + compose_a_message(answer)
#     elif 301 <= aqi:
#         return "🔴 🔽Notification🔽 🔴\n\n" \
#                 "Air Quality Level at the location <i><b>" + name + "</b></i> fell!\n\n" + compose_a_message(answer)


def get_aqi(response):
    answer = json.loads(response.text)
    answer = answer["data"]
    return answer["aqi"]

# returns idx
def get_idx(response):
    answer = json.loads(response.text)
    if answer["status"] == "ok":
        answer = answer["data"]
        return answer["idx"]
    else:
        return "ERROR"

# returns city and country
def get_city_country(response):
    temp_answer = json.loads(response.text)
    if temp_answer["status"] == "ok":
        temp_answer = temp_answer["data"]
        temp_answer = temp_answer["city"]
        temp_answer = temp_answer["name"]
        temp_str = str (temp_answer)
        answer = ""
        for i in temp_str:
            if i != "(":
                answer += i
            elif i == "(":
                return answer.strip()

            if i == temp_str[-1]:
                return answer.strip()
    else :
        return "ERROR"