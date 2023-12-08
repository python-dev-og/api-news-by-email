import requests

api_key = "7d233c34c7f744cd8f4aa2c848d22bed"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-11-08&sortBy=publishedAt&" \
      "apiKey=7d233c34c7f744cd8f4aa2c848d22bed"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

