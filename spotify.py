import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_podcasts(mood, client_id, client_secret):
    # Mood → topic mapping
    mood_query_map = {
        "happy": "funny",
        "sad": "self help",
        "angry": "calm stories",
        "neutral": "trending podcasts",
        "surprise": "mystery",
        "disgust": "wellness"
    }

    query = mood_query_map.get(mood.lower(), "trending")

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    print(f"🎧 Fetching Spotify podcasts for mood: {mood} → query: {query}")
    
    results = sp.search(q=query, type='show', limit=3)
    podcasts = []

    for show in results['shows']['items']:
        podcasts.append({
            "name": show['name'],
            "publisher": show['publisher'],
            "description": show['description'],
            "url": show['external_urls']['spotify']
        })

    return podcasts
