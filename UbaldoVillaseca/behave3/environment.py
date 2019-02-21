import yaml

global info_dict
g = yaml.load(open('config\config.yml'))

def before_all(context):
    context.host = g['host']
    context.method = g['method']
    context.code = g['code']