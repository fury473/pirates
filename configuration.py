from json import load
from pygame import font

class Configuration(object):
    def __init__(self, file_path):
        with open(file_path) as config_file:
            config = load(config_file)
        self.font = font.Font(None, 14)
        self.types_border = self.get_types_border(config)
        self.windowed_resolution = self.get_windowed_resolution(config)

    def get_types_border(self, config):
        types_border = {}
        for type, color in config['skin']['cell'].items():
            types_border[type] = (color[0], color[1], color[2])
        return types_border

    def get_windowed_resolution(self, config):
        return (config['screen']['width'], config['screen']['height'])
