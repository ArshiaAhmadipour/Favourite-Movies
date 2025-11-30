import requests
from django.core.management.base import BaseCommand
from movies.models import MediaItem
from time import sleep

class Command(BaseCommand):
    help = 'Fetch TMDB data (poster, year, director, cast, IMDb) for all items'

    def handle(self, *args, **options):
        API_KEY = "423490f0a46d4efc899d90c8c823ad8d"
        BASE_URL = "https://api.themoviedb.org/3"
        IMG_BASE = "https://image.tmdb.org/t/p/w500"

        items = MediaItem.objects.all()
        total = items.count()

        for idx, item in enumerate(items, 1):
            query = f"{item.title} {item.year or ''}".strip()
            media_type = "movie" if item.category in ["movie", "animation"] else "tv"

            search_url = f"{BASE_URL}/search/{media_type}"
            params = {"api_key": API_KEY, "query": query}
            resp = requests.get(search_url, params=params).json()

            results = resp.get("results", [])
            if not results:
                self.stdout.write(self.style.WARNING(f"[{idx}/{total}] Not found: {item.title}"))
                sleep(0.25)
                continue

            tmdb = results[0]
            tmdb_id = tmdb["id"]

            details = requests.get(f"{BASE_URL}/{media_type}/{tmdb_id}", params={"api_key": API_KEY}).json()
            credits = requests.get(f"{BASE_URL}/{media_type}/{tmdb_id}/credits", params={"api_key": API_KEY}).json()

            director = next((c["name"] for c in credits.get("crew", []) if c["job"] == "Director"), None)

            cast_list = [c["name"] for c in credits.get("cast", [])[:4]]
            cast = ", ".join(cast_list) if cast_list else None

            year = int(details.get("release_date", "")[:4] or details.get("first_air_date", "")[:4] or 0) or None

            imdb_id = details.get("imdb_id")
            imdb_url = f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else None

            poster = IMG_BASE + tmdb.get("poster_path") if tmdb.get("poster_path") else None

            item.tmdb_id = tmdb_id
            item.poster_path = poster
            item.year = year
            item.director = director
            item.cast = cast
            item.imdb_url = imdb_url
            item.save()

            self.stdout.write(self.style.SUCCESS(f"[{idx}/{total}] {item.title}"))
            sleep(0.25)

        self.stdout.write(self.style.SUCCESS("All items updated with TMDB data!"))