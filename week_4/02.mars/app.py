from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://lewigolski:1234@cluster0.1vcre.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    print(name_receive,address_receive,size_receive)
    doc = {
        "name": name_receive, 
        "address": address_receive,
        "size": size_receive
    }
    db.mars.insert_one(doc)
    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/mars", methods=["GET"])
def mars_get():
    mars_data = list(db.mars.find({}, {"_id": False}))
    return jsonify({'msg':'GET 연결 완료!', 'result': mars_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)