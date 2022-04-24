# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from deepface import DeepFace
import json
from flask_cors import CORS
import base64, re
from google.cloud import storage
from importlib_metadata import os


  
# creating a Flask app
app = Flask(__name__)
CORS(app)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})



#creates a user
@app.route('/adduser', methods = ['GET', 'POST'])
def add_user():
    if(request.method == 'POST'):
        user = json.loads(request.data)
        return jsonify(user["name"]+" has been added successufully")


#upload image
@app.route('/uploadimg', methods = ['GET', 'POST'])
def upload_img():
    if(request.method == 'POST'):
        img = json.loads(request.data)
        png = base64.b64decode(img["img"])     
        filename = "img.jpg"

        with open(filename, "wb") as f:        
            f.write(png)

        client = storage.Client.from_service_account_json(os.path.abspath('gcpkey.json'))
        bucket = client.get_bucket('hackerbucket')
        blob = bucket.blob(filename)        
        
        regex = r"(?<=data:)(.*)(?=;)"
        split = img["img"].split('base64')
        format_image = re.findall(regex, split[0])[0]
        base64_image = base64.b64decode(split[1])
        blob.upload_from_string(base64_image, content_type=format_image)       

        image_url = "https://storage.googleapis.com/hackerbucket/" + filename
        return jsonify({"data":image_url})


#tracks a user
@app.route('/loguser', methods = ['GET', 'POST'])
def log_user():
    if(request.method == 'POST'):
        user = json.loads(request.data)
        return jsonify(user["name"]+" was spotted at  "+str(user["location"]))
  
  
# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
  
    return jsonify({'data': num**2})
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)