# DROP TABLES

songplay_table_drop = "drop table songplay;"
user_table_drop = "drop table user;"
song_table_drop = "drop table song;"
artist_table_drop = "drop table artist;"
time_table_drop = "drop table time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplay (
    songplay_id int, 
    start_time date, 
    user_id int, 
    level int, 
    song_id int, 
    artist_id int, 
    session_id int, 
    location text, 
    user_agent text
);
""")

user_table_create = ("""
CREATE TABLE user (
    user_id int, 
    first_name text, 
    last_name text, 
    gender text, 
    level text
""")

song_table_create = ("""
CREATE TABLE song (
    song_id int, 
    title text, 
    artist_id int, 
    year date, 
    duration numeric
""")

artist_table_create = ("""
CREATE TABLE artist (
    artist_id text, 
    name text, 
    location text, 
    latitude text, 
    longitude text
""")

time_table_create = ("""
CREATE TABLE time (
    start_time date, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday int
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO user (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
INSERT INTO song (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
INSERT INTO artist (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""

""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]