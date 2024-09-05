import pygame as pg
import moderngl as mgl
from moderngl import Context

class Texture:
    def __init__(self, ctx):
        self.ctx: Context = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='assets/textures/img.png')
        self.textures[1] = self.get_texture(path='assets/textures/img.png')
        self.textures[2] = self.get_texture(path='assets/textures/pala.jpeg')

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()

        #anisbaswedan
        texture.anisotropy = 32.0
        
        return texture
    
    def destroy(self):
        [tex.release() for tex in self.textures.values()]