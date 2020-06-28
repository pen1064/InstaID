import sys, json, os
import requests

def get_id(username):
    url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+username
    userJSON = requests.get(url).json()

    try:
        for i in range(len(userJSON['users'])):
            if userJSON['users'][i].get("user").get("username") == username:
                user_id = str(userJSON['users'][i].get("user").get("pk"))
                return user_id
    except:
        return "Unexpected error"


if __name__ == "__main__":
    user_id = get_id(sys.argv[1])
    print(user_id)
