# Le container de départ, que je veux modifier
FROM python:3.9-slim

# Définition du dossier de travail ici /app
WORKDIR /app

# Copy du fichier requirements.txt vers /app (le point fait référence à ce dossier)
COPY requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Lancement du projet
CMD ["python" ,"producer.py"]