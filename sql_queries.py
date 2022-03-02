# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS;"
user_table_drop = "DROP TABLE IF EXISTS USERS;"
song_table_drop = "DROP TABLE IF EXISTS SONGS;"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS;"
time_table_drop = "DROP TABLE IF EXISTS TIME;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS SONGPLAYS(
songplay_id SERIAL PRIMARY KEY,  
start_time BIGINT NOT NULL,
user_id INT NOT NULL,  
level VARCHAR NOT NULL, 
song_id VARCHAR,  
artist_id VARCHAR, 
session_id INT, 
location VARCHAR, 
user_agent VARCHAR 
);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS USERS(
user_id int PRIMARY KEY,
first_name VARCHAR NOT NULL, 
last_name VARCHAR NOT NULL, 
gender VARCHAR, 
level VARCHAR 
);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS(
song_id VARCHAR PRIMARY KEY, 
title VARCHAR(255) NOT NULL, 
artist_id VARCHAR(255) NOT NULL, 
year INT, 
duration FLOAT NOT NULL
);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS ARTISTS(
artist_id VARCHAR(255) PRIMARY KEY, 
name VARCHAR(255) NOT NULL, 
location VARCHAR, 
latitude FLOAT, 
longitude FLOAT
);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS TIME(
start_time TIME PRIMARY KEY, 
hour INT NOT NULL, 
day INT NOT NULL, 
week INT NOT NULL, 
month INT NOT NULL, 
year INT NOT NULL, 
weekday INT NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id) DO NOTHING 
;""")

user_table_insert = ("""INSERT INTO USERS(user_id, first_name, last_name, gender, level) \
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT(user_id) DO UPDATE SET level = excluded.level
;""")

song_table_insert = ("""INSERT INTO SONGS(song_id, title, artist_id, year, duration) \
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
;""")

artist_table_insert = ("""INSERT INTO ARTISTS(artist_id, name, location, latitude, longitude) \
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
;""")


time_table_insert = ("""INSERT INTO TIME(start_time, hour, day, week, month, year, weekday) \
VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
;""")


# FIND SONGS

song_select = ("""SELECT s.song_id songid, a.artist_id artistid \
FROM \
    songs s \
JOIN \
    artists a \
ON \
    s.artist_id = a.artist_id \
WHERE \
    s.title = %s and a.name = %s and s.duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
