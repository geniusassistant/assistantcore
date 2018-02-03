import importlib
import json
import os
import sys

# TODO: add more API features and support

enabledmods = json.load(open('config.json'))["enabledmods"]

print('loaded tree:')
for folder in os.listdir('mod'):
    if folder == '__pycache__':
        break
    if '.' not in folder:
        if folder in json.load(open('config.json'))["enabledpacks"]:
            sys.path.insert(0, 'mod/' + folder)
            print('    -' + folder)
            for mod in os.listdir('mod/' +  folder):
                if mod == '__pycache__':
                    break
                print('        -' + mod)
                enabledmods.append(mod.replace('.py', ''))
    else:
        if folder != 'load.py':
            print('    -' + folder)



print('-------------------')

def outsourcer(text):
    for module in enabledmods:
        module = importlib.import_module(module, package=None)
        ret = module.outsource(text)
        if ret != None:
            return ret