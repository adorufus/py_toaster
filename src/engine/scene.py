from .model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self, object):
        add = self.add_object

        add(object)

    def render(self):
        for obj in self.objects:
            obj.render()