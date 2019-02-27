import yaml

global info_dict
generic_data = yaml.load(open('config/config.yml'))

def before_all(context):
    context.host = generic_data['host']
    context.method = generic_data['method']
    context.code = generic_data['code']
