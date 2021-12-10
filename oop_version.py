class Trello:
    def __init__(self,key,token):
        self.key = key
        self.token = token

    def getBoardDescription(self, board_id):
        import requests
        import json

        url = "https://api.trello.com/1/boards/" + str(board_id)

        headers = {"Accept": "application/json"}

        query = {
            'key': self.key,
            'token': self.token
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        res = json.loads(response.text)

        return res

    def getAllListOnABoard(self,board_id):
        import requests
        import json

        url = "https://api.trello.com/1/boards/" + str(board_id) + "/lists"
        headers = {"Accept": "application/json"}

        query = {
            'key': self.key,
            'token': self.token
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        res = json.loads(response.text)

        return res

    def getAllCardsOnAList(self,list_id):
        import requests
        import json

        url = "https://api.trello.com/1/lists/" + str(list_id) + "/cards"

        headers = {"Accept": "application/json"}

        query = {
            'key': self.key,
            'token': self.token
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        res = json.loads(response.text)

        return res

    def getAllChecklistOnACard(self, card_id):
        import requests
        import json

        url = "https://api.trello.com/1/cards/" + str(card_id) + "/checklists"

        headers = {"Accept": "application/json"}

        query = {
            'key': self.key,
            'token': self.token
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        res = json.loads(response.text)

        return res

    def getCardsInformation(self, card_id):
        import requests
        import json

        url = "https://api.trello.com/1/cards/" + str(card_id)

        headers = {"Accept": "application/json"}

        query = {
            'key': self.key,
            'token': self.token
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        res = json.loads(response.text)

        return res
