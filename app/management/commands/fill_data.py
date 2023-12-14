from django.core.management.base import BaseCommand, CommandError
from django.db import models
import re
import csv
from pathlib import Path 
from app.models import Zno
from app.utils import get_primary_key


class Command(BaseCommand):
    FILL_DATA_RELATIVE_PATH = 'fill_data'
    help = "Filling data from CSV files to DB table ZNO"
    
    def handle(self, *args, **options):
            try:
                self.stdout.write(
                    self.style.SUCCESS('Started fillind ZNO DB table by data')
                )
                for file_path in Path(self.FILL_DATA_RELATIVE_PATH).iterdir():
                    print(f"Filling data from {file_path.name}")
                    with open(file_path, 'r', encoding='windows-1251') as file:
                        reader = csv.DictReader(file, delimiter=';')

                        primary_key_name = get_primary_key(Zno)
                        

                        if not primary_key_name:
                            raise Exception('Not found primary key in ZNO DB table model')
                        
                        match = re.search(r'\d{4}', file_path.name) # get year from name of current csv file
                        if not match:
                            raise Exception(f"Can't get year from name of CSV file: {file_path}")
                
                        year = int(match.group())
                        
                        for row in reader:
                            primary_key_value = row[primary_key_name]

                            model_data = {
                                'year': year,
                            }

                            for header, value in row.items():
                                if header != primary_key_name:
                                    if value == 'null':
                                        value = None
                                    elif isinstance(getattr(Zno, header).field, models.FloatField): # handle float values
                                        value = float(value.replace(',', '.'))
                                    
                                    
                                        
                                    model_data[header] = value
                            
                            obj, created = Zno.objects.get_or_create(**{primary_key_name: primary_key_value}, defaults=model_data)

                            if not created: # update existing
                                for key, value in model_data.items():
                                    setattr(obj, key, value)
                                obj.save()
            except Exception as e:
                raise CommandError(f'Error while filling data to ZNO DB table: {e}')

            self.stdout.write(
                self.style.SUCCESS('Successfully filled data to ZNO DB table')
            )