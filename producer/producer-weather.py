from kafka import KafkaProducer
import json
import time
import requests
from bs4 import BeautifulSoup

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Création du producer qui pointe vers notre cluster Kafka (localhost:9092)
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=json_serializer
)

while True:

    url = "https://weather.com/fr-FR/temps/aujour/l/FRXX0076:1:FR"
    try:
        response = requests.get(url)
        soup= BeautifulSoup(response.text, 'lxml')
        # element HTML : <span data-testid="TemperatureValue"> </...>
        temp_element = soup.find('span',{'data-testid':'TemperatureValue'})
        temp_el_clean = temp_element.text.replace('°','') # Parsing
        print(temp_el_clean)
        currentTemp= int(temp_el_clean)
        message = {
                'temperature': currentTemp,
                'timestamp': time.time(),
                'city':'Paris'
        }
        print(f"Producing message: {message}")
        producer.send('test_topic', message) # Utilise le producer pour envoyer une objet
        producer.flush() # Demande au producer d'attendre que le message soit bien envoyé
        time.sleep(2)
    except Exception as e:
        print(f"Unexpected error: {e}")