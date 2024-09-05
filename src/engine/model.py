from moderngl import Context
import numpy as np
import glm
import pygame as pg

class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.shader_program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        m_model = glm.translate(m_model, self.pos)
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.scale(m_model, self.scale)
        return m_model
    
    def render(self):
        self.update()
        self.vao.render()




class Cube(BaseModel):

    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.shader_program['m_model'].write(self.m_model)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['camPos'].write(self.camera.position)

    def on_init(self):
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()

        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)
        
        self.shader_program["light.position"].write(self.app.light.position)
        self.shader_program["light.Ia"].write(self.app.light.ambient_intensity)
        self.shader_program["light.Id"].write(self.app.light.diffuse_intensity)
        self.shader_program["light.Is"].write(
            self.app.light.specular_intensity)


class Jokowi(BaseModel):

    def __init__(self, app, vao_name='jokowi', tex_id=2, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.shader_program['m_model'].write(self.m_model)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['camPos'].write(self.camera.position)

    def on_init(self):
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()

        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)
        
        self.shader_program["light.position"].write(self.app.light.position)
        self.shader_program["light.Ia"].write(self.app.light.ambient_intensity)
        self.shader_program["light.Id"].write(self.app.light.diffuse_intensity)
        self.shader_program["light.Is"].write(
            self.app.light.specular_intensity)