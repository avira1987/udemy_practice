
import requests
from pprint import pprint

class NewsFeed:
    """Repesenting multiple news title and links as a single sting"""
    base_url = "https://newsapi.org/v2/everything?"
    #API key
    api_key ="72d7841dd6de4b3fb8cde460d585d4cd"

    def __init__(self, interst, from_date, to_date, language):
        self.interst = interst
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"{self.base_url}" \
                f"qInTitle={self.interst}&" \
                f"from={self.from_date}&" \
                f"to={self.to_date}&" \
                f"Language={self.language}&" \
                f"sortBy=publishedAt&" \
                f"apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        # pprint(x)
        # pprint(content)
        email_body = ""
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

# news_feed = NewsFeed(interst='nasa', from_date='2023-01-14', to_date='2023-01-15', language='en')
# p=news_feed.get()
# print(p)