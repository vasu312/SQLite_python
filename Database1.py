# import sqlite3 to Connect to the sqlite3 database
import sqlite3

#Creating new SQLite database
connection = sqlite3.connect("myDatabase.db")

cursor = connection.cursor()

#creating a new table (Movies)
myQuery_1 = ''' CREATE TABLE Movies(
                  Name TEXT,
                  Actor TEXT,
                  Actress TEXT,
                  Director TEXT,
                  ReleaseYear TEXT
                  );
            '''
# Execute the Query
cursor.execute(myQuery_1)

# Records
Records=[ ("Spider-Man: No Way Home","Tom Holland         ","Zendaya           ","Jon Watts          ","2021"),
          ("Interstellar           ","Matthew McConaughey ","Anne Hathaway     ","Christopher Nolan  ","2014"),
          ("Titanic                ","Leonardo DiCaprio   ","Kate Winslet      ","James Cameron      ","1997"),
          ("Passengers             ","Chris Pratt         ","Jennifer Lawrence ","Morten Tyldum      ","2016"),
          ("Deadpool               ","Ryan Reynolds       ","Morena Baccarin   ","Tim Miller         ","2016") ]

# Query to Inserting data into Movies Table
cursor.executemany('INSERT INTO Movies VALUES(?,?,?,?,?);',Records);

connection.commit()
connection.close()
