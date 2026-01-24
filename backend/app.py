from flask import Flask,request,jsonify
import mysql.connector,bcrypt

app=Flask(__name__)

db=mysql.connector.connect(
host="db",
user="root",
password="root",
database="logindb"
)

@app.route("/login",methods=["POST"])
def login():
 data=request.json
 hashed=bcrypt.hashpw(data["password"].encode(),bcrypt.gensalt())
 cur=db.cursor()
 cur.execute("INSERT INTO users(username,password) VALUES(%s,%s)",
 (data["username"],hashed))
 db.commit()
 return jsonify({"message":"User saved securely"})

app.run(host="0.0.0.0",port=5000)
