import moderngl
from pyrr import Matrix44

from base_window import BaseWindowConfig


class PhongWindow(BaseWindowConfig):

    def __init__(self, **kwargs):
        super(PhongWindow, self).__init__(**kwargs)

    def init_shaders_variables(self):
        # transformation matrix for objects
        self.transform_matrix = self.program['transform_matrix']
        # colors of objects
        self.color_input = self.program['color_input']
        # eye position
        self.eye_position = self.program['eye_position']

    def model_load(self):
        # loading sphere and cube as objects
        self.cube_obj = self.load_scene('cube.obj')
        self.sphere_obj = self.load_scene('sphere.obj')
        # creating every part of robot as object from cube and sphere
        self.head = self.sphere_obj.root_nodes[0].mesh.vao.instance(self.program)
        self.body = self.cube_obj.root_nodes[0].mesh.vao.instance(self.program)
        self.right_hand = self.cube_obj.root_nodes[0].mesh.vao.instance(self.program)
        self.left_hand = self.cube_obj.root_nodes[0].mesh.vao.instance(self.program)
        self.right_leg = self.cube_obj.root_nodes[0].mesh.vao.instance(self.program)
        self.left_leg = self.cube_obj.root_nodes[0].mesh.vao.instance(self.program)
        

    def render(self, time: float, frame_time: float):
        # black background
        self.ctx.clear(0.0, 0.0, 0.0, 1.0)
        # white background
        # self.ctx.clear(1.0, 1.0, 1.0, 1.0)
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        lookat = Matrix44.look_at(
            (-20.0, -15.0, 5.0),
            (0.0, 0.0, 1.0),
            (0.0, 0.0, 1.0),
        )
        # assuming that eye position is first vertex from look_at matrix
        self.eye_position.value = (-20.0, -15.0, 5.0)

        # creating transformation matrices - every transformation matrix must be multiplied by projection and look_at matricies (to look at objects from other point and display correct)
        # for head only translation
        mat_tr_head = projection * lookat * Matrix44.from_translation((0, 0, 5))
        # for body translation and scale
        mat_tr_body = projection * lookat * Matrix44.from_translation((0, 0, 2)) * Matrix44.from_scale((1, 1, 2))
        # for left hand translation, rotation by x_axis by RADIANS (!) and scale
        mat_tr_left_hand = projection * lookat * Matrix44.from_translation((0, 3, 3)) * Matrix44.from_x_rotation(-0.78) * Matrix44.from_scale((0.5, 0.5, 1.25))
        # for right hand same operations like for left but with different angle (in RADIANS) and translation vector
        mat_tr_right_hand = projection * lookat * Matrix44.from_translation((0, -3, 3)) * Matrix44.from_x_rotation(0.78) * Matrix44.from_scale((0.5, 0.5, 1.25))
        # same for left leg but with other translation, rotation and scale vectors
        mat_tr_left_leg = projection * lookat * Matrix44.from_translation((0, -2, -1.5)) * Matrix44.from_x_rotation(0.52) * Matrix44.from_scale((0.5, 0.5, 1.75))
        # same for right leg but with other translation, rotation and scale vectors
        mat_tr_right_leg = projection * lookat * Matrix44.from_translation((0, 2, -1.5)) * Matrix44.from_x_rotation(-0.52) * Matrix44.from_scale((0.5, 0.5, 1.75))
        
        # rendering head
        # applying color to head
        self.color_input.value = (0.565, 0.933, 0.565)
        self.transform_matrix.write((mat_tr_head).astype('f4'))
        self.head.render()

        # rendering body
        # applying color to body
        self.color_input.value = (0.69, 0.61, 0.85)
        self.transform_matrix.write((mat_tr_body).astype('f4'))
        self.body.render()

        # rendering left hand
        # applying color to left_hand
        self.color_input.value = (0.45, 0.20, 0.76)
        self.transform_matrix.write((mat_tr_left_hand).astype('f4'))
        self.left_hand.render()

        # rendering right hand
        # applying color to right_hand
        self.color_input.value = (0.59, 0.0, 0.45)
        self.transform_matrix.write((mat_tr_right_hand).astype('f4'))
        self.right_hand.render()

        # rendering left leg
        # applying color to left_leg
        self.color_input.value = (209/255, 196/255, 102/255)
        self.transform_matrix.write((mat_tr_left_leg).astype('f4'))
        self.left_leg.render()

        # rendering right leg
        # applying color to right_leg
        self.color_input.value = (158/255, 106/255, 108/255)
        self.transform_matrix.write((mat_tr_right_leg).astype('f4'))
        self.right_leg.render()
