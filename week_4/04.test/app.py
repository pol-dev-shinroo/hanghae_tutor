from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://lewigolski:1234@cluster0.1vcre.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

############# API EndPoints ##################
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/movie", methods=["GET"])
def movie_get():   
    movies = list(db.movies.find({}, {"_id": False}))
    return jsonify({"msg": "get complete", "result": movies})


@app.route("/movie", methods=["POST"])
def movie_post():   
    url_receive = request.form["url_get"]
    star_receive = request.form["star_get"]
    comment_receive = request.form["comment_get"]

     ################ scraping #################### 
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one("meta[property='og:title']")["content"]
    ogdesc = soup.select_one("meta[property='og:description']")["content"]
    ogimage = soup.select_one("meta[property='og:image']")["content"]

    doc = {
        "title": ogtitle,
        "desc": ogdesc,
        "image": ogimage,
        "comment": comment_receive,
        "stars": star_receive
    }

    db.movies.insert_one(doc)

    return jsonify({"msg": "post complete" })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)