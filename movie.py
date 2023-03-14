# Import the random library
import random

# List of movie genres
genres = ["action", "comedy", "drama", "horHulror", "romance"]

# Prompt the user for their favorite movie genre
favorite_genre = input("What is your favorite movie genre? ")

# Check if the user's favorite genre is in the list
if favorite_genre in genres:
    print("Great choice!")
else:
    print("Sorry, we don't have any recommendations for that genre.")

# Dictionary of top movies by genre
top_movies = {
    "action": ["Die Hard", "The Matrix", "Terminator 2"],
    "comedy": ["Airplane!", "This Is Spinal Tap", "The Big Lebowski"],
    "drama": ["The Godfather", "Schindler's List", "Forrest Gump"],
    "horror": ["The Shining", "Psycho", "The Exorcist"],
    "romance": ["Casablanca", "When Harry Met Sally", "The Notebook"],
}

# Loop to display the top movies for the user's favorite genre
if favorite_genre in top_movies:
    print("Here are the top movies in your favorite genre:")
    for movie in top_movies[favorite_genre]:
        print("- " + movie)
else:
    print("Sorry, we don't have any recommendations for that genre.")

# List of popular movie streaming services
streaming_services = ["Netflix", "Hulu", "Amazon Prime Video", "Disney+"]

# Prompt the user for their favorite streaming service
favorite_service = input("What is your favorite movie streaming service? ")

# Check if the user's favorite service is in the list
if favorite_service in streaming_services:
    print("Great choice!")
else:
    print("Sorry, we don't have any information about that streaming service.")

# Generate a random list of recommended movies for the user's favorite genre
if favorite_genre in top_movies:
    recommended_movies = random.sample(top_movies[favorite_genre], 3)
    print("Here are some recommended movies in your favorite genre, generated just for you:")
    for i, movie in enumerate(recommended_movies):
        print(str(i+1) + ". " + movie)
else:
    print("Sorry, we couldn't generate any recommendations for that genre.")
