import yaml

global generic_data
generic_data = yaml.load(open('config/config.yml'))


def before_all(context):
    context.host = generic_data['app']['host']
    context.root_path = generic_data['app']['rootPath']
    context.code = generic_data['app']['code']
    context.method = generic_data['app']['method']

