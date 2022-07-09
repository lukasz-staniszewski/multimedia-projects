#version 330

in vec2 vert_pos;
uniform vec2 center_fract;
uniform float scale;
uniform int n_of_iterations;
uniform float asp_ratio;
out vec4 frag_color;

void main()
{
    // at first we need to specify point p - we need to correctly scale it on screen, apply aspect_ratio and add shift 
    // because in each recursive equation p is constant - lets create p apart
    vec2 p;
    // x and y will be scalled by scale, but also x need to be multiplied by >1 fraction (because we use 16:9 ratio with width > hight)
    p.x = scale*asp_ratio*vert_pos.x + center_fract.x;
    p.y = scale*vert_pos.y + center_fract.y;
    // our iteration starts with 0
    int i=0;
    // and z will start with value p, because z_1 = 0^2 + p = p
    vec2 z = p;
    while(i<n_of_iterations){
        // we will do modifications on z directly, so its safe to create temporary copy of it
        vec2 temp_z = z;
        // math equation for real part in complex number squaring + adding p.x according to equation 
        z.x =  (z.x * z.x - z.y * z.y) + p.x;
        // math equation for imaginary part in complex number squaring + adding p.y according to equation
        z.y = 2*temp_z.x*z.y + p.y;
        // if in n iterations exists a complex number thats module is higher than 2, point p doesnt belong to mandelbrot set  
        if((z.x*z.x + z.y*z.y)>4.0){
            break;
        }
        i++;
    }
    // if in n iterations we know that point p (pixel p) does not belong to mandelbrot set, its color is black
    if (i < n_of_iterations){
        frag_color = vec4(0.0f, 0.0f, 0.0f, 1.0f);
    }
    // else - if in n iterations we suppose that point p (pixel p) belongs to mandelbrot set, its color is blue
    else{
        frag_color = vec4(0.15f, 0.20f, 0.76f, 1.0f);
    }

}
