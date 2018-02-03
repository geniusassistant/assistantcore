import importlib
import json
import os
import sys

# TODO: add more API features and support

enabledmods = json.load(open('config.json'))["enabledmods"]

for folder in os.listdir('mod'):
    if '.' not in folder:
        if folder in json.load(open('config.json'))["enabledpacks"]:
            sys.path.insert(0, 'mod/' + folder)
            for mod in os.listdir('mod/' +  folder):
                enabledmods.append(mod.replace('.py', ''))


print('Loaded mods:')
for i in enabledmods:
    print('    -' + i)

print('-------------------')

os.system('pause')

def outsourcer(text):
    for module in enabledmods:
        module = importlib.import_module(module, package=None)
        ret = module.outsource(text)
        if ret != None:
            return ret