from flask import Flask, request
import sys
import atexit
from fbAdapter import getName, getFriends
from sqlAdapter import *
from collections import OrderedDict
import time
import json

current_milli_time = lambda: int(round(time.time() * 1000))
#from mockFacebook import mockFriends

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

@app.route('/leaderboard/<userid>', methods=['GET'])
def leaderboard(userid):
    print "Received Leaderboard request at milli: {0}".format(current_milli_time() % 1000)
    return getLeaderBoard(userid)

def postUser():
    r = None
    try:
        accessToken = request.get_json().get('accessToken', '')
        fbId = request.get_json().get('fbId', '')
    except:
        return 'Error: Fields are accessToken, fbId. \
         If you sent those, you likely did not pass json to this URL'
    try:
        name = getName(accessToken)
        firstName = name.split()[0]
        lastName = name.split()[1]
        lastId = createUser(firstName, lastName, accessToken, fbId)

    except Exception as e:
        return "Insert Into User Threw an exception: %s" % e
    return "%d" % lastId

def getLeaderBoard(userId):
    friendList = getFriendList(userId)
    friendDict = dict()
    for friendId in friendList:
        user = getUser(friendId)
        score = getFitPoints(user.id)
        friendDict[user.getFullName()] = score
    #TODO: Logging
    print "Responded Leaderboard request at milli: {0}".format(current_milli_time() % 1000)
    od =  OrderedDict(sorted(friendDict.items(), key = lambda t: t[1]))
    return json.dumps(od)

def createUser(firstName, lastName, accessToken, fbId):
    sql = "INSERT INTO User (firstName, lastName, accessToken, fbId) VALUES ('%s', '%s', '%s', '%s')" \
         % (firstName, lastName, accessToken, fbId)
    userId = sendSql(sql)

    sql = "INSERT INTO FriendList (userId, friendList) VALUES ('%s', '%s')" \
        % (userId, getFriends(accessToken))
    sendSql(sql)

    sql = "INSERT INTO FitPoints (userId, fitPoints) VALUES ('%s', 0)" % userId
    sendSql(sql)

    return userId


def clean():
    print "Clean complete"
    #sys.stdout.flush()
    sys.stdout.close()

atexit.register(clean)

if __name__ == '__main__':
    app.run(debug=True)
