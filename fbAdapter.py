import urllib2
import json
import motiv8Logger

def getName(accessToken):
    url = "https://graph.facebook.com/v2.4/me/?access_token={0}".format(accessToken)

    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    jsonData = resp.read()
    data = json.loads(jsonData)

    return data['name']

#TODO: Only returns 25 at a time
def getFriends(accessToken):
    logger = motiv8Logger.adapter
    logger.error("Ello sir")
    url = "https://graph.facebook.com/v2.4/me/friends?access_token={0}".format(accessToken)

    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    jsonData = resp.read()
    data = json.loads(jsonData)

    #friendArr has list of friend names and ids
    friendArr = data["data"]
    friendListStr = ""

    for friend in friendArr:
        friendListStr += friend["id"]
        friendListStr += ", "

    #get rid of last comma and whitespace
    friendListStr = friendListStr[:-2]
    return friendListStr

def writeUserPic(userId, accessToken):
    #TODO: See if this works
    logger = motivLogger.getLogger()
    url = "https://graph.facebook.com/v2.5/{0}/picture?access_token={1}".format(userId, accessToken)
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    rawPic = resp.read()
    try:
        fd = open('/var/www/profPics/{0}.jpeg'.format(userId), 'wb')
    except Exception as e:
        logger.error(e)

    fd.write(rawPic)
    fd.close()


