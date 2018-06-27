from django.db import models
from django.utils import timezone



class Combine(models.Model):
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    crop = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    production = models.CharField(max_length=200)
    yields = models.CharField(max_length=200)
    yield_units = models.CharField(max_length=200)
    
    class Meta:
        managed=False
        db_table='area_production_yield'
    
class agro_chemical_abbreviations(models.Model):
	shortcut=models.CharField(max_length=200)
	full_form=models.CharField(max_length=200)
	
	class Meta:
		managed=False
		db_table='agro_chemical_abbreviations'

class agro_chemical_formulation(models.Model):
	shortcut=models.CharField(max_length=200)
	full_form=models.CharField(max_length=200)
	
	class Meta:
		managed=False
		db_table='agro_chemical_formulation'


class agro_chemical_products(models.Model):
	sno=models.IntegerField()
	technical=models.CharField(max_length=200)
	brand_name=models.CharField(max_length=200)
	application=models.CharField(max_length=200)
	dose_or_acre=models.CharField(max_length=200)
	mode_of_action=models.CharField(max_length=200)
	category=models.CharField(max_length=200)
	mixture=models.CharField(max_length=200)

	class Meta:
		managed=False
		db_table='agro_chemical_products'

