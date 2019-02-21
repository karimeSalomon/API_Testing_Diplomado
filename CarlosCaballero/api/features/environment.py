import yaml

config = yaml.load(open('config/config.yml'))

def before_all(context):
    context.host = config['host']
    context.method = config['method']
    context.code = config['code']

