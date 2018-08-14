# Tier One
An application for personal trainers.

## Application Summary

A friend who is personal trainer approached me on developing an for his clients. He would like a more effecient way to send clients their workouts. The app allows the trainer to create workouts and send them to multiple clients. The client will be able to see the workouts and comment on difficulties or general comments about the workout. 


## Tech Used

* Framework
  * Django
* Database
  * PostgresSQL
* ODM
  * Django
* Styling
  * CSS
  * Materialize


## Planning

I first started planning this app by meeting with the client and seeing what the basic functionality that was required. I then came started drawing wire frames as seen below.


![Wire frame](/main_app/static/images/wireframe.png)

I also used trello to define the deliverables and built individual checkbox tasks for each deliverable.

![trello](/main_app/static/images/trelloboard.png)

![checkbox](/main_app/static/images/trellocheckboard.png)

## Frontend Design

The intended design was to allow the trainer to quickly add workouts to different clients. This was done with a series of forms and drop down menus.

![dropdown](/main_app/static/images/dropdown.png)

 *Example of a dropdown menu with different clients*

 

  ## Backend Design

 The backend was done using a series of view methods that would retrieve and post data. The project had both a one to many and many to many relationship. 

 
  
  ![checkbox](/main_app/static/images/usermodelextended.png)

  *User Extended Model.*

  ![checkbox](/main_app/static/images/workoutmodel.png)

  *Workout Model.*

  ![checkbox](/main_app/static/images/excercisemodel.png)

  *Excercise Model.*

 

## Connecting Frontend with the Backend

The view methods also passed along the data to the front so it could be availble to render.

![checkbox](/main_app/static/images/backend.png)



## Future Features

Here is some of the features that we intend to implement, post cohort:

* Ability for clients to push comments to the trainer on a given workout.
* Ability for the trainer to label something as assigned in class or for homework.
* Tracking client participation for homework.
* Integrate a workout clock that corresponds to the total time of the workout.


## Challenges and Experiences

This was a very challenging project. Though the project is not very complex, understanding Django's database relations was difficult. Though the framework does a lot for the developer, it is very rigid and can cause a lot of setbacks. Thought this was a challening expeirence, I was able to learn a decent amount about the Django framework. In the future, I will probably rewrite this project in another framework. 

## Acknowledgments

I would like to thank Steve Peters and Kyle Van Bergen for their patience and sharing thier insight. I also like to thank the the rest of the class on helping me throughout this process.