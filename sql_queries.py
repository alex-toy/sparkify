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
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]