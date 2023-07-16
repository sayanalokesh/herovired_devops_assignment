import configparser
from pymongo import MongoClient
import os
from flask import Flask, jsonify

client = MongoClient('mongodb+srv://username:password@cluster0.gdxqqlg.mongodb.net/')
db = client['configuration']
collection = db['items']

def configuration_read_file(config_file):
    try:
        if os.path.exists(config_file):  # it is built-in function in Python that checks if a file exists for that I've imported os module
            config = configparser.ConfigParser()
            config.read(config_file)
            return dict(config.items())
        else:
            raise FileNotFoundError("File not found",config_file)  #to check whether the file is exists with the name config_file, if the file is not found not it throws an error
    except Exception as e:
        print("Exception occurred: ",e)
configuration_read_file("config_file.properties")

app = Flask(__name__)

@app.route('/items', methods=['POST'])
def postItemRoute():
    collection.insert_one(configuration_read_file("config_file.properties")) # here I've mentioned only specified data,  i.e., "Database" & ""Server" as asked in the question
    return jsonify({'message': 'Added Successfully'})

@app.route('/items', methods=['GET']) # to fetch the information from the database using postman
def getItemRoute():
    items = list(collection.find({}, { '_id': 0 }))
    return jsonify(items)

if __name__ == "__main__":
    app.run(port=3000, debug=True)