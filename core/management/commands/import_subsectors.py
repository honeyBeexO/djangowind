import json
import os
from django.core.management.base import BaseCommand # type: ignore
from core.models import Sector, SubSector
from django.conf import settings  # type: ignore
from pathlib import Path

class Command(BaseCommand):
    help = 'Import sub-sectors from predefined JSON files'

    def handle(self, *args, **options):
        payloads = [
            '1.json', '2.json', '60.json', '132.json', '194.json',
            '230.json', '282.json', '313.json', '329.json', '383.json',
            '398.json', '418.json', '522.json', '523.json', '541.json',
            '594.json', '782.json'
        ]
        base_path = Path(settings.BASE_DIR) / 'static/json/'

        for json_file in payloads:
            file_path = base_path / json_file
            self.stdout.write(self.style.NOTICE(f'Processing file: {file_path}'))

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    
                    for item in data:
                        try:
                            parent_sector = Sector.objects.get(sub_id=item['parent_id'])
                        except Sector.DoesNotExist:
                            self.stdout.write(self.style.ERROR(f"Sector with sub_id {item['parent_id']} does not exist. Skipping sub-sector {item['name']}"))
                            continue

                        # Create or update the SubSector
                        subsector, created = SubSector.objects.update_or_create(
                            sub_id=item['id'],
                            defaults={
                                'name': item['name'],
                                'description': item['description'],
                                'parent': parent_sector,
                                'connector_activity_id': item.get('connector_activity_id'),
                                'has_children': item.get('has_children', False),
                                'to_be_reviewed': item.get('to_be_reviewed', False),
                                'type': item.get('type', None),
                                'jqpa': item.get('jqpa', None),
                                'post_payment': item.get('post_payment', None),
                            }
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f"Created sub-sector {subsector.name}"))
                        else:
                            self.stdout.write(self.style.SUCCESS(f"Updated sub-sector {subsector.name}"))

            except FileNotFoundError:
                self.stdout.write(self.style.ERROR(f"File {file_path} not found. Skipping."))
            except json.JSONDecodeError:
                self.stdout.write(self.style.ERROR(f"File {file_path} is not valid JSON. Skipping."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to process file {file_path}: {str(e)}"))