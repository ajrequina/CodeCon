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

* Signup/Register
   - Users can register on the site by providing their email, username, password, firstname and lastname
   - Email addresses should be unique as well as the username
   - User will be redirected to the homepage after successful registration

* Signin/Login
   - Users can signin on the site by providing their username and password
   - User will be redirected to the homepage after successful signing in

* Logout
   - Users can logout on the site after signing in or registering 
   - User will redirected to the account page after successful log out

* Edit Profile
   - By going to the Settings (inside dropdown)
   - Users can update their profile info : firstname and/or lastname
   - Users can update their username and email (must be unique)
   - Users can change their passwords

* Follow User
   - By going to the dropdown (Search Function)
   - Users can search for another users and view their profile
   - They can follow the users and the posts of followed users will reflected on the stream page

* Unfollow User
   - By going to the dropdown (Search Function)
   - Users can search for another users and view their profile
   - They can unfollow the followed users and the posts of previously followed users will not be reflected on the user stream      page.
 
 
 ### Post Module
 
 * Add Post
    - Users can add their own post by clicking create content in the stream page and profile page
    - The inputs are title, category, language, and the content
    - The website provides a Github Flavored Markdown support but the images cannot be uploaded to the server
    - https://guides.github.com/features/mastering-markdown/
    - The link of the images must be from Internet
 
 * Delete Post
    - Users can delete their own post by clicking the post (going to post detail page) and click 'delete'
 
 * Edit Post
    - Users can edit their own post by clicking the post (going to the post detail page) and click 'edit'
    - User will be redirected to the edit form page
    - User can edit the title, category, language and the content of the post
 
 * View Post Detail
    - Users can view the detail of any post (followed or owned) by clicking the title of the post
  
 * View Posts (List)
    - Users can view the list of post in the profile (own) and in the stream page (followed and own)
  
 * Like Post/Star
    - User can like the post of any user (in profile page, stream page, and search page)
 
 * Unlike Post/Unstar
    - User can unlike the liked post of any user (in profile page, stream page, and search page)
 
 ### Comment Module
 
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
   These are the posts that have the top ten highest number of likes and comments within the week. If the ranking of the 
   posts within the week is less than ten, the posts on the previous week will be included.
 
 
