import json
from attrdict import AttrDict

def load_config(file_path):
	with open(file_path) as config_file:
		cfg = json.load(config_file, object_hook=AttrDict)
	return cfg