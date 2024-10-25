import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")

all_movies = soup.find_all(name="h3")
all_movies_names = []

for movie in all_movies:
    movie_name = movie.getText()
    if ")" in movie_name:
        movie_name = movie_name.split(") ")[1]
    all_movies_names.append(movie_name)

all_movies_names.reverse()
index = 1
for movie in all_movies_names:
    with open("movies.txt", mode="a") as file:
        file.write(f"{index}. {movie}\n")

    index += 1
