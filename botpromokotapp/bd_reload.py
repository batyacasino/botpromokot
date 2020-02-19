from admitad import api, items
import json

from .models import *

def scope(scops):
	client_id = os.environ['client_id']
	client_secret = os.environ['client_secret']
	scope = ''.join(set([scops]))
	return api.get_oauth_client_client(client_id,client_secret,scope)

def json_dump(file_name, dict_name):
	with open(f'adm_json/{file_name}.json', 'w', encoding='UTF-8') as jfile:
		json.dump(dict_name, jfile, indent=2, ensure_ascii=False)

def get_cupons():
	client = scope('coupons_for_website')
	meta = client.CouponsForWebsite.get(1155537)['_meta']
	offset = 0
	data_cupons = []
	while True:        
		result = client.CouponsForWebsite.get(1155537, offset=offset, limit=500, order_by='-rating', region=1)['results']
		data_cupons.extend(result)
		offset += 500
		if offset > meta['count']:
			break
	json_dump('get_cupons', data_cupons)

def json_load(file_name):
	return json.load(open(f'adm_json/{file_name}.json', 'r', encoding='UTF-8'))

def del_db():
	results = json_load('get_cupons')
	for result in results:
		camp, created = Campaigns.objects.get_or_create(
															id=result["campaign"]["id"],
															name=result["campaign"]["name"]
															)

		categor, created = Categories.objects.get_or_create(
															id=result["categories"][0]["id"],
															name=result["categories"][0]["name"] 
															)

		typ, created = Types.objects.get_or_create(
															id=result["types"][0]["id"],
															name=result["types"][0]["name"] 
															)

		obj, created = Cupons.objects.get_or_create(
															id=result["id"],
															rating=result["rating"], 
															campaigns=Campaigns.objects.get(id=result["campaign"]["id"]), 
															goto_link=result["goto_link"],
															short_name=result["short_name"],
															discount=result["discount"],
															image=result["image"],
															promocode=result["promocode"],
															description=result["description"],
															categories=Categories.objects.get(id=result["categories"][0]["id"]),
															types=Types.objects.get(id=result["types"][0]["id"]),
															)