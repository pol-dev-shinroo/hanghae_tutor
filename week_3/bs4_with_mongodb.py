from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

# mongodb setup
client = MongoClient("mongodb+srv://lewigolski:1234@cluster0.1vcre.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta


# bs4
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829", headers=headers)

soup = BeautifulSoup(data.text, "html.parser")

trs = soup.select("#old_content > table > tbody > tr")
# print(trs)
# #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
for tr in trs:
    a = tr.select_one("td.title > div > a")
    if a is not None:
        title = a.text
        rank = tr.select_one("td:nth-child(1) > img")["alt"]
        star = tr.select_one("td.point").text
        doc = {"title": title, "rank": rank, "star": star}
        db.movies.insert_one(doc)
