import psycopg2

conn = psycopg2.connect('dbname=movies user=benhurst')
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS movies CASCADE")
cur.execute("DROP TABLE IF EXISTS genres CASCADE")
cur.execute("DROP TABLE IF EXISTS movies_genres CASCADE")
cur.execute("DROP TABLE IF EXISTS persons CASCADE")
cur.execute("DROP TABLE IF EXISTS roles CASCADE")
cur.execute("DROP TABLE IF EXISTS person_roles CASCADE")
cur.execute("DROP TABLE IF EXISTS movies_persons CASCADE")
conn.commit()
conn.close()