import os
import json

variables = {}

class Variable:
	def __init__(self, name, value):
		self.value = value
		self.name = name
	def hold(self):
		global variables
		variables[self.name] = self.value

def get(variable):
	return variables[variable]

def call_py(script_id, func_name, args = ''):
	with open(f'./running/call.py', 'w') as f:
		f.write(f'from running{script_id} import *\n')
		f.write(f'{func_name}({args})')
	os.system('python ./running/call.py')

def call_node(script_id, func_name, args = ''):
	with open(f'./running/call.js', 'w') as f:
		f.write(f'let sgms = require("./running{script_id}.js");\n')
		f.write(f'sgms.{func_name}({args});')
	os.system('node ./running/call.js')

def load():
	global variables
	with open('./running/variables.json', 'r', encoding='utf-8') as f:
		variables = json.load(f)

def save():
	with open('./running/variables.json', 'w', encoding='utf-8') as f:
		json.dump(variables, f, ensure_ascii=False, indent=4)