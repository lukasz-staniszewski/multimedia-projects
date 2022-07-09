import moderngl_window

from base_window import BaseWindowConfig
from mandelbrot_window import MandelbrotWindowConfig
from robot_window import RobotWindow
from phong_window import PhongWindow

# python src/main.py --shader_path=./resources/shaders/mandelbrot --shader_name=mandelbrot --model_name=cube.obj
# python src/main.py --shader_path=./resources/shaders/robot --shader_name=robot
# python src/main.py --shader_path=./resources/shaders/phong --shader_name=phong

if __name__ == '__main__':
    moderngl_window.run_window_config(PhongWindow)
