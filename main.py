import requests
from send_email import send_email
import os
from dotenv import load_dotenv
load_dotenv()

topic = "tesla"
api_key = os.getenv('API_KEY')
url = url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      f"from=2023-12-20&sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + str(article["description"]) \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

