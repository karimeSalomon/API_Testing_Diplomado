import yaml

global info_dict
generic_data = yaml.load(open('Config/config.yml'))


def before_all(context):
    context.host = generic_data['app']['host']
    context.method = generic_data['app']['method']
    context.code = generic_data['app']['code']


