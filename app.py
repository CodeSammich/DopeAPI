from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/<query>",methods=["GET","POST"])
def main(query ="radiohead"):
    if query == "radiohead":
    	return render_template("noArtist.html")
    #Default query to radiohead
    basic = """http://developer.echonest.com/api/v4/artist/search?api_key=V9SVA3AEDH6NCGYXY&format=json&name=""" + query + """&results=1"""
    
    #basic API call for searching for artist names
    requesta = urllib2.urlopen(basic)
    resulta = requesta.read()
    query = json.loads(resulta)
    if query["response"]["artists"]:
        query = json.loads(resulta)["response"]["artists"][0]["name"]
    else:
	query = "radiohead"
	error = "dang"
    
    #get first name from API return
    url="""http://developer.echonest.com/api/v4/artist/images?api_key=V9SVA3AEDH6NCGYXY&name=""" + query + """&format=json"""
    
    #basic API call for search
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)["response"]["images"] #gets images from image dictionary

    #creates array of image urls to reference
    final = []
    for image in r:
        final.append(image["url"])
    if len(final) > 15:
        final = final[0:16]
        
    artist = query #artist names
    
    return render_template("Artist.html",images=final,artist=artist)

if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
