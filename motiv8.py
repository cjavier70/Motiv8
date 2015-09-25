from flask import Flask, g, render_template, url_for, request, Response, jsonify
import MySQLdb
import sys 
import atexit
from mockFacebook import mockFriends


db = MySQLdb.connect("motiv8instance.cwkcvq4ycfyc.us-west-2.rds.amazonaws.com","admin","motivate","innodb")
sys.stdout=open('/var/www/motiv8/log/output.log', 'a+w', 0)

app = Flask(__name__)


@app.route('/')
def index():
    fromField = request.headers.get('From')
    print fromField
    return "Welcome to Motiv8 API"

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method=='GET':
        return "Welcome to Motiv8 API"
    else:
        return postUser()

def postUser():
    r = None
    try:
        accessToken = request.get_json().get('accessToken', '')
        fbId = request.get_json().get('fbId', '')
        firstName = request.get_json().get('firstName', '')
        lastName = request.get_json().get('lastName', '')
    except:
        return 'Error: Fields are firstName, lastName, accessToken. \
         If you sent those, you likely did not pass json to this URL'
    try:
        #getName(fbId, accessToken);
        sql = "INSERT INTO User (firstName, lastName, accessToken, fbId) VALUES ('%s', '%s', '%s', '%s')" \
         % (firstName, lastName, accessToken, fbId)
        cur = db.cursor()
        cur.execute(sql)
        lastId = cur.lastrowid
        db.commit()
    except Exception as e:
        return "Insert Into User Threw an exception: %s" % e
    return "%d" % lastId

def getLeaderBoard():
    return "hello"

def clean():
    print "Clean complete"
    #sys.stdout.flush()
    sys.stdout.close()

atexit.register(clean)

if __name__ == '__main__':
    app.run(debug=True)
