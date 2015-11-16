from flask import Flask, render_template, request
import urllib2
import json
import signal
import thread
import time
import multiprocessing

app = Flask(__name__)

#/**
#apiCall:
#Params:
#	n: A string containing an API call to be ran
#
#Returns:
#	A python dictionary based on the JSON structure of the API call.
#
#	This method takes an API call and returns the corresponding dictionary.
#**/
def apiCall(n):
    request = urllib2.urlopen(n)
    result = request.read()
    return json.loads(result)
    

#/**
#check_url:
#Params:
#	url: A string containing a link to be validated
#
#Returns:
#	A boolean indicating the validity of the url
#
#	This method makes a server call searching for a valid responsing suggesting a valid link. 
#	If the request times out or gets a failure response from the server, it returns false.
#**/
def check_url(url):
    try:
        headers={
            "Range": "bytes=0-10",
            "User-Agent": "MyTestAgent",
            "Accept":"*/*"
        }
        req = urllib2.Request(url, headers=headers) #35 seconds if invalid link, .1 if valid
        response = urllib2.urlopen(req)
        return response.code in range(200, 209)
    except Exception, ex:
        return False
        
     
#/**
#Main:
#Params:
#	Query, a piece of data sent from a POST form.
#
#Returns:
#	Renders a webpage.
#
#	This method takes a query (defaulted to Radiohead, the coolest of bands) and uses it to make a set of
#	API calls. The first and third API calls are to Echonest and Spotify respectively for finding an artist
#	whose name is equal or similar to the query. This should remove a risk of typos, but defaults to Radiohead
#	if necessary. The second and fourth API calls are used to get images and track-names respectively from
#	databases. Then, a loop checks image links to make sure they are valid so that they can be rendered. Valid
#	images and tracknames are passed into the render form.
#**/
@app.route("/",methods=["GET","POST"])
def main():
    query = "Radiohead"
    if request.method == "POST":
        query = request.form["artist"]
    for space in [' ']:
        query = query.replace(space, "%20")
    basic = """http://developer.echonest.com/api/v4/artist/search?api_key=V9SVA3AEDH6NCGYXY&format=json&name=""" + query + """&results=1"""
    query = apiCall(basic)

    if query["response"]["artists"]:
        query = query["response"]["artists"][0]["name"]
    else:
	query = "Radiohead"
    artist = query
    
    for space in [' ']:
        query = query.replace(space, "%20")
    print query
    
    url="""http://developer.echonest.com/api/v4/artist/images?api_key=V9SVA3AEDH6NCGYXY&name=""" + query + """&format=json&results=100"""
    r = apiCall(url)["response"]["images"]

    newQuery = apiCall("https://api.spotify.com/v1/search?q=" + query + "&type=artist")["artists"]["items"][0]["id"]
    track = apiCall("https://api.spotify.com/v1/artists/" + newQuery + "/top-tracks?country=US")

    final = []
    counter = 0
    for image in r:
        ''' 
        multiprocessing might have to run in __name__ == "main", stackoverflow here:
        http://stackoverflow.com/questions/14920384/stop-code-after-time-period 
        multiprocessing code below, good for reference
        '''
        t1 = multiprocessing.Process( target=check_url, name = "check_url", args=(image["url"],))
        t1.start()
        time.sleep(.2);
        t1.join(.2);
        valid_image = True
        print "\n" + image["url"] + "\n"
        if t1.is_alive():
            t1.terminate()
            t1.join()
            valid_image = False
            print "check_url taking too long, terminated"
    	if counter < 1 and valid_image:
            final.append(image["url"])
            counter = counter + 1
    
    if len(final) > 1:
        final = final[0:1]
    Tracks = []
    for T in track["tracks"]:
    	Tracks.append(T["name"])
    return render_template("Artist.html",images=final,artist=artist,Tracks = Tracks)

if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
