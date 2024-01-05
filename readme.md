## Movie EDA

I wanted to create a project where I used a few different skills I have learned from data ingestion, transformation, storage and then visualise a few plots.

# Ingestion

I started by finding an API from a website called https://www.omdbapi.com/
You can search for movies using imdb id numbers. So my first job was to obtain a list of these id's.

In [extract.py](extract.py) I first create a list of urls from a public list of the top 1000 highest grossing movies worldwide.
Then I use BeautifulSoup and grequests (for concurrency) to gather all of the pages and parse through them of the id's of each of these movies.
I next create a new list of requests with each of the id's and my API key for omdbapi.com
Using grequests again, I can request all of the urls at once and dump them as a json into a txt file.

# Transform and Storage

Once all the details are in [txt file](extracted/movie_details.txt), I can open it up in a new script and begin to transform the data ready to be stored in a database.
[transform.py](transform.py) loads the data, creates a connection to the database, and then each item in the dictionary it will sort out the data i'd like into different tables of the database.
The aim was to reduce duplicate genres, actors and directors and use join tables to link movies with cast / crew and genres together.

# EDA

[eda.ipynb](eda.ipynb) is my document for looking through the data now stored, creating a few plots of interesting ideas I had.
