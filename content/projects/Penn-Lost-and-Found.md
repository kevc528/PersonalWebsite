# Penn Lost and Found
> A mobile app with an administrator web app for to help locate lost items

---
**Source Code**

<https://github.com/kevc528/Penn-Lost-and-Found>

---

![Project Architecture](/content/images/lost-found-architecture.jpg)

## About
This project was my final project for CIS350, a software enginering class I took freshman spring. The goal of 
this project was to develop a complex software system as part of a team using agile methodology. My team decided 
to create a lost and found app for Penn students to try and relieve some of the stress caused by loosing items 
on campus. The main parts of this project was an android app for normal users, a web app for administrators, and 
on the backend, an API to interact with data we stored using MongoDB.

## Development
### The Process: XP implementation of Agile
Throughout the entire project, we had a project manager who was paired to us. Our PM helped with organizing 
meetings and our evaluations. First, our team met and came up with a project spec containing user stories that 
would guide the rest of our development process. The rest of our development time was split into three 
iterations, each two weeks long. Each iteration began with a planning session and ended with a demo. Throughout 
the iterations, we would have regular check in meetings to make sure everyone is on the same track and there are 
no blockers.

### The REST API
For this project, we used an API to assist in performing the CRUD operations with our MongoDB database, which was 
important for maintaining state in our application. The database contained collections with information on users, 
lost and found items, chats, messages, and more. And the API, written using Express and Node.js, was important 
for interacting with this data. Express was used to build HTTP routes that could be called by other applications 
to get/modify data. There was also a really nice Node package for MongoDB called Mongoose that made building 
the API much easier.

One initial challenge for us was storing images in the database. For images, we used GridFS and Multer to 
configure the server to take requests to post and get images from MongoDB. GridFS works by dividing files into 
chunks of bit data and storing those chunks in separate entries. Multer was useful for handling file uploads and 
worked as a middleware to get the file data into the GridFS storage.

Then after an image is saved and there is a request for the image, GridFS will create a bit stream to send back 
bit data to display the image in the app.

With the API in place, we used Ajax requests in the web app and AsyncTasks with the package Java.Net in the 
Android app to make HTTP requests to this API to fetch and write data.

### Native Android App
![Android App](/content/images/penn-lost-found-android.jpg)

The Android App was developed using Java in Android Studio. It is what most students would use on 
this platform. Students would be able to create an account and login through the app. Then they would be able to 
see a live feed of items that other students have lost or found, as well as create their own postings. The 
postings have information on location of item, descriptions, and pictures. All of this data is created and 
brought in through requests to the API, using an AsyncTask and HttpURLConnection to execute the request in the 
background.

To gather information on location we utilized Foursquare Places API and Bing Maps API. Foursquare Places API was 
used to populate an AutoCompleteTextView in the create posting form which would get longitude and latitude data 
from the location the user selects. Then when the post is viewed, Bing Maps API would take these coordinates and 
display a MapView pointing to that location.

Additionally, we also implemented messaging to communicate claiming items with other users. Users could create 
chats with the poster of any item of interest. We had the chat "live" update by fetching message data every 5 
seconds... which might be a questionable implementation. With the feed, we were able to avoid maintaining live 
refreshes by just having data update when the user pulls the screen down.

The other features like logging in, creating an account, reporting an user, etc. are all pretty simple and 
involve simple reads and writes to the database through the API.

### Admin Web App
![Web App](/content/images/penn-lost-found-web.jpg)

The web app was developed using HTML/CSS/JavaScript and Vue.js for more interactivity in the UI, like modals, 
forms, and tables. The web app is for administrators of the app, who can see everything going on behind the 
scenes, like all of the user activity and any reported users. The admin app also has to power to issue warnings 
and bans to anyone who is misusing the app.

Like the Android app, the web app also gets and sends its data through the API. The web app uses Ajax requests 
through an XMLHttpRequest object. The tables with user and item data are populated through the data returned by 
these requests. 

The web app is pretty similar to the Android app, but has less restrictions on access, like viewing anyones 
messages and account data. The web app also has access to requests in the API that will delete items and warn/ban 
users.

## Final Thoughts
Overall, I really enjoyed the this project. It was my first big project experience and it was really cool being 
able to develop an application with so many features. Also, I was able to gain a lot of valuable skills from this 
project, not only with software development, but also with working in an Agile setting. Even during my 
internships, I've used some of what I learned since it's pretty common to design applications with a similar 
idea for architecture.

As for the overall development experience, something that really stood out to me was Android Studio. It was my 
first time developing a mobile app so the task felt pretty daunting at first. But with the great tooling in 
Android Studio, like the built in emulator, and the detailed documentation online, app development was a pretty 
smooth experience.

Looking back, there probably could've been a few things that could be better. One main thing was that the 
constant refreshing to keep everything up to date, which might become costly as the app scales. Maybe, using 
web sockets to have a persistent connection might have been a better approach.