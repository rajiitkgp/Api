from django.shortcuts import render
from django.core import serializers

from django.http import HttpResponse
from django.http import JsonResponse
from .models import Combine, area_under_crop, crop_irrigated,source_irrigated
from .models import soil_health_card

def index(request):
    return HttpResponse("Hello, world")



def area_prod(request):
	if request.method=='GET':
		comb=Combine.objects.all()
		state=request.GET.get('state')
		if(state is not None):
			comb=comb.filter(state=state)
		year=request.GET.get('year')
		if(year is not None):
			comb=comb.filter(year=year)

		season=request.GET.get('season')
		if(season is not None):
			comb=comb.filter(season=season)



		response=[]
		for i in comb:
			xv  = {
		    'state': i.state,
		    'district': i.district,
		    'crop' : i.crop,
		    'year' : i.year,
		    'season' : i.season,
		    'area' : i.area,
		    'production' : i.production,
		    'yields' : i.yields,
		    'yield_units' : i.yield_units
		    }

			response.append(xv)

	    
	return JsonResponse(response,safe=False) 

def soil_health(request):
	if request.method=='GET':
		users = soil_health_card.objects.all().values()  # or simply .values() to get all fields
		users_list = list(users)  # important: convert the QuerySet to a list object
		return JsonResponse(users_list, safe=False)




def area_under_crops(request):
	if request.method=='GET':
		area=area_under_crop.objects.all()

		response=[]
		for i in area:
			xv  = {
			'district' : i.district,
			'rice_autumn' : i.rice_autumn,
			'rice_winter' : i.rice_winter,
			'rice_summer' : i.rice_summer,
			'rice_total_1' : i.rice_total_1,
			'jowar_kharif' : i.jowar_kharif,
			'jowar_rabi' : i.jowar_rabi,
			'jowar_total_2' : i.jowar_total_2,
			'bajra_3' : i.bajra_3,
			'maize_4' : i.maize_4,
			'ragi_5' : i.ragi_5,			
			'wheat_6' : i.wheat_6,
			'barley_7' : i.barley_7,
			'other_cereals_and_millets_kharif' : i.other_cereals_and_millets_kharif,
			'other_cereals_and_millets_rabi' : i.other_cereals_and_millets_rabi,
			'other_cereals_and_millets_total_8' : i.other_cereals_and_millets_total_8,
			'total_cereals_and_millets_plus_1_to_8' : i.total_cereals_and_millets_plus_1_to_8,
			'gram_9' : i.gram_9,
			'arhar_aka_tur_10' : i.arhar_aka_tur_10,
			'other_pulses_kharif' : i.other_pulses_kharif,
			'other_pulses_rabi' : i.other_pulses_rabi,
			'other_pulses_misc' : i.other_pulses_misc,
			'other_pulses_total_11' : i.other_pulses_total_11,
			'total_pulses_plus_9_to_11' : i.total_pulses_plus_9_to_11,
			'total_food_grain' : i.total_food_grain,
			'sugarcane_12' : i.sugarcane_12,
			'other_sugar_13' : i.other_sugar_13,
			'total_sugar_plus_13_to_14' : i.total_sugar_plus_13_to_14,
			'black_pepper_14' : i.black_pepper_14,
			'chillies_15' : i.chillies_15,
			'ginger_16' : i.ginger_16,
			'turmeric_17' : i.turmeric_17,
			'cardamom_19' : i.cardamom_19,
			'betulnet_20' : i.betulnet_20,
			'garlic_21' : i.garlic_21,
			'coriander_22' : i.coriander_22,
			'other_condiments_and_spices_23' : i.other_condiments_and_spices_23,
			'total_condiments_and_spices_plus_14_to_23' : i.total_condiments_and_spices_plus_14_to_23,
			'banana_24' : i.banana_24,
			'mango_25' : i.mango_25,
			'citrus_fruits_26' : i.citrus_fruits_26,
			'grapes_27' : i.grapes_27,
			'pome_fruits_28' : i.pome_fruits_28,
			'papaya_29' : i.papaya_29,
			'apple_30' : i.apple_30,
			'other_fruits_31' : i.other_fruits_31,
			'total_fruits_plus_24_to_31' : i.total_fruits_plus_24_to_31,
			'cashewnut_32' : i.cashewnut_32,
			'other_dry_fruits_33' : i.other_dry_fruits_33,
			'total_dry_fruits_plus_32_to_33' : i.total_dry_fruits_plus_32_to_33,
			'total_fruits_drydruits_plus_24_to_33' : i.total_fruits_drydruits_plus_24_to_33,
			'potato_34' : i.potato_34,
			'tapioca_35' : i.tapioca_35,
			'sweet_potato' : i.sweet_potato,
			'onion' : i.onion,
			'other_vegetables_kharif' : i.other_vegetables_kharif,
			'other_vegetables_rabi' : i.other_vegetables_rabi,
			'other_vegetables_misc' : i.other_vegetables_misc,
			'other_vegetables_total' : i.other_vegetables_total,
			'total_vegetables' : i.total_vegetables,
			'total_fruits_and_vegetable' : i.total_fruits_and_vegetable,
			'other_food_crops' : i.other_food_crops,
			'total_food_crop' : i.total_food_crop,
			'groundnut' : i.groundnut,
			'castor_seed' : i.castor_seed,
			'sesamum' : i.sesamum,
			'rapeseed_and_mustard' : i.rapeseed_and_mustard,
			'linseed' : i.linseed,
			'soyabean' : i.soyabean,
			'coconut' : i.coconut,
			'niger_seed' : i.niger_seed,
			'sunflower' : i.sunflower,
			'safflower' : i.safflower,
			'other_oilseeds' : i.other_oilseeds,
			'total_oilseeds' : i.total_oilseeds,
			'cotton' : i.cotton,
			'jute' : i.jute,
			'mesta' : i.mesta,
			'sanhemp' : i.sanhemp,
			'other_fibres' : i.other_fibres,
			'total_fibres' : i.total_fibres,
			'indigo' : i.indigo,
			'other_dyes_and_tanning_materials' : i.other_dyes_and_tanning_materials,
			'total_dyes_and_tanning_materials' : i.total_dyes_and_tanning_materials,
			'opium' : i.opium,
			'tobacco' : i.tobacco,
			'chinchona' : i.chinchona,
			'indian_hemp' : i.indian_hemp,
			'tea' : i.tea,
			'coffee' : i.coffee,
			'rubber' : i.rubber,
			'other_plantation_crops' : i.other_plantation_crops,
			'total_drugs_narcotics_and_plantation_crops' : i.total_drugs_narcotics_and_plantation_crops,
			'guar_seed' : i.guar_seed,
			'oats' : i.oats,
			'fodder_crops' : i.fodder_crops,
			'green_manure' : i.green_manure,
			'other_non_food_crops' : i.other_non_food_crops,
			'total_non_food_crop' : i.total_non_food_crop,
			'total_cropped_area' : i.total_cropped_area,
			'area_sown_more_than_once' : i.area_sown_more_than_once,
			'net_area_sown' : i.net_area_sown,
			'state' : i.state,
			'year' : i.year,
			'unit' : i.unit


			}

			response.append(xv)

	return JsonResponse(response,safe=False)


