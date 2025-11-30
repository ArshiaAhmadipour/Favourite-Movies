import json
from pathlib import Path
from django.core.management.base import BaseCommand
from movies.models import MediaItem

class Command(BaseCommand):
    help = 'Import media from media_data.json'

    def handle(self, *args, **options):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        json_path = base_dir / 'media_data.json'

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count = 0
        for item in data:
            MediaItem.objects.update_or_create(
                title=item['title'],
                defaults={
                    'category': item['category'],
                    'rating': item['rating'],
                    'watched': item['watched'],
                }
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} items!'))