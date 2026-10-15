#Petite application utilisant des variables d'environnement

import os

from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
app_port = os.getenv("APP_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

if not db_password:
    raise ValueError("Le mot de passe est absent du fichier .env.")

print(f"Application : {app_name}")
print(f"Port : {app_port}")
print(f"Utilisateur : {db_user}")
print("Mot de passe chargé de manière sécurisée.")