import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# mongodb setup
client = MongoClient("mongodb+srv://lewigolski:1234@cluster0.1vcre.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

# headers 안에 사용되는 다른 common keys (authorization, accept (data format: application.json))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829", headers=headers)

soup = BeautifulSoup(data.text, "html.parser")

########## question 1 #########

# stars = soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.point").text
# title = soup.select_one("#old_content > table > tbody > tr:nth-child(4) > td.title > div > a").text
# print(stars, title)

########## question 1 (alternative via iteration) #########

# trs = soup.select("#old_content > table > tbody > tr")
# # old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# for idx, tr in enumerate(trs):
#     if idx == 3:
#         title = tr.select_one("td.title > div > a").text
#         stars = tr.select_one("td.point").text
#         print(stars, title)
#     else:
#         pass

########## question 2 #########

# trs = soup.select("#old_content > table > tbody > tr")
# # old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# to_find = soup.select_one("#old_content > table > tbody > tr:nth-child(4) > td.point").text

# for idx, tr in enumerate(trs):
#     stars = tr.select_one("td.point")
#     if stars is not None:
#         if stars.text == to_find:
#             title = tr.select_one("td.title > div > a").text
#             print(stars.text, title)
#             pass
#         else:
#             pass

########## question 1 #########
# movie = db.movies.find_one({"title": "가버나움"})
# print(movie["star"])

########## question 2 #########
# movie = db.movies.find_one({"title": "가버나움"})
# target_star = movie["star"]

# movies = list(db.movies.find({"star": target_star}))
# find  까지는 cursor object => iterable 가능함
# print(type(movies))

# for a in movies:
#     print(a["title"])

# for b in db.movies.find({"star": target_star}):
#     print(b["title"])

########## question 3 #########
# db.movies.update_one({"title": "가버나움"}, {"$set": {"star": "0"}})
