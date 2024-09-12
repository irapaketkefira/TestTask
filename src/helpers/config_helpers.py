
import os


def get_base_url():

    env = os.environ.get('ENV','test')

    if env.lower() == 'test':
        return 'https://useinsider.com'
    elif env.lower() ==  'prod':
        return 'https://prod.useinsider.com'
    else:
        raise Exception(f"Unknown environment: {env}")
