import json

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