query = "artificial intellegence"
api = "0ab6974e00fa4a658cac84dc45450b76"

#  0ab6974e00fa4a658cac84dc45450b76 = my api key from news API

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-09-24&sortBy=publishedAt&apiKey={api}"

print(url)