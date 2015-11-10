from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/<query>",methods=["GET","POST"])
def main(query ="radiohead"):
    basic = """http://developer.echonest.com/api/v4/artist/search
    ?api_key=V9SVA3AEDH6NCGYXY&format=json&name=""" + query + """&results=1"""
    requesta = urllib2.urlopen(basic)
    resulta = requesta.read()
    query = json.loads(resulta)["response"]["artists"]["artist"][0]["name"]
    #should fix typos, if they exist
    url="""http://developer.echonest.com/api/v4/artist/images?
    api_key=V9SVA3AEDH6NCGYXY&name=""" + query + """&format=json"""
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)["response"]["images"]

if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
