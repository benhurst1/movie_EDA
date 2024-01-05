import json
import psycopg2
from datetime import datetime

def retrieve_details(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def store_details(data):
    conn = psycopg2.connect('dbname=movies user=benhurst')
    cur = conn.cursor()

    for index, movie in enumerate(data):
        if data[movie]['Response'] == 'False':
            continue
        title = data[movie]['Title']
        release_date = datetime.strptime(data[movie]['Released'], '%d %b %Y').date()
        release_year = release_date.year
        rating = data[movie]["Rated"]
        runtime = int(data[movie]['Runtime'].split(' ')[0])
        genres = data[movie]['Genre'].split(', ')
        directors = data[movie]['Director'].split(', ')
        writers = data[movie]['Writer'].split(', ')
        actors = data[movie]['Actors'].split(', ')
        revenue = None
        if data[movie]['BoxOffice'] != 'N/A':
            revenue = int(''.join(data[movie]['BoxOffice'].split(','))[1:])
        else:
            continue

        cur.execute("""INSERT INTO movies (id, title, release_year, release_date, rating, runtime, box_office) VALUES (%s, %s, %s, %s, %s, %s, %s)""", [index, title, release_year, release_date, rating, runtime, revenue])

        # inserting genres and movie_genres
        for genre in genres:
            cur.execute("""INSERT INTO genres (genre) VALUES (%s) ON CONFLICT (genre) DO UPDATE SET genre=EXCLUDED.genre RETURNING id""", [genre])
            id = cur.fetchone()
            if id != None:
                cur.execute("""INSERT INTO movies_genres (movie_id, genre_id) VALUES(%s, %s)""", [index, id])
        
        # inserting directors
        for director in directors:
            cur.execute("""INSERT INTO persons (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name=EXCLUDED.name RETURNING id""", [director])
            id = cur.fetchone()
            if id != None:
                cur.execute("""INSERT INTO movies_persons (movie_id, person_id, role) VALUES(%s, %s, %s)""", [index, id, 'director'])

        for writer in writers:
            cur.execute("""INSERT INTO persons (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name=EXCLUDED.name RETURNING id""", [writer])
            id = cur.fetchone()
            if id != None:
                cur.execute("""INSERT INTO movies_persons (movie_id, person_id, role) VALUES(%s, %s, %s)""", [index, id, 'writer'])

        for actor in actors:
            cur.execute("""INSERT INTO persons (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name=EXCLUDED.name RETURNING id""", [actor])
            id = cur.fetchone()
            if id != None:
                cur.execute("""INSERT INTO movies_persons (movie_id, person_id, role) VALUES(%s, %s, %s)""", [index, id, 'actor'])


        conn.commit()
    conn.close()

data = retrieve_details('extracted/movie_details.txt')
store_details(data)