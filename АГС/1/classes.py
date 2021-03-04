from OpenGL.GL import *
from OpenGL.GLUT import *


class Shader:
    # Процедура подготовки шейдера (тип шейдера, текст шейдера)
    def create_shader(shader_type, source):
        # Создаем пустой объект шейдера
        shader = glCreateShader(shader_type)
        # Привязываем текст шейдера к пустому объекту шейдера
        glShaderSource(shader, source)
        # Компилируем шейдер
        glCompileShader(shader)
        # Возвращаем созданный шейдер
        return shader

    def pars_file(filename):
        with open(filename) as f:
            lst = f.readlines()
        s = ""
        for i in lst:
            s = s+i
        return s

