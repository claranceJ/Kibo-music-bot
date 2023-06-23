# Import the time and random library
import time
import random

# escape code \033[34m sets the console text color to blue. The escape code \033[0m is added after the last line to reset the text color back to the default.

print("\033[34m" + 
      "                 **************************\n"
      "                 *** Welcome to KiboMusicBot***\n"
      "                 **************************\n"
      "\n")

# Intro text stored as a variable  to allow delay print

intro_text = \
             "Hello there! I am MusicBot from kibo, an AI-powered assistant dedicated to helping you discover new music based on your preferences.\n\n" \
             "With my expertise, I can provide you with top song recommendations,\n"\
             "generate a playlist based on your favorite genre, and help you find \nthe best music streaming service to suit your needs. \n \033[0m"\

# for loop to print the intro text with some delay,the end='' argument is to prevent the console from adding a newline character. The set flush=True is to immediately flush the output and show the text as it is printed

for char in intro_text:
    print(char, end='', flush=True)
    time.sleep(0.03)

#List of music genres

genres = ["afrobeat","pop", "reggea", "rocks", "rnb", "blues"  "soul" "drill" "hip hop", "country", "jazz"]

# Prompt the user for their favorite music genre
favorite_genre = input("What is your favorite music genre🎶 ? ")

# Check if the user's favorite genre is in the list
if favorite_genre in genres:
    print("Nice choice!")
else:
    print("Sorry, we don't have any recommendations for that genre.")

# Dictionary of top songs by genre
top_songs ={
    "afrobeat": ["Calm Down","Peru","Essence","Last Last","Rush"],
    "pop": ["Single Ladies","Uptown Funk","Toxic","Rolling in the Deep","Firework" "Call Me Maybe"],
    "reggea": ["Get Up","I Shot the Sheriif","No Woman, No Cry","Three Little Birds","The Harder They Come"],
    "rock": ["I Love Rock 'N Roll","Purple Haze","Slow Ride","La Grange","You Really Got Me"],
    "rnb": ["Say My Name", "Untitled(How Does it Feel)", "The Boy is Mine","Waterfalls","Let's Stay Together"],
    "blues": ["Baby Please Don't Go","Cross Road Blues","Boogie Chillen","The Thrill Is Gone","Boom Boom", "Sweet Home Chicago", "Boen Under a bad Sign","Hoochie Coochie Man"],
    "soul": ["Heat Wave","Soul Man","When a Man Loves a Woman","Let's Stay Together","Walk on By"],
    "drill": ["My Everything","Lets Lurk","Big Drip","Lets Get it","Commitment Issues"],
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
streaming_services = ["spotify", "apple Music", "tidal", "amazon music"]

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
