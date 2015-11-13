from flask import Flask, render_template, request
import urllib2
import json


app = Flask(__name__)

def apiCall(n):
    request = urllib2.urlopen(n)
    result = request.read()
    return json.loads(result)
    
def file_exists(path):
    try:
    	f = urllib2.urlopen(urllib2.Request(path))
        deadLinkFound = False
    except:
        deadLinkFound = True
    return deadLinkFound

@app.route("/",methods=["GET","POST"])
def main():
    if request.method != "GET":
        query = request.form["artist"]
    else:
        return render_template("Artist.html")
    #handles a lack of a query
    
    basic = """http://developer.echonest.com/api/v4/artist/search?api_key=V9SVA3AEDH6NCGYXY&format=json&name=""" + query + """&results=1"""
    #basic API call for searching for artist names
    
    query = apiCall(basic)
    #find a band of a similar name
    
    if query["response"]["artists"]:
        query = query["response"]["artists"][0]["name"]
    else:
	query = "Radiohead"
    #uses a band of the similar name if there is one
    #defualts query to radiohead if none is found
    
    url="""http://developer.echonest.com/api/v4/artist/images?api_key=V9SVA3AEDH6NCGYXY&name=""" + query + """&format=json"""
    #sets API call for image search
    
    r = apiCall(url)["response"]["images"] #gets images from image dictionary
    #runs the API call


    final = []
    for image in r:
    	if file_exists(image["url"]):
            final.append(image["url"])
    #creates array of image urls to reference
    
    if len(final) > 5:
        final = final[0:6]
    #truncates excess length
    
    return render_template("Artist.html",images=final,artist=query)

if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
