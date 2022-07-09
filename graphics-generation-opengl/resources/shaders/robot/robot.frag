#version 330

uniform vec3 color_input;
out vec4 f_color;

void main()
{
    // applying color  
    f_color = vec4(color_input, 1.0);
}
