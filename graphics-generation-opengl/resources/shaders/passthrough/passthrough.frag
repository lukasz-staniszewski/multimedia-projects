#version 330

out vec4 f_color;
in vec2 pos;
void main()
{
    if (mod(pos.x, 2)==0){
        f_color = vec4(1.0, 0.0, 0.0, 1.0);
    }
    else{
        f_color = vec4(0.0, 1.0, 0.0, 1.0);
    }
}
