from json import load
from pygame import font

class Configuration(object):
    def __init__(self):
        with open('gui_conf.json') as config_file:
            config_dict = load(config_file)
        self.font = self.get_font(config_dict)
        self.types_border = self.get_types_border(config_dict)
        self.windowed_resolution = self.get_windowed_resolution(config_dict)

    def get_font(self, config_dict):
        return config_dict['pygame']['font']

    def get_types_border(self, config_dict):
        types_border = {}
        for type, color in config_dict['graphic_components']['cell'].items():
            types_border[type] = (color[0], color[1], color[2])
        return types_border

    def get_windowed_resolution(self, config_dict):
        return (config_dict['pygame']['screen']['width'], config_dict['pygame']['screen']['height'])

config = Configuration()
