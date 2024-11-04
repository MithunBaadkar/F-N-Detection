
#program - 1 without sentiment

import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    print("1")
    response = requests.get(url)
    print(f"Responce status code: {response.status_code}")
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text,'html.parser')
    print(soup.prettify()[:1000])
    headlines = soup.find_all('h2')
    news_articles = [headline.get_text() for headline in headlines]
    return news_articles

def is_fake_news(article):
    fake_keywords = ['hoax','fake','scam','unverified','false']
    for keyword in fake_keywords:
        if keyword in article.lower():
            return True
    return False

url = input("Bro just enter the URL here: ")
news_articles = fetch_news(url)

if not news_articles:
    print("No article found or three wes an error fetching the news.")
else:
    for article in news_articles:
        if is_fake_news(article):
            print(f'Fake News Detected: {article}')
        else:
            print(f'Real News: {article}')

#https://www.wionews.com/world/canada-hindu-temple-attack-police-arrests-three-people-demonstrating-against-khalistanis-773225      -RealNews
#https://www.bbc.com/news/topics/cjxv13v27dyt   -FakeURL

#program-2 with sentiment 
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import readability

def fetch_news(url):
    response = requests.get(url)
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text,'html.parser')
    headlines = soup.find_all('h2')
    news_articles = [headline.get_text() for headline in headlines]
    return news_articles

def analyze_articles(article):
    sentiment = TextBlob(article).sentiment.polarity
    readability_score = readability.getmeasures(article,lang='en')
    return sentiment,readability_score['readability grades']['FleschReadingEase']

url = input("Just enter the URL of the news website: ")
news_articles = fetch_news(url)

if not news_articles:
    print("No articles found or there was an error fetching the news.")
else:
    for article in news_articles:
        sentiment,readability_score = analyze_articles(article)
        if sentiment < -0.5 or readability_score < 30:
            print(f'Possible Fake News: {article}')
        else:
            print(f'Real News: {article}')

#https://www.wionews.com/world/canada-hindu-temple-attack-police-arrests-three-people-demonstrating-against-khalistanis-773225      -RealNews
#https://www.bbc.com/news/topics/cjxv13v27dyt   -FakeURL