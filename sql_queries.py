# DROP TABLES

songplay_table_drop = "DROP TABLE SONGPLAYS;"
user_table_drop = "DROP TABLE USERS;"
song_table_drop = "DROP TABLE SONGS;"
artist_table_drop = "DROP TABLE ARTISTS;"
time_table_drop = "DROP TABLE TIME;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS SONGPLAYS(
songplay_id SERIAL,  
start_time BIGINT,
user_id INT,  
level VARCHAR, 
song_id VARCHAR,  
artist_id VARCHAR, 
session_id INT, 
location VARCHAR, 
user_agent VARCHAR  
);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS USERS(
user_id int,
first_name varchar, 
last_name varchar, 
gender varchar, 
level varchar
);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS(
song_id varchar NOT NULL, 
title varchar(255) NOT NULL, 
artist_id varchar(255) NOT NULL, 
year int, 
duration FLOAT
);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS ARTISTS(
artist_id varchar(255) NOT NULL, 
name varchar(255) NOT NULL, 
location varchar, 
latitude FLOAT, 
longitude FLOAT
);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS TIME(
start_time TIME, 
hour INT, 
day INT, 
week INT, 
month INT, 
year INT, 
weekday INT
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO USERS(user_id, first_name, last_name, gender, level) \
VALUES(%s, %s, %s, %s, %s);
""")

song_table_insert = ("""INSERT INTO SONGS(song_id, title, artist_id, year, duration) \
VALUES(%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""INSERT INTO ARTISTS(artist_id, name, location, latitude, longitude) \
VALUES(%s, %s, %s, %s, %s);
""")


time_table_insert = ("""INSERT INTO TIME(start_time, hour, day, week, month, year, weekday) \
VALUES(%s, %s, %s, %s, %s, %s, %s);
""")


# FIND SONGS

song_select = ("""SELECT s.song_id songid, a.artist_id artistid \
FROM songs s \
JOIN artists a on s.artist_id = a.artist_id \
WHERE s.title = %s and a.name = %s and s.duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
