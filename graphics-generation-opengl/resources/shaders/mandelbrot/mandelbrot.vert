#version 330

in vec2 in_position;
out vec2 vert_pos;

void main() {
    gl_Position = vec4(in_position, 0.0, 1.0);
    vert_pos = in_position;
}