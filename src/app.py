from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import  ObjectId


app= Flask(__name__)

app.config['MONGO_URI']='mongodb://localhost/y'
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def holaMundo():
    user = mongo.db.user.find()
    us = json_util.dumps(user)
    return {"message": us}


@app.route('/createuser', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']

    if email and password:
        mongo.db.user.insert_one({
            'email':email,
            'password':password
        })
        return {"messsage":"saved user"}
    else:
        return{"message":"datos no ingresados"}
if __name__ == "__main__":
    app.run(debug=True)