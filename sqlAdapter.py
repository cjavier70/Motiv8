__author__ = 'cameronjavier'

from errorHandler import *
import MySQLdb
db = MySQLdb.connect("motiv8instance.cwkcvq4ycfyc.us-west-2.rds.amazonaws.com","admin","motivate","innodb")

def sendSql(sql):
    cur = db.cursor()
    cur.execute(sql)
    lastId = cur.lastrowid
    db.commit()
    return lastId

def getFriendList(userId):
    sql = "SELECT * FROM FriendList WHERE userId={0}".format(userId)
    cur = db.cursor()
    cur.execute(sql)
    if(cur.rowcount == 0):
        return printAndExit("No friendList entry for id {0}".format(userId))
    friends = cur.fetchall()[0][1]
    return friends.split(", ")

def getFitPoints(userId):
    #TODO:friendList has fbIds, and we also need to return names
    #TODO: cache User info
    sql = 'SELECT fitPoints FROM FitPoints WHERE userId={0}'.format(userId)
    cur = db.cursor()
    cur.execute(sql)
    if(cur.rowcount == 0):
        return printAndExit("No fitPoints entry for id {0}".format(userId))
    return cur.fetchall()[0][0]

def getUser(userId):
    sql = 'SELECT * FROM User WHERE fbId="{0}"'.format(userId)
    cur = db.cursor()
    cur.execute(sql)
    if(cur.rowcount == 0):
        return printAndExit("No user entry for id {0}".format(userId))
    userData = cur.fetchall()[0]
    return User(userData[0], userData[1], userData[2], userData[3], userData[4])

class User:
    def __init__(self, id, firstName, lastName, accessToken, fbId):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.accessToken = accessToken
        self.fbId = fbId
    def getFullName(self):
        return self.firstName + " " + self.lastName