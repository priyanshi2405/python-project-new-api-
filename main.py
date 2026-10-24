import requests   
# pip install requests


query = "artificial intellegence"
api = "0ab6974e00fa4a658cac84dc45450b76"

#  0ab6974e00fa4a658cac84dc45450b76 = my api key from news API

url = f"https://newsapi.org/v2/everything?q=query&from=2026-09-24&sortBy=publishedAt&apiKey=0ab6974e00fa4a658cac84dc45450b76"

print(url)

r = requests.get(url)

data = r.json()  #the json content is we have it as a dictionay in our python

articles = data["articles"]

for a in articles:
    print(a["title"], a["url"])
    print("\n******************\n")
