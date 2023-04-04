import requests

def create_trello_card(idea, board_id, list_id, config):
    trello_api_key = config.get('API_KEYS', 'TRELLO_API_KEY')
    trello_api_secret = config.get('API_KEYS', 'TRELLO_API_SECRET')

    url = f"https://api.trello.com/1/cards?key={trello_api_key}&token={trello_api_secret}"

    query = {
        "idList": list_id,
        "name": idea,
        "desc": f"Generated idea: {idea}",
    }

    response = requests.request("POST", url, params=query)
    if response.status_code == 200:
        print(f"Card created with idea: {idea}")
    else:
        print("Error creating Trello card")