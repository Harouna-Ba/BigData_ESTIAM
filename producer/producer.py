from kafka import KafkaProducer
import json
import time
import requests
import os
import base64
 
def json_serializer(data):
    return json.dumps(data).encode('utf-8')
 
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=json_serializer
)
 
CLIENT_ID = '6745488901e446d4ba752aec03aca296'
CLIENT_SECRET = '05f6a3e76c49493da989eb3b5adb6683'
AUTH_URL = 'https://accounts.spotify.com/api/token'
 
# Obtenir un token d'accès pour l'API Spotify
def get_access_token(client_id, client_secret):
    try:
        auth = f"{client_id}:{client_secret}"
        auth_encoded = base64.b64encode(auth.encode()).decode()
        response = requests.post(
            AUTH_URL,
            data={'grant_type': 'client_credentials'},
            headers={'Authorization': f"Basic {auth_encoded}"}
        )
        if response.status_code != 200:
            print(f"Erreur HTTP {response.status_code}: {response.text}")
        response.raise_for_status()
        token_info = response.json()
        return token_info['access_token']
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'obtention du token : {e}")
        return None
 
# Récupération des artistes depuis Spotify
def fetch_spotify_artists(access_token):
    search_endpoint = 'https://api.spotify.com/v1/search'
    try:
        response = requests.get(
            search_endpoint,
            headers={'Authorization': f'Bearer {access_token}'},
            params={
                'q': 'a',  # Mot-clé pour rechercher les artistes (ici, 'a' pour obtenir un large éventail)
                'type': 'artist',
                'limit': 10  # Nombre d'artistes à récupérer
            }
        )
        if response.status_code != 200:
            print(f"Erreur HTTP {response.status_code}: {response.text}")
        response.raise_for_status()
        data = response.json()
        artists = []
        for artist in data['artists']['items']:
            artists.append({
                'artist_name': artist['name'],
                'followers': artist['followers']['total'],
                'genres': artist['genres'],
                'timestamp': time.time()
            })
        return artists
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête Spotify : {e}")
        return None
 
# Initialisation du token
access_token = None
token_expiration = 0
 
while True:
    # Vérifiez si le token est expiré ou inexistant
    if not access_token or time.time() > token_expiration:
        access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
        if access_token:
            token_expiration = time.time() + 3600  # Expire dans 1 heure
        else:
            print("Impossible d'obtenir un token valide. Nouvelle tentative dans 10 secondes.")
            time.sleep(10)
            continue
 
    # Récupération des artistes Spotify
    messages = fetch_spotify_artists(access_token)
    if messages:
        for message in messages:
            print(f"Producing message: {message}")
            try:
                producer.send('spotify_topic', message)
                producer.flush()  # Assure l'envoi du message
            except Exception as e:
                print(f"Erreur lors de l'envoi du message à Kafka : {e}")
    else:
        print("Aucun message à produire en raison d'une erreur lors de la récupération des données.")
 
    time.sleep(10)