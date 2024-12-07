 # Créer un environnement virtuel
 python -m venv venv                       

# Activer l'environnement :
# Sur Windows :
venv\Scripts\activate

# Sur macOS/Linux :
source venv/bin/activate

# Installer les dépendances à partir du fichier requirements.txt
pip install -r ecommerce/requirements.txt

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur de développement
python manage.py runserver 8000
