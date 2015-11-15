# DopeAPI

### Objective: Music Search Engine

###APIs Used

- Spotify API
- Echonest API Key: V9SVA3AEDH6NCGYXY

The DopeAPI project makes use of a search-box to make an API-call to EchoNest to find an artist of a similar name. This should remove typos and similar errors. Then it finds a list of image links for the artist selected, and runs through all of them using multiple threads and server calls to make sure they point to valid images. If they do, it adds them to a list of valid images. After that Spotify's API is used to find the top tracks for the artist, which are then passed along with the images into the HTML form.

###Contributors

Front End: Ari Hatzimemos, Rong Yu,
Back End: Albert Mokrejs, Samuel Zhang

| Contributor | Role |
|:-----------:|:----:|
| ![Albert Mokrejs] (https://www.facebook.com/photo.php?fbid=700179553421740&set=a.110070619099306.12066.100002891068047&type=3&theater) | Backend |
| ![Samuel Zhang] (https://www.facebook.com/photo.php?fbid=1091968907487880&set=a.151440211540759.25095.100000243424333&type=3&theater) | Backend |
| ![Ari Hatzimemos] (https://www.facebook.com/photo.php?fbid=2004306209708289&set=a.108416925963903.10098.100003867890546&type=3&theater) | Frontend / Leader |
| ![Rong Yu] (https://www.facebook.com/photo.php?fbid=595674690463262&set=a.204390769591658.50865.100000622105674&type=3&theater) | Frontend |
