import random

# List of movie titles
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Forrest Gump", "Star Wars", "Jurassic Park", "The Lion King", "Titanic", "Indiana Jones and the Raiders of the Lost Ark", "Back to the Future"]

# List of genres
genres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller"]

# List of years
years = list(range(1930, 2022))

# List of ratings
ratings = list(range(1, 11))

# List of movie dicts
movies_data = []

# Generate 50 random movies
for i in range(50):
    movie = {}
    movie["title"] = random.choice(movies)
    movie["genre"] = random.choice(genres)
    movie["year"] = random.choice(years)
    movie["rating"] = random.choice(ratings)
    movies_data.append(movie)

# Define function to search for movies
def search_movies(title=None, genre=None, year=None, rating=None):
    results = []
    for movie in movies_data:
        if title and title.lower() not in movie["title"].lower():
            continue
        if genre and genre.lower() != movie["genre"].lower():
            continue
        if year and year != movie["year"]:
            continue
        if rating and rating != movie["rating"]:
            continue
        results.append(movie)
    return results

# Define function to print movie details
def print_movie(movie):
    print("Title: ", movie["title"])
    print("Genre: ", movie["genre"])
    print("Year: ", movie["year"])
    print("Rating: ", movie["rating"])

# Welcome message
print("Welcome to Movie Finder! We have a collection of 50 movies for you to browse.\n")

# Loop for searching movies
while True:
    # Get user input for search criteria
    print("Search movies by:\n1. Title\n2. Genre\n3. Year\n4. Rating\n5. Quit")
    choice = input("Enter your choice (1-5): ")
    if choice == "5":
        break
    elif choice == "1":
        title = input("Enter the movie title: ")
        results = search_movies(title=title)
    elif choice == "2":
        genre = input("Enter the movie genre: ")
        results = search_movies(genre=genre)
    elif choice == "3":
        year = int(input("Enter the movie year: "))
        results = search_movies(year=year)
    elif choice == "4":
        rating = int(input("Enter the movie rating (1-10): "))
        results = search_movies(rating=rating)
    else:
        print("Invalid choice. Please try again.")
        continue
    
    # Print search results
    if len(results) == 0:
        print("No results found.")
    else:
        print("Search results:")
        for movie in results:
            print_movie(movie)
