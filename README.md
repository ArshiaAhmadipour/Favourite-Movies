# My Media Vault  

https://favourite-movies-production.up.railway.app/

A beautiful, personal cinema database — every movie, series, anime, and animation I’ve ever loved, rated, and remembered.  
Built with Django + Tailwind CSS + TMDB API, because text files weren’t cutting it anymore.

### Features
- Gorgeous poster grid sorted by my personal rating (10 = masterpiece)
- Detailed pages with year, director, cast, and direct IMDb link
- "More like this" recommendations by category
- Dedicated Watchlist for everything I still need to see
- Fully responsive dark theme (because light mode is for cowards)

### Why I Built This
Because Rango is a perfect 10/10.  
Because I needed a place that feels like home for all the stories that shaped me.  
Because sometimes you just want to show the world your impeccable taste.

### Live Demo
https://my-media-vault.up.railway.app *(or your actual Railway link)*

### Tech Stack
- Django 5
- PostgreSQL (SQLite in dev)
- Tailwind CSS via CDN
- TMDB API for posters & metadata
- Deployed on Railway

### Local Development
```bash
git clone https://github.com/ArshiaAhmadipour/my-media-vault.git
cd my-media-vault
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_tmdb  # needs TMDB API key + VPN if blocked
python manage.py runserver
