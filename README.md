FDM
===

### Program
The program is a gamified version of the FDM website. It allows users to register for 
an account; once logged in, users can access the games page, where they are presented 
with games to choose from and the leaderboard, where user high scores are displayed.

### Running the program
Please install any missing libraries from the `requirements.txt` file before running the 
program. The program will run without connecting to the database, but most functionality
will be disabled as it is directly linked to the database. For instructions on how to connect
to the databse, see the `Database` section below.  
To start the program, simply run `app.py` and you will be presented with a link to the
website.

### Program structure
The program consists of multiple files, the main one being `app.py`. This file 
calls functions from other modules as well as references HTML templates in the 
`Templates` folder. This folder in turn references items from the `static` folder, 
where images and CSS files are contained. `app.py` is extended by other python files, such as 
`games/bluepirnts.py` and `user/views.py` where most of the program's functionality is handled,
including login, leaderboards and games.

### Database
The provided MariaBD database was used in the project.  
The program is set up using the localhost in the program, as there were issues with
the remote host.  
##### - Connection  
To connect to the database, simply use team_4 login details in the `Database` tab of the IDE; 
the SSH should be using the Local port `3333`. This port is used in the code and thus can not
be different.
##### - Layout
The database consists of two tables: `Users` and `Scores`. The `Users` table stores all 
necessary user data, including login details and personal information. The `Scores` table is 
linked to the `Users` table via a foreign key. This table stores all scores from all users and
is used when generating the leaderboard.

### Repository
All project files can be found using the following link:  
https://github.com/Newcastle-University-CSC2033-Group04/FDM

### Program Authors
Program developed by Team 4:  
• Charlotte Bale  
• Benas Bulota  
• Yuan Liu  
• William Moses  
• Abdulla Rashed

Newcastle, 2022