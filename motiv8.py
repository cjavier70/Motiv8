from flask import Flask, g, render_template, url_for, request, Response, jsonify
import _mysql
db = _mysql.connect("motiv8instance.cwkcvq4ycfyc.us-west-2.rds.amazonaws.com","admin","motivate","innodb")
import sys 
sys.stdout=open('/var/www/motiv8/log/output.log', 'w')

app = Flask(__name__)


@app.route('/user', methods=['GET','POST'])
def index():
    if request.method=='GET':
        return "Welcome sir to Motiv8 API"
    else:
        print "LOOK"
        print request.get_json()
        try:
            body = "Your json passed me %s" % request.get_json().get('firstName', '')
        except:
            sys.stdout.close()
            return 'Error'

        #db.query("INSERT INTO User (firstName, lastName, accessToken) VALUES ('Gabrielle', 'Javier', 'fake2')")
        return body

if __name__ == '__main__':
    app.run(debug=True)

