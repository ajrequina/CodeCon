# CodeCon

## Developers
- Roland Justine Navaja <br>
- Arjemariel Requina

## Description
CodeCon (Code Conference) is a web application that will serve as a social media
site for programmers. It will act like a project expo but held online. Programmers will have a
chance to showcase their algorithms and programs to other programmers around the world.
They can show and explain their algorithms or programs as a whole and its specification and
features. Aside from posting their codes, programmers can also follow another programmer’s
account. Through this, the user will be notified for any new posts and other activities of the
followed users. The users can also comment the post of other users and like them as well.
Another feature will be the trending posts of the week. This will compose of codes, programs,
and/or algorithms that are the talked by most users within a week.

## Installation
1. clone the repo https://github.com/ajrequina/codecon.com.git
2. cd codecon/codecon
3. execute pip install -r requirements
4. execute python manage.py makemigrations
5. execute python manage.py migrate
6. execute python manage.py runserver

## Features and Functionalities

### User Module

![screenshot from 2017-05-30 12-49-40](https://cloud.githubusercontent.com/assets/24803247/26568502/8869e5f0-4536-11e7-9042-ee9d5f4d1fd9.png)

* Signup/Register
   - Users can register on the site by providing their email, username, password, firstname and lastname
   - Email addresses should be unique as well as the username
   - User will be redirected to the homepage after successful registration

* Signin/Login
   - Users can signin on the site by providing their username and password
   - User will be redirected to the homepage after successful signing in

![editprofile](https://cloud.githubusercontent.com/assets/15230546/26581344/a3909b66-456e-11e7-8c8c-cfd039f3c1d5.PNG)

* Logout
   - Users can logout on the site after signing in or registering 
   - User will redirected to the account page after successful log out

* Edit Profile
   - By going to the Settings (inside dropdown)
   - Users can update their profile info : firstname and/or lastname
   - Users can update their username and email (must be unique)
   - Users can change their passwords
   
![follow](https://cloud.githubusercontent.com/assets/15230546/26581296/722822e2-456e-11e7-9156-88b7f324c570.PNG)

* Follow User
   - By going to the dropdown (Search Function)
   - Users can search for another users and view their profile
   - They can follow the users and the posts of followed users will reflected on the stream page

* Unfollow User
   - By going to the dropdown (Search Function)
   - Users can search for another users and view their profile
   - They can unfollow the followed users and the posts of previously followed users will not be reflected on the user stream      page.
 
 
 ### Post Module
 
 ![image](https://cloud.githubusercontent.com/assets/15230546/26581379/c221a016-456e-11e7-8e77-3202e1447a8a.png)
 
 * Add Post
    - Users can add their own post by clicking create content in the stream page and profile page
    - The inputs are title, category, language, and the content
    - The website provides a Github Flavored Markdown support but the images cannot be uploaded to the server
    - https://guides.github.com/features/mastering-markdown/
    - The link of the images must be from Internet
    
 ![image](https://cloud.githubusercontent.com/assets/15230546/26581395/de367402-456e-11e7-9bfa-4c97afcafc4d.png)
 
 * Delete Post
    - Users can delete their own post by clicking the post (going to post detail page) and click 'delete'
 
 ![image](https://cloud.githubusercontent.com/assets/15230546/26581432/04ace328-456f-11e7-8fda-b13e18aaf6d3.png)
 
 * Edit Post
    - Users can edit their own post by clicking the post (going to the post detail page) and click 'edit'
    - User will be redirected to the edit form page
    - User can edit the title, category, language and the content of the post
    
 ![image](https://cloud.githubusercontent.com/assets/15230546/26581459/27ea5082-456f-11e7-87cf-c8bbe838d757.png)
 
 * View Post Detail
    - Users can view the detail of any post (followed or owned) by clicking the title of the post
  
  ![image](https://cloud.githubusercontent.com/assets/15230546/26581482/48c981f6-456f-11e7-8d82-44a22afb0e76.png)
  
 * View Posts (List)
    - Users can view the list of post in the profile (own) and in the stream page (followed and own)
  
 * Like Post/Star
    - User can like the post of any user (in profile page, stream page, and search page)
 
 * Unlike Post/Unstar
    - User can unlike the liked post of any user (in profile page, stream page, and search page)
 
 ### Comment Module
 
 ![image](https://cloud.githubusercontent.com/assets/15230546/26581913/75d4bcf4-4571-11e7-9903-1376c2db5d32.png)
 
 * Add Comment
    - Users can add comment on posts (in profile page, stream page, and search page)
 
 * Edit Comment
    - Users can edit comment on commented posts (in profile page, stream page, and search page)
    - Own comments only
 
 * Delete Comment
    - Users can delete comment on commented posts (in profile page, stream page, and search page)
    - Own comments only

### Notif Module
  The shown notifs on users are those notifs that are unread.
  
  ![image](https://cloud.githubusercontent.com/assets/15230546/26581952/918d8548-4571-11e7-8792-cb5137d670d3.png)
  
  * Add Post Notif
    - Followers of the users will be notified if the followed user has new post
  
  * Comment Post Notif
    - The owner of the post will be notified if there are users who commented on their post
  
  * Like Post Notif
    - The owner of the post will be notified if there are users who liked on their post
  
  * Follow Post Notif
    - Users will be notified if there users who followed them
  
  * Unfollow Post Notif
    - Users will be notified if there are users who unfollowed them
    
### Top10WeeklyPost

   ![image](https://cloud.githubusercontent.com/assets/15230546/26581982/b3507a46-4571-11e7-8819-d501d0e1e976.png)

   These are the posts that have the top ten highest number of likes and comments within the week. If the ranking of the 
   posts within the week is less than ten, the posts on the previous week will be included.
 
