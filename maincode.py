import requests

api_key = "AIzaSyD0SaQFY3kTFagLAV5uPxMzeUbZwLtsY6M"
search_engine_id = "e31bbb8afd1104758m"

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" not in data:
        print("literally 1984, cant find anything")
        return

    print("\nHere are some results that i was able to find:\n")
    for item in data["items"][:5]: 
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        print(f"Snippet: {item['snippet']}\n")



print("hi what is your name?")
print("hi " + input() + " nice yo meet you")
print("do you need help in something? " + "go ahead and tell me!!!")
help = input()

if help == "yes":
    print("alright what do you need help in?")
    help_response = input()
    if help_response == "search":
        query = input("What do you want me to search for?")
        print("hope this helps gng")
        google_search(query)
    else:
        print("sorry that isnt a command, you prob got it wrong")
else:
    print("alright then have a great day")

