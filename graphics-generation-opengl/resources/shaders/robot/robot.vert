#version 330
uniform mat4 transform_matrix;
in vec3 in_position;
void main() {
    // applying transformation matrix to position by multiplying
    gl_Position = transform_matrix * vec4(in_position, 1.0);
}