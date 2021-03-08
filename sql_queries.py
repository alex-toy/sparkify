# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
    songplay_id SERIAL PRIMARY KEY, 
    start_time date NOT NULL, 
    user_id text NOT NULL, 
    level text, 
    song_id text, 
    artist_id text, 
    session_id text, 
    location text, 
    user_agent text
);
""")

user_table_create = ("""
CREATE TABLE users (
    user_id text PRIMARY KEY, 
    first_name text NOT NULL, 
    last_name text NOT NULL, 
    gender text, 
    level text
);
""")

song_table_create = ("""
CREATE TABLE songs (
    song_id text PRIMARY KEY, 
    title text NOT NULL, 
    artist_id text, 
    year int, 
    duration numeric
);
""")

artist_table_create = ("""
CREATE TABLE artists (
    artist_id text PRIMARY KEY, 
    name text NOT NULL, 
    location text, 
    latitude text, 
    longitude text
);
""")

time_table_create = ("""
CREATE TABLE time (
    start_time date PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday int
);
""")

add_constraints_query = ("""
ALTER TABLE songplays 
ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users (user_id) MATCH FULL,
ADD CONSTRAINT fk_song_id FOREIGN KEY (song_id) REFERENCES songs (song_id) MATCH FULL,
ADD CONSTRAINT fk_artist_id FOREIGN KEY (artist_id) REFERENCES artists (artist_id) MATCH FULL,
ADD CONSTRAINT fk_start_time FOREIGN KEY (start_time) REFERENCES time (start_time) MATCH FULL;
""")
    

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT song_id, songs.artist_id 

FROM songs
JOIN artists ON (songs.artist_id = artists.artist_id)

WHERE title = %s AND name = %s AND duration = %s;
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create, add_constraints_query]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]