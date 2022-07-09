#version 330
uniform mat4 transform_matrix;
in vec3 in_position;
in vec3 in_normal;
out vec3 normal;
out vec3 vec_pos;

void main() {
    // passing norml vector of vertex to fragment shader
    normal = in_normal;
    // setting transformation to vertex
    gl_Position = transform_matrix * vec4(in_position, 1.0);
    // passing vertex position to fragment shader
    vec_pos = in_position;
}