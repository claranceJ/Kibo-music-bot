# Import the random library
import random

# List of music genres
genres = ["pop", "rock", "hip hop", "country", "jazz"]

# Prompt the user for their favorite music genre
favorite_genre = input("What is your favorite music genre? ")

# Check if the user's favorite genre is in the list
if favorite_genre in genres:
    print("Nice choice!")
else:
    print("Sorry, we don't have any recommendations for that genre.")

# Dictionary of top songs by genre
top_songs = {
    "pop": ["Driver's License", "Good 4 U", "Levitating"],
    "rock": ["Stairway to Heaven", "Bohemian Rhapsody", "Hotel California"],
    "hip hop": ["Lose Yourself", "Juicy", "N.Y. State of Mind"],
    "country": ["I Will Always Love You", "The Dance", "Friends in Low Places"],
    "jazz": ["Take Five", "In a Sentimental Mood", "My Favorite Things"],
}

# Loop to display the top songs for the user's favorite genre
if favorite_genre in top_songs:
    print("Here are the top songs in your favorite genre:")
    for song in top_songs[favorite_genre]:
        print("- " + song)
else:
    print("Sorry, we don't have any recommendations for that genre.")

# List of popular music streaming services
streaming_services = ["Spotify", "Apple Music", "Tidal", "Amazon Music"]

# Prompt the user for their favorite streaming service
favorite_service = input("What is your favorite music streaming service? ")

# Check if the user's favorite service is in the list
if favorite_service in streaming_services:
    print("Great choice!")
else:
    print("Sorry, we don't have any information about that streaming service.")

# Generate a random playlist of top songs for the user's favorite genre
if favorite_genre in top_songs:
    playlist = random.sample(top_songs[favorite_genre], 3)
    print("Here's a playlist of top songs in your favorite genre, generated just for you:")
    for i, song in enumerate(playlist):
        print(str(i+1) + ". " + song)
else:
    print("Sorry, we couldn't generate a playlist for that genre.")
