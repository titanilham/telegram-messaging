import requests

TOKEN = "********************************"
CHAT_ID = "*************"

def send_msg(text: str, token: str, chat_id: str ) -> None:
   
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

if __name__ == "__main__":
    send_msg("HI", TOKEN, CHAT_ID)
