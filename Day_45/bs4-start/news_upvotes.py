from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')
titles = soup.find_all(name='a',class_='titlelink')
article_title = []
article_link = []
for title in titles:
    article_title.append(title.getText())
    article_link.append(title.get('href'))
score_list = []
upvotes = [upvote.getText().split()[0] for upvote in soup.find_all(name='span',class_='score')]

print(len(article_title))
print(len(article_link))
print(len(upvotes))




