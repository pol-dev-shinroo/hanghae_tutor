import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get("https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701", headers=headers)

soup = BeautifulSoup(data.text, "html.parser")

trs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

for tr in trs:
    title = tr.select_one("td.info > a.title.ellipsis").text.strip()
    rank = tr.select_one("td.number").text[0:2].strip()
    artist = tr.select_one("td.info > a.artist.ellipsis").text.strip().replace("\s+", " ")

    print(rank, title, artist)


# strip 예시:
string_with_whitespace = "   hello world   "
string_without_whitespace = string_with_whitespace.strip()

# print(string_with_whitespace)  # prints "   hello world   "
# print(string_without_whitespace)  # prints "hello world"

# slice notation 예제:
# my_string = "Hello, world!"
# substring = my_string[0:5]

# print(my_string)    # prints "Hello, world!"
# print(substring)    # prints "Hello"
