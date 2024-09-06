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
        self.textures['skybox'] = self.get_texture_cube(path='assets/textures/skybox/', ext='png')

    def get_texture_cube(self, path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        # textures = [pg.image.load(path + f'{face}.{ext}').convert() for face in faces]

        textures = []
        for face in faces:
            texture = pg.image.load(path + f'{face}.{ext}').convert()

            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)

            textures.append(texture)


        size = textures[0].get_size()

        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        print(size)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

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