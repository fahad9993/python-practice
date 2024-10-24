from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles_tr = soup.find_all(name="tr", class_="athing")
articles_tr_score = soup.find_all(name="td", class_="subtext")

article_texts = []
article_links = []
articles_upvote = []
final_data = []

for tr in articles_tr:
    href = tr.find(name="span", class_="titleline").find("a").get("href")
    text = tr.find(name="span", class_="titleline").find("a").getText()
    if "https" not in href:
        href = "https://news.ycombinator.com/" + href
    article_links.append(href)
    article_texts.append(text)

for tr in articles_tr_score:
    span_score = tr.find(name="span", class_="score")
    score = int(span_score.getText().split()[0]) if span_score else 0
    articles_upvote.append(score)

for index in range(len(article_links)):
    final_data.append({
        "name": article_texts[index],
        "link": article_links[index],
        "upvote": articles_upvote[index]
    })

print(final_data)