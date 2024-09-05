import pygame as pg
import moderngl as mgl
import sys
from src.engine import Cube, Camera, Light, Mesh, Texture, Scene
from src.engine.model import Jokowi

class ToasterEngine:
    def __init__(self, win_size=(1920, 1080)):
        pg.init()
        self.WIN_SIZE = win_size

        #set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        #create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE | pg.FULLSCREEN)
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        pg.display.set_caption("Toaster")

        #use existing opengl context
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

        #time tracker object
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        self.light = Light()
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)

        self.scene.load(Jokowi(self, pos=(0, -15, 0),  scale=(10, 10, 10)))

        n, s = 80, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                self.scene.load(Cube(self, pos=(x, -s, z))) 

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))

        self.scene.render()

        #swap buffer
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

# RESOURCES = sdl2.ext.Resources(__file__, "assets")


# def run():
#     engine = Engine(title="Toaster", size=(640, 480))

#     engine.init()

#     running = True

#     while running:
#         events = sdl2.ext.get_events()
#         for event in events:
#             if event.type == sdl2.SDL_QUIT:
#                 running = False
#                 break
        
#         engine.render()
#         engine.loop()

#     engine.destroy()

#     return 0


if __name__ == "__main__":
    app = ToasterEngine()
    app.run()
