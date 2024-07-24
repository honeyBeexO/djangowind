import json
from django.core.management.base import BaseCommand # type: ignore
from core.models import Sector
from django.conf import settings  # type: ignore

class Command(BaseCommand):
    help = 'Load activities from a JSON file into the database'

    def handle(self, *args, **kwargs):
        file_path = settings.BASE_DIR / 'static/json/base/activities.json'  # Adjust the path to your JSON file
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                for item in data:
                    Sector.objects.update_or_create(
                        sub_id=item['id'],
                        defaults={
                            'name': item['name'],
                            'description': item['description'],
                            'connector_activity_id': item.get('connector_activity_id'),
                            'has_children': item['has_children'],
                            'to_be_reviewed': item['to_be_reviewed'],
                            'type': item.get('type'),
                            'jqpa': item.get('jqpa'),
                            'post_payment': item.get('post_payment'),
                        }
                    )

            self.stdout.write(self.style.SUCCESS('Successfully imported activities'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Error decoding JSON"))