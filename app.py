from flask import Flask, render_template, request
import urllib2
import json
import signal
import thread
import time
import multiprocessing

app = Flask(__name__)

#resrouce links
'''
Multithreading resources for reference and alternative solutions, in order of usefulness and relevance:

http://stackoverflow.com/questions/14429703/when-to-call-join-on-a-process
http://stackoverflow.com/questions/15085348/what-is-the-use-of-join-in-python-threading
http://stackoverflow.com/questions/14920384/stop-code-after-time-period
http://softwareramblings.com/2008/06/running-functions-as-threads-in-python.html
http://stackoverflow.com/questions/15460677/python-running-function-in-thread-does-not-modify-current-thread
http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
http://stackoverflow.com/questions/492519/timeout-on-a-python-function-call

'''

#testing threading class
'''
#Make check_url calls in main a thread (can be used for all functions)
#used as FuncThread( <function name only>, <args>)
class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
        
    def run(self):
        self._target(*self._args)
'''

#start of actual code
def apiCall(n):
    request = urllib2.urlopen(n)
    result = request.read()
    return json.loads(result)
    
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

@app.route("/",methods=["GET","POST"])
def main():
    if request.method != "GET":
        query = request.form["artist"]
    else:
        query = "Radiohead"
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
    
    url="""http://developer.echonest.com/api/v4/artist/images?api_key=V9SVA3AEDH6NCGYXY&name=""" + query + """&format=json&results=100"""
    #sets API call for image search
    r = apiCall(url)["response"]["images"] #gets images from image dictionary
    #runs the API call
    
    newQuery = apiCall("https://api.spotify.com/v1/search?q=" + query + "&type=artist")["artists"]["items"][0]["id"]
    track = apiCall("https://api.spotify.com/v1/artists/" + newQuery + "/top-tracks?country=US")

    final = []
    counter = 0
    for image in r:
        #multiprocessing might have to run in __name__ == "main", stackoverflow here:
        #http://stackoverflow.com/questions/14920384/stop-code-after-time-period
        t1 = multiprocessing.Process( target=check_url, name = "check_url", args=image["url"])
        t1.start()
        time.sleep(2); #Will wait for 2 seconds to do the .1 second function, just in case
        p.join(2); #will also terminate check_url if successfully finished
        valid_image = True
        
        if p.is_alive():
            # Terminate check_url if not finished
            p.terminate()
            t1.join
            valid_image = False
            
    	if counter < 5 and valid_image:
            final.append(image["url"])
            counter = counter + 1
    #creates array of image urls to reference
    
    if len(final) > 5:
        final = final[0:1]
    #truncates excess length
    
    Tracks = []
    for T in track["tracks"]:
    	Tracks.append(T["name"])
    
    return render_template("Artist.html",images=final,artist=query,Tracks = Tracks)

if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
