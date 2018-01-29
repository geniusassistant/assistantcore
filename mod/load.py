import importlib

# TODO: add more API features and support

# TODO: move this array into a config file
with open('config.txt') as f:
    enabledmods = f.readlines()
#enabledmods = ['examplemod', 'base']
print('init mods')

def outsourcer(text):
    for module in enabledmods:
        module = importlib.import_module(module, package=None)
        ret = module.outsource(text)
        if ret != None:
            return ret