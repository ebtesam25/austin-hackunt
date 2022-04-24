import compare_face as cf
from flask import Flask, request, redirect, session, url_for, Response, json, render_template, send_from_directory
from werkzeug.utils import secure_filename
from flask.json import jsonify
from flask_cors import CORS
from google.cloud import datastore
from google.cloud import vision
from google.cloud import storage
import os
import cdbh as cdb

# import faceutils


with open('credentials.json', 'r') as f:
    creds = json.load(f)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_top_labels(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    
    client = vision.ImageAnnotatorClient.from_service_account_json('gc.json')
    image = vision.types.Image()
    image.source.image_uri = uri

    
    response = client.label_detection(image=image)

    print ('hereeeeeeeeeeeeeeeeeeeeeee')

    labels = response.label_annotations
    # print('Labels:')

    i = 0

    keywords = []
    for label in labels:
        print(label.description)
        keywords.append(label.description)
        i = i + 1
        if i == 3:
            break


    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    if len(keywords) == 0:
        keywords.append("random")
    return keywords


def uploadtogcp(filename):
    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json('gcpkey.json')

    # Make an authenticated API request
    ##buckets = list(storage_client.list_buckets())
    ##print(buckets)

    bucketname = "hackerbucket"
    # filename = sys.argv[2]


    bucket = storage_client.get_bucket(bucketname)

    destination_blob_name = "current.jpg"
    source_file_name = filename

    blob = bucket.blob(destination_blob_name)
    blob.cache_control = "no-cache"

    blob.upload_from_filename(source_file_name)
    blob.make_public()
    blob.cache_control = "no-cache"

    print('File {} uploaded to {}.'.format(source_file_name, destination_blob_name))


@app.route("/file_upload", methods=["POST"])
def fileupload():

    if 'file' not in request.files:
          return "No file part"
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
      return "No selected file"
    if file and allowed_file(file.filename):
        # UPLOAD_FOLDER = "./uploads"
        UPLOAD_FOLDER = "uploads"
  
        filename = secure_filename(file.filename)
        # file.save(os.path.join(UPLOAD_FOLDER, filename))
        file.save(filename)
        # uploadtogcp(os.path.join(UPLOAD_FOLDER, filename))
        uploadtogcp(os.path.join(filename))
        return 'https://storage.googleapis.com/hackybucket/current.jpg' 
    
    return 'file not uploaded successfully', 400









@app.route("/registeruser", methods=['GET', 'POST'])
def registeruser():

    print(request)

    request_json = request.get_json()
    print (request_json)

    # resraw = request.get_data()
    # print (resraw)


    conn = cdb.connector()
    
    
    cf.downloadpic(request_json['imageurl'], "candidate.jpg")
    
    estr = cf.save_encoding("candidate.jpg", "candidate.txt", "hackunt2022")
    estr = estr.replace("[", "")
    estr = estr.replace("]", "")
    
    cdb.add_users(conn, request_json['name'], estr)
    



    retjson = {}

    # retjson['dish'] = userid
    retjson['status'] = "successfully added"
    
    return json.dumps(retjson)

    resp = Response(retjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp  
 


@app.route("/verifyandtrackuser", methods=['GET', 'POST'])
def dregisteruser():

    print(request)

    request_json = request.get_json()
    print (request_json)

    resraw = request.get_data()
    print (resraw)

    imgurl1 = request_json['imageurl']
    imgurl2 = ""
    found = 0
    estr = ""
    lat = request_json['location']['lat']
    lng = request_json['location']['lng']
    outcome = False
    
    conn = cdb.connector()

    fval, estr = cdb.login(conn, request_json['name'])
    
    if fval:
        cf.downloadpic(imgurl1, "testx.jpg")
        fembed = cf.np.fromstring(estr, dtype=float, sep=' ')

        
        outcome = cf.compare(fembed, "testx.jpg")
        
        if outcome:
            
            cdb.add_tracking(conn, request_json['name'], lat, lng)


        
        # cf.downloadpic(imgurl2, "testy.jpg")
        
    

    retjson = {}

    # retjson['dish'] = userid
    retjson['status'] = str(outcome)
    
    return json.dumps(retjson)
    

    resp = Response(retjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp  








@app.route("/dummyJson", methods=['GET', 'POST'])
def dummyJson():

    print(request)

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()
 

    status = {}
    status["server"] = "up"
    status["message"] = "some random message here"
    status["request"] = res 

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp




@app.route("/dummy", methods=['GET', 'POST'])
def dummy():

    ##res = request.json

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(js, status=200, mimetype='text/html')
    ##resp.headers['Link'] = 'http://google.com'

    return resp

@app.route("/api", methods=["GET"])
def index():
    if request.method == "GET":
        return {"hello": "world"}
    else:
        return {"error": 400}


if __name__ == "__main__":
    app.run(debug=True, host = 'localhost', port = 8003)
