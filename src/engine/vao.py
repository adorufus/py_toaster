from .vbo import VBO
from .shader import Shader

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = Shader(ctx)
        self.vaos = {}

        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cube']
        )

        self.vaos['jokowi'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['jokowi']
        )

        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox']
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(
            program,
            [(vbo.vbo, vbo.format, *vbo.attrib)])
        return vao
    
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()