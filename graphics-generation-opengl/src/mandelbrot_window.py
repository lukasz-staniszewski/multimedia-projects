import moderngl

from base_window import BaseWindowConfig


class MandelbrotWindowConfig(BaseWindowConfig):
    def __init__(self, **kwargs):
        super(MandelbrotWindowConfig, self).__init__(**kwargs)

    def init_shaders_variables(self):
        self.n_of_iterations = self.program['n_of_iterations']
        self.center_fract = self.program['center_fract']
        self.asp_ratio = self.program['asp_ratio']
        self.scale = self.program['scale']

    def render(self, time: float, frame_time: float):
        self.ctx.clear(1.0, 1.0, 1.0, 0.0)
        # setting number of iterations
        self.n_of_iterations.value = 100
        # setting center point
        self.center_fract.value = (-0.5, 0.0)
        # aspect ratio setting
        self.asp_ratio.value = self.aspect_ratio
        # setting value of scale
        self.scale.value = 1.2;
        self.vao.render(moderngl.TRIANGLE_STRIP)
