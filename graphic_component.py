class GraphicComponentMixin(object):
    def __init__(self):
        self.graphic_component = None


    def set_graphic_component(self, graphic_component):
        self.graphic_component = graphic_component

class GraphicComponent(object):
    def __init__(self, model):
        model.set_graphic_component(self)
        self.model = model

    def draw(self, surface):
        pass

