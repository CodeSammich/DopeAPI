# DopeAPI

### Objective: Music Search Engine

###APIs Used

- Spotify API
- Echonest API Key: V9SVA3AEDH6NCGYXY

The DopeAPI project makes use of a search-box to make an API-call to EchoNest to find an artist of a similar name. This should remove typos and similar errors. Then it finds a list of image links for the artist selected, and runs through all of them using multiple threads and server calls to make sure they point to valid images. If they do, it adds them to a list of valid images. After that Spotify's API is used to find the top tracks for the artist, which are then passed along with the images into the HTML form.

###Contributors

|                                       |   **Member**   |                   **GitHub**                 |            **Role**            |
|---------------------------------------|:--------------:|:--------------------------------------------:|:------------------------------:|
| <img src="images/albert.jpg" width="100" height="100" /> | Albert Mokrejs   |[`@AlbertMokrejs`](https://github.com/AlbertMokrejs)        | Backend - API Handler  |
| <img src="images/samuel.jpg" width="100" height="100" /> | Samuel Zhang |[`@CodeSammich`](https://github.com/CodeSammich)    | Backend - Thread Handler  |
| <img src="images/ari.jpg" width="100" height="100" /> | Ari Hatzimemos    |[`@ahatzi`](https://github.com/ahatzi)| Frontend - Overseer |
| <img src="images/rong.jpg" width="100" height="100" />  | Rong Yu  |[`@RongYu98`](https://github.com/RongYu98)        | Frontend - Designer  |

