import importlib
import json

# TODO: add more API features and support

enabledmods = json.load(open('config.json'))["enabledmods"]

print('Loaded mods:')
for i in enabledmods:
    print('    -' + i)
print('-------------------')

#enabledmods = ['examplemod', 'base']

def outsourcer(text):
    for module in enabledmods:
        module = importlib.import_module(module, package=None)
        ret = module.outsource(text)
        if ret != None:
            return ret