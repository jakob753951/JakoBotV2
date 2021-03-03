import unittest
import random
import string
import utils

def get_rand_string(length: int):
	return ''.join(random.choices(string.ascii_letters, k=length))

class ConfigTests(unittest.TestCase):
	def test_json_load(self):
		test_string = get_rand_string(8)
		test_json = f"""\
{{
	"a": "{test_string}"
}}"""
		with open('ConfigTest.json', 'w') as cfg_file:
			cfg_file.write(test_json)

		cfg = utils.load_config('ConfigTest.json')
		self.assertEqual(cfg.a, test_string)


	def test_nested_properties_write_read(self):
		test_string = get_rand_string(8)
		test_json = f"""\
{{
	"a":
	{{
		"b": "{test_string}"
	}}
}}"""

		with open('ConfigTest.json', 'w') as cfg_file:
			cfg_file.write(test_json)

		cfg = utils.load_config('ConfigTest.json')
		self.assertEqual(cfg.a.b, test_string)

if __name__ == '__main__':
	unittest.main()