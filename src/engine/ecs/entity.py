from .transform import Transform

class Entity:
    def __init__(self, entity_id, name, transform: Transform):
        self.id = entity_id
        self.components = {}
        self.transform = transform
        self.name = name

    def add_component(self, component_type, component):
        self.components[component_type] = component

    def get_component(self, component_type):
        return self.components.get(component_type, None)

    def remove_component(self, component_type):
        if component_type in self.components:
            del self.components[component_type]

    def update(self, delta_time): ...

    def start(self): ...
