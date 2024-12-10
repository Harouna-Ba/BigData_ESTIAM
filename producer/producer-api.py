from kafka import KafkaProducer
import json
import time
import requests
import os

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Création du producer qui pointe vers notre cluster Kafka (localhost:9092)
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=json_serializer
)

while True:
    API_KEY = 'xxxxxx'
    CITY = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"
    try:
        response = requests.get(url)
        data = response.json()
        currentTemp = data['current']['temp_c']

        message = {
            'temperature': currentTemp,
            'timestamp': time.time(),
            'city':'Paris'
        }
        print(f"Producing message: {message}")
        producer.send('test_topic', message) # Utilise le producer pour envoyer une objet
        producer.flush() # Demande au producer d'attendre que le message soit bien envoyé
        time.sleep(2) # toute les 2 secondes
    except Exception as e:
        print(f"Unexpected error: {e}")