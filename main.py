import requests   
# pip install requests


query = input("what type of news are u interested in today ?")
api = "0ab6974e00fa4a658cac84dc45450b76"

#  0ab6974e00fa4a658cac84dc45450b76 = my api key from news API

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-09-24&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()  #the json content is we have it as a dictionay in our python

articles = data["articles"]

for index ,a in enumerate(articles):
    print( index+1 ,a["title"], a["url"])
    print("\n******************\n")
