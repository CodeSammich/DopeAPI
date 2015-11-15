# DopeAPI
To make the dopest of API's

Front End: Ari Hatzimemos, Rong Yu,
Back End: Albert Mokrejs, Samuel Zhang

Echonest API Key: V9SVA3AEDH6NCGYXY

The DopeAPI project makes use of a search-box to make an API-call to EchoNest to find an artist of a similar name. This should remove typos and similar errors. Then it finds a list of image links for the artist selected, and runs through all of them using multiple threads and server calls to make sure they point to valid images. If they do, it adds them to a list of valid images. After that Spotify's API is used to find the top tracks for the artist, which are then passed along with the images into the HTML form.
