# modules
import requests
import csv
from bs4 import BeautifulSoup

# URL
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# fetch the data and get the text out
response = requests.get(url).text

# create the soup
soup = BeautifulSoup(response,"html.parser")

# get all the title tags
title_tags = soup.find_all(name="h3",class_="title")

# create a DS to store all the movies
movies = []
header = ["Top 100 Movies"]

# fetch all the movies and append it to movies list
for title in title_tags:

    movies.append(title.text)

# reverse the list to display top 1-100 instead of 100 to 10.
movies =  movies[::-1]

# open a file and start writing the movies to the CSV
with open("movies.txt","w") as file:

    write = csv.writer(file)

    write.writerow(header)

    for movie in movies:

        write.writerow([movie])



