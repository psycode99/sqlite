import sqlite3

# CREATING DATABASE
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# CREATE TABLE
# cursor.execute("""CREATE TABLE albums
#                (title text, artist text, release_date text,
#                publisher text, media_type text)
#                """) # title= column name, text=data type

# INSERTING VALUES INTO TABLE
# cursor.execute("""INSERT INTO albums
#                VALUES ('Glow', 'Andy hunter', '7/24/2012',
#                'Xplore records', 'MP3')
#                """)
#
# cursor.execute("INSERT INTO albums VALUES"
#                "('omerta', 'drake', '10/10/2021',"
#                "'sony', 'MP3')"
#                )
# # save data to database
# conn.commit()

# INSERT MULTIPLE RECORDS USING SECURE '?' METHOD
# albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
#           ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
#           ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TF\14Kmusic', 'CD'),
#           ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD'),
#           ('Life is good', 'Future', '4/10/2020', 'FOX', 'MP3')]
#
# cursor.executemany('INSERT INTO albums VALUES (?,?,?,?,?)', albums)
# the number of '?' indicates the number of columns of the table
# conn.commit()

# UPDATING RECORDS IN DATABASE
# sql_code = """
# UPDATE albums
# SET artist = 'John Doe'
# WHERE artist = 'Andy Hunter'
# """
#
# artist_update = """
# UPDATE albums
# SET artist = 'Drake'
# WHERE artist = 'Future'
# """
#
# cursor.execute(sql_code)
# cursor.execute(artist_update)
# conn.commit()

# DELETE RECORD FROM THE DATABASE
# sql_to_delete = """
# DELETE FROM albums
# WHERE title = 'Life is good'
# """
# cursor.execute(sql_to_delete)
# conn.commit()

# ADDING NEW RECORD
# sql_to_add = """
# INSERT INTO albums
# VALUES ('One Dance', 'Drake', '12/07/2010', 'Sony', 'MP3')
# """
# cursor.execute(sql_to_add)
# conn.commit()

# BASIC SQLITE QUERIES
sql_query = """
SELECT * FROM albums WHERE artist=? 
"""
cursor.execute(sql_query, ['Drake'])  # select all from albums table
# where artist column is = Drake

print(cursor.fetchall())  # use fetchall() to fetch all instances with
#  given query. Use fetchone() to fetch first instance of given query

# selects row id and all from albums table by order of title column alpphabetically
print("\nHere's a listing of all the records in the table:\n")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY title"):
    print(row)

print("\nResults from a LIKE query:\n")
# selects all rows with title that start like 'o'
sql = """
SELECT * FROM albums
WHERE title LIKE 'O%'
"""   # the % sign is a wildcard operator

cursor.execute(sql)
print(cursor.fetchall())