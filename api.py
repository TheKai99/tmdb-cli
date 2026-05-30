import requests
import os
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

headers = {
    "User-Agent": "Mozilla/5.0"
}

BASE_URL = "https://api.themoviedb.org/3"

def get_popular():

    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}"
    response = requests.get(url , headers=headers)

    data = response.json()
    
    print("=========== P O P U P L A R ========")
    for movie in data['results']:
        print(f"{movie['title']} : {movie['vote_average']}")


def get_now_playing():
    
    url = f"{BASE_URL}/movie/now_playing?api_key={API_KEY}"
    response = requests.get(url, headers=headers)

    data = response.json()
    
    print("=========== N O W - P L A Y I N G ========")
    for movie in data['results']:
        print(f"{movie['title']} : {movie['vote_average']}")


def get_top_rated():

    url = f"{BASE_URL}/movie/top_rated?api_key={API_KEY}"
    response = requests.get(url , headers=headers)

    data = response.json()
    
    print("=========== T O P - R A T E D  ========")
    for movie in data['results']:
        print(f"{movie["title"]} : {movie['vote_average']}")

def get_upcoming():

    url = f"{BASE_URL}/movie/upcoming?api_key={API_KEY}"
    response = requests.get(url , headers=headers)

    data = response.json()
    
    print("=========== U P C O M I N G ========")
    for movie in data['results']:
        print(f"{movie["title"]} : {movie['vote_average']}")
        




