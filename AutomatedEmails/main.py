import yagmail
import pandas
from news import NewsFeed
import datetime
import time

df = pandas.read_excel("people.xlsx")
def send_email():
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        
        news_feed = NewsFeed(interst=row['interest'], 
                    from_date=today, 
                    to_date = yesterday, 
                    language='en')

        email = yagmail.SMTP(user='backendforemail@gmail.com', password='txwgghrqyymtrzlc')
        email.send(
            to = row['email'], 
            subject = f"Your {row['interest']} news for today!",
            contents = f" Hi {row['name']}\n See what's about {row['interest']} today. {news_feed.get()}")

            
while True:
    if datetime.datetime.now().hour == 16 and datetime.datetime.now().minute == 34:
        for index, row in df.iterrows():
            send_email()
    time.sleep(60)