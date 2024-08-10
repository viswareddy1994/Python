import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

ancher_tags = soup.find_all(name="span", class_ = "titleline")
titles = []
urls = []
for tag in ancher_tags:
    anchors = tag.find("a")
    title = anchors.getText()
    titles.append(title)
    url = anchors.get("href")
    urls.append(url)
    
    
scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# print(titles)
# print(urls)
# print(scores)

highest_num = max(scores)
highest_upvote_article = scores.index(highest_num)
print(titles[highest_upvote_article])
print(urls[highest_upvote_article])
print(scores[highest_upvote_article])
