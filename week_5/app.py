from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://lewigolski:1234@cluster0.1vcre.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {"name": name_receive, "comment": comment_receive}

    db.fan.insert_one(doc)
    return jsonify({"msg": "응원 완료!"})


@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    comments = list(db.fan.find())
    comments = [{**comment, **{"_id": str(comment["_id"])}} for comment in comments] # convert ObjectId to string
    return jsonify({'result': comments})



@app.route("/delete_updatebook", methods=["DELETE"])
def guestbook_delete():
    name_receive = request.form["id"]
    print(name_receive)
    db.fan.delete_one({'_id': ObjectId(name_receive)})
    return jsonify({'result': "success"})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
