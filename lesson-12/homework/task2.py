import requests
import random
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

api_key = 'a96e7b1b3b4ea5612a16b67490abeefd'  #API key
BASE_URL = "https://api.themoviedb.org/3"


def get_genres():  #getting list of all genres
    url = f"{BASE_URL}/genre/movie/list"
    response=requests.get(url, params={"api_key": api_key})

    if response.status_code == 200:
        genres = response.json().get('genres',[])
        return {genre["name"]: genre["id"] for genre in genres}
    else:
        print("Error fetching genres:", response.json())
        return {}

def get_movie(genre_id): #fetching a random movie by given genre_id
    url = f"{BASE_URL}/discover/movie?api_key={api_key}&with_genres={genre_id}&page={random.randint(1, 5)}"
    response = requests.get(url)

    if response.status_code == 200:
        movies = response.json().get('results',[])
        if movies:
            return random.choice(movies)
        print('Error fetching movies: ', response.json())
        return None

def recommend_movie():
    """Recommend a random movie based on user's chosen genre."""

    genres= get_genres()
    if not genres:
        return
    
    print("\nAvailable genres: ")
    for i,genre in enumerate(genres.keys(),1):
        print(f"{i}. {genre}")
    
    try:
        choice = int(input("Enter your choice: ")) - 1
        if choice < 0 or choice >= len(genres):
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    selected_genre = list(genres.keys())[choice]
    genre_id = genres[selected_genre]
    movie = get_movie(genre_id)
    if movie:
        print("\n🎬 Recommended Movie 🎬")
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview']}")
        print(f"Rating: {movie['vote_average']}/10")
        print(f"Release Date: {movie['release_date']}")
        print(f"More Info: https://www.themoviedb.org/movie/{movie['id']}")
    else:
        print("No movies found in this genre.")


if __name__ == "__main__":
    recommend_movie()

