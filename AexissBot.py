import requests


def send_msg(text):
    token = "**************************"
    chat_id = "**********"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


send_msg("HI")