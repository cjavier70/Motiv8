__author__ = 'cameronjavier'
from flask import g

def sendSql(sql):
    try:
        g.cur.execute(sql);
        print g.cur._last_executed

    except pymysql.err.MySQLError as e:
        print("MYSQL ERROR")
        print e

    except pymysql.err.OperationalError:
        print pymysql.err.OperationalError
        if g.cur.connection.ping(True):
            g.cur.execute(sql)
            print g.cur._last_executed
        else:
            print "Server still not responding"
            return 'database error'