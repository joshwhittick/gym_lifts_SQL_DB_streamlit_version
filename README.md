# gym_lifts_SQL_DB_streamlit_version

**Development of https://github.com/joshwhittick/gym_lifting_tracking as a web app using https://streamlit.io to host and https://heroku.com/ for a PostgreSQL DB**

files here are for the purpose of launcing app on streamlit and not for running on personal machine with MySQL DB

**notes on files included:**

**DB_SQL_STREAMLIT_FUNCTIONS.py**
deffinition of functions required for the streamlit web app 

**Lifting_DB_Main_Page.py**
main page for streamlit web app launching

**make_SQL_DB_with_pyth.py**
initial python code for making table in heroku DB although on their website they state:

"Starting November 28th, 2022, free Heroku Dynos, free Heroku Postgres, and free Heroku Data for Redis® will no longer be available."

so will have to transition to different cloud based web DB which is hard given i can only use free stuff lol just caus dont wanna be running MySQL for public use on my own machine innit

**page/Insert to Database.py**
streamlit page defining widgets to input data and calling the necessary functions to write to the DB

**pages/Interogate Database.py**
streamlit webpage defining widgets where user can query DB, file calls necessary functions to connect to DB and express the results as text and graphs 

this could b improved to be more "valuable" i.e. more relevant graphs or other output formats like .csv files blah blah blah

**requirements.txt**
for streamlit to "pip install" the appropriate packages
