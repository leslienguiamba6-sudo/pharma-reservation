# Image de base pour faire tourner l'application
FROM python:3.14-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copie du fichier de requirements dans le conteneur
COPY requirements.txt requirements.txt

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code de l'application dans le conteneur
COPY app ./app

# Port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
