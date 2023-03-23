import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829", headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, "html.parser")

#############################
# 공식문서 참고 할것!
#############################


# a = soup.select_one("#old_content > table > tbody > tr:nth-child(3) > td.title > div > a")
# # print(type(a)) => class, 즉 object

# print(a)
# print(a["href"])

#############################
# 제목만 가져오기
#############################
# old_content > table > tbody > tr:nth-child(2) // 공통적인것만 빼기
trs = soup.select("#old_content > table > tbody > tr")
# print(trs)
# #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
for tr in trs:
    a = tr.select_one("td.title > div > a")
    if a is not None:
        title = a.text
        rank = tr.select_one("td:nth-child(1) > img")["alt"]
        star = tr.select_one("td.point").text
        print(rank, title, star)
