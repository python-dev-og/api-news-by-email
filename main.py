import requests
from send_email import send_email

api_key = "7d233c34c7f744cd8f4aa2c848d22bed"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-11-08&sortBy=publishedAt&" \
      "apiKey=7d233c34c7f744cd8f4aa2c848d22bed&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + str(article["description"]) \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