def crop_irrigated_csv(request):
	if request.method=='GET':
		area=crop_irrigated.objects.all()

		response=[]
		for i in area:
			xv  = {
			# 'ids': i.id,
			'district' : i.district,
			'rice_autumn' : i.rice_autumn,
			'rice_kharif' : i.rice_kharif,
			'rice_winter' : i.rice_winter,
			'rice_summer' : i.rice_summer,
			'rice_total_1' : i.rice_total_1,
			'jowar_kharif' : i.jowar_kharif,
			'jowar_rabi' : i.jowar_rabi,
			'jowar_total_2' : i.jowar_total_2,
			'bajra_3' : i.bajra_3,
			'maize_4' : i.maize_4,
			'ragi_5' : i.ragi_5,			
			'wheat_6' : i.wheat_6,
			'barley_7' : i.barley_7,
			'other_cereals_and_millets_kharif' : i.other_cereals_and_millets_kharif,
			'other_cereals_and_millets_misc' : i.other_cereals_and_millets_misc,			
			'other_cereals_and_millets_rabi' : i.other_cereals_and_millets_rabi,
			'other_cereals_and_millets_total_8' : i.other_cereals_and_millets_total_8,
			'total_cereals_and_millets_plus_1_to_8' : i.total_cereals_and_millets_plus_1_to_8,
			'gram_9' : i.gram_9,
			'arhar_aka_tur_10' : i.arhar_aka_tur_10,
			'other_pulses_kharif' : i.other_pulses_kharif,
			'other_pulses_misc' : i.other_pulses_misc,
			'other_pulses_rabi' : i.other_pulses_rabi,			
			'other_pulses_total_11' : i.other_pulses_total_11,
			'total_pulses_plus_9_to_11' : i.total_pulses_plus_9_to_11,
			'total_food_grain' : i.total_food_grain,
			'sugarcane_12' : i.sugarcane_12,
			'condiments_and_spices_total_13' : i.condiments_and_spices_total_13,
			'fruits_and_vegetables_total_14' : i.fruits_and_vegetables_total_14,
			'other_food_crops_15' : i.other_food_crops_15,
			'food_crop_total_plus_1_to_15' : i.food_crop_total_plus_1_to_15,
			'groundnut_16' : i.groundnut_16,
			'sesamum_17' : i.sesamum_17,
			'rapeseed_and_mustard_18' : i.rapeseed_and_mustard_18,
			'linseed_19' : i.linseed_19,
			'soyabean_20' : i.soyabean_20,
			'sunflower_21' : i.sunflower_21,
			'other_oilseeds_22' : i.other_oilseeds_22,
			'total_oilseeds_plus_16_to_22' : i.total_oilseeds_plus_16_to_22,
			'cotton_23' : i.cotton_23,
			'tobacco_24' : i.tobacco_24,
			'fodder_crops_25' : i.fodder_crops_25,
			'other_non_food_crops_26' : i.other_non_food_crops_26,
			'non_food_crop_total_plus_16_to_26' : i.non_food_crop_total_plus_16_to_26,
			'total_irrigated_area_plus_1_to_26' : i.total_irrigated_area_plus_1_to_26,
			'state' : i.state,
			'year' : i.year,
			'unit' : i.unit

			}
			response.append(xv)

	return JsonResponse(response,safe=False)


# def crop(request):
# 	if request.method=='GET':
# 		area=crop_irrigated.objects.all()

# 		response=[]
# 		for i in area:




def source_irrigated_csv(request):
    users = source_irrigated.objects.all().values()  # or simply .values() to get all fields
    users_list = list(users)  # important: convert the QuerySet to a list object
    return JsonResponse(users_list, safe=False)