import json
from attrdict import AttrDict
import os

def load_config(file_path = 'Config.json'):
	with open(file_path, encoding='utf8') as config_file:
		cfg = json.load(config_file, object_hook=AttrDict)
	return cfg

def get_cog_names(cogs_dir):
	return [f'{cogs_dir}.{remove_file_extension(file_name)}' for file_name in os.listdir(cogs_dir)]

def remove_file_extension(file_name):
	return '.'.join(file_name.split('.')[:-1])
