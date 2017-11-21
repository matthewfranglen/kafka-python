import configparser
from os.path import dirname, join

SETTINGS_FILE = join(dirname(__file__), '..', 'config.ini')

def read_settings():
    config = configparser.ConfigParser()
    config.read(SETTINGS_FILE)
    return config
