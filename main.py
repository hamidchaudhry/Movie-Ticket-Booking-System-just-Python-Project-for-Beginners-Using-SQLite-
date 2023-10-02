import sqlite3

# Create a database connection
con = sqlite3.connect("movie.db")

# Create a cursor object
cur = con.cursor()

# Create the `book` table
cur.execute("""CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    Movie_ID text,
    Movie_Name text,
    Release_Date text,
    Director text,
    Cast text,
    Budget text,
    Duration text,
    Rating text
)""")

# Create the `tickets` table
cur.execute("""CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    name TEXT,
    movie_name TEXT,
    date TEXT,
    time TEXT
)""")

# Start a while loop
while True:

    # Create a menu
    print("Welcome to the movie database!")
    print("1. View movie list")
    print("2. Get a ticket")
    print("3. Add new record")
    print("4. Delete record")

    # Get the user's choice
    choice = input("Enter your choice: ")

    # Process the user's choice
    if choice == "1":
        # View the movie list
        cur.execute("SELECT * FROM book")
        movies = cur.fetchall()

        if not movies:
            print("Sorry, record is empty")
        else:
            for movie in movies:
                print(movie)

    elif choice == "2":
        # Get a ticket
        movie_name = input("Enter the movie name: ")

        cur.execute("SELECT * FROM book WHERE Movie_Name = ?", (movie_name,))
        movie = cur.fetchone()

        if not movie:
            print("Sorry, this movie is not available")
        else:
            name = input("Enter your name: ")
            date = input("Enter the date: ")
            time = input("Enter the time: ")

            cur.execute("INSERT INTO tickets (name, movie_name, date, time) VALUES (?, ?, ?, ?)", (name, movie_name, date, time))
            con.commit()

    elif choice == "3":
        # Add a new record
        movie_id = input("Enter the movie ID: ")
        movie_name = input("Enter the movie name: ")
        release_date = input("Enter the release date: ")
        director = input("Enter the director: ")
        cast = input("Enter the cast: ")
        budget = input("Enter the budget: ")
        duration = input("Enter the duration: ")
        rating = input("Enter the rating: ")

        cur.execute("INSERT INTO book (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (movie_id, movie_name, release_date, director, cast, budget, duration, rating))
        con.commit()

    elif choice == "4":
        # Delete a record
        movie_name = input("Enter the movie name: ")

        cur.execute("SELECT * FROM book WHERE Movie_Name = ?", (movie_name,))
        movie = cur.fetchone()

        if not movie:
            print("Sorry, record is empty")
        else:
            cur.execute("DELETE FROM book WHERE Movie_Name = ?", (movie_name,))
            con.commit()

    else:
        print("Invalid choice")

