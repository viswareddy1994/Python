import requests
from bs4 import BeautifulSoup
import os 

script_path = os.path.dirname(__file__)

file_path = os.path.join(script_path,"top_100_movies.txt")

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

gratest_movies_webpage = response.text

soup = BeautifulSoup(gratest_movies_webpage,"html.parser")

top_movies = soup.find_all(name="h3",class_="title")

top_movies_list = [movie.getText() for movie in top_movies]

top_movies = top_movies_list[::-1]
# print("\n".join(top_movies))
# top_movies_list.reverse()
# print("\n".join(top_movies_list))

with open(file_path, "w",encoding="utf-8") as file:
    for movie in top_movies:
        file.write(f"{movie}\n")