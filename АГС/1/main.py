# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLUT import *

from classes import Shader


def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Очищаем экран и заливаем серым цветом
    glEnableClientState(GL_VERTEX_ARRAY)  # Включаем использование массива вершин
    glEnableClientState(GL_COLOR_ARRAY)  # Включаем использование массива цветов
    # Указываем, где взять массив верши:
    # Первый параметр - сколько используется координат на одну вершину
    # Второй параметр - определяем тип данных для каждой координаты вершины
    # Третий парметр - определяет смещение между вершинами в массиве
    # Если вершины идут одна за другой, то смещение 0
    # Четвертый параметр - указатель на первую координату первой вершины в массиве
    glVertexPointer(3, GL_FLOAT, 0, pointdata)
    # Указываем, где взять массив цветов:
    # Параметры аналогичны, но указывается массив цветов
    # glColorPointer(3, GL_FLOAT, 0, pointcolor)
    # Рисуем данные массивов за один проход:
    # Первый параметр - какой тип примитивов использовать (треугольники, точки, линии и др.)
    # Второй параметр - начальный индекс в указанных массивах
    # Третий параметр - количество рисуемых объектов (в нашем случае это 3 вершины - 9 координат)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glVertexPointer(3, GL_FLOAT, 0, pointdata2)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glDisableClientState(GL_VERTEX_ARRAY)  # Отключаем использование массива вершин
    glDisableClientState(GL_COLOR_ARRAY)  # Отключаем использование массива цветов
    glutSwapBuffers()  # Выводим все нарисованное в памяти на экран


# Здесь начинется выполнение программы
# Использовать двойную буферезацию и цвета в формате RGB (Красный Синий Зеленый)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
# Указываем начальный размер окна (ширина, высота)
glutInitWindowSize(300, 300)
# Указываем начальное
# положение окна относительно левого верхнего угла экрана
glutInitWindowPosition(50, 50)
# Инициализация OpenGl
glutInit(sys.argv)
# Создаем окно с заголовком "Shaders!"
glutCreateWindow(b"Shaders!")
# Определяем процедуру, отвечающую за перерисовку
glutDisplayFunc(draw)
# Определяем процедуру, выполняющуюся при "простое" программы
glutIdleFunc(draw)
# Задаем серый цвет для очистки экрана
glClearColor(0.2, 0.2, 0.2, 1)

# объект класса Shader
shader = Shader
s_vertex = shader.pars_file("SHADER\Example.vsh")
s_fragment = shader.pars_file("SHADER\Example.fsh")

# Создаем вершинный шейдер:
# Положение вершин не меняется
# Цвет вершины - такой же как и в массиве цветов
vertex = shader.create_shader(GL_VERTEX_SHADER, s_vertex)
# Создаем фрагментный шейдер:
# Определяет цвет каждого фрагмента как "смешанный" цвет его вершин
fragment = shader.create_shader(GL_FRAGMENT_SHADER, s_fragment)
# Создаем пустой объект шейдерной программы
program = glCreateProgram()
# Приcоединяем вершинный шейдер к программе
glAttachShader(program, vertex)
# Присоединяем фрагментный шейдер к программе
glAttachShader(program, fragment)
# "Собираем" шейдерную программу
glLinkProgram(program)
# Сообщаем OpenGL о необходимости использовать данную шейдерну программу при отрисовке объектов
glUseProgram(program)
# Определяем массив вершин (три вершины по три координаты)
pointdata = [
    [-0.5, 0.5, 0],
    [-0.5, -0.5, 0],
    [0.5, 0.5, 0],
]
pointdata2 = [
    [0.5, -0.5, 0],
    [-0.5, -0.5, 0],
    [0.5, 0.5, 0],
]
glutMainLoop()
