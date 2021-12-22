from bs4 import BeautifulSoup
import requests
URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, 'html.parser')
movies = soup.find_all(name='h3',class_='title')
movies_list = []
for movie in movies:
    movies_list.append(movie.getText())
final_list = movies_list[::-1]

# create a text file
with open('movies.txt',mode='w') as file:
    for movie in final_list:
        file.write(f"{movie}\n")