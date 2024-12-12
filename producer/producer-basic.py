from kafka import KafkaProducer
import json
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Création du producer qui pointe vers notre cluster Kafka (localhost:9092)
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=json_serializer
)

counter = 0
while True:
    message = {
        'id': counter,
        'message': 'Bonjour Kafka!',
        'timestamp': time.time()
    }
    print(f"Producing message: {message}")
    producer.send('test_topic', message) # Utilise le producer pour envoyer une objet
    producer.flush() # Demande au producer d'attendre que le message soit bien envoyé
    time.sleep(2)
    counter+=1