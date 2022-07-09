#version 330

uniform vec3 color_input;
out vec4 f_color;
in vec3 normal;
in vec3 vec_pos;
uniform vec3 eye_position;

// light variables
const vec3 light_pos = vec3(-20.0f, 10.0f, 10.0f);
const vec3 light_ambient = vec3(0.3f, 0.3f, 0.3f);
const vec3 light_diffuse = vec3(0.5f, 0.5f, 0.5f);
const vec3 light_specular = vec3(4.0f, 4.0f, 4.0f);

// object variables
const vec3 object_diffuse = vec3(1.0f, 1.0f, 1.0f);
const vec3 object_specular = vec3(2.0f, 2.0f, 2.0f);
const float object_shininess = 52.0f;

void main()
{
    // implementation of phong shading algorithm
    // vector N - vertex's normal vector (another normalizing to be sure)
    vec3 norm_vector = normalize(normal);
    // vector L - from vertex's position towards light source
    vec3 light_vector = normalize(light_pos - vec_pos);
    // vector V - from vertex's position towards observer
    vec3 eye_vector = normalize(eye_position-vec_pos);
    // vector R - reflected ray (between light vector and normal vector)
    // IMPORTANT: glsl.reflect function wants light vector to point from the light source towards object, thats why there is '-'
    vec3 reflect_vector = normalize(reflect(-light_vector, norm_vector));
    
    // counting full ambient, I assume that object_ambient equals 1.0
    vec3 ambient = light_ambient;
    // counting full diffuse
    vec3 diffuse = object_diffuse * dot(light_vector, norm_vector) * light_diffuse;
    // counting full specular - there is need to ensure that dot product of vector V and vector R is a value belonging to <0, 1>
    vec3 specular = object_specular * pow(clamp(dot(eye_vector, reflect_vector),0.0f, 1.0f), object_shininess) * light_specular;
    // setting color of fragment as color*(counted ambient + counted diffuse + counted specular)
    f_color = vec4(vec3(color_input*(ambient+diffuse+specular)), 1.0f);
}
