# import sdl2.ext

# class SpriteRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
#     def __init__(self, window):
#         super(SpriteRenderer, self).__init__(window)
#         print("initializing renderer")

#     def render(self, components):
#         sdl2.ext.fill(self.surface, sdl2.ext.Color(1, 1, 1, 1))
#         super(SpriteRenderer, self).render(components)