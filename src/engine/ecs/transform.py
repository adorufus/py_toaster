import glm


class Transform:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
