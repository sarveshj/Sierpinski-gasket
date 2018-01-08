def get_midpoints(point1, point2):
    return (0.5 *(point1[0]+point2[0]), 0.5 *(point1[1]+point2[1])  )

def gen_sierpinski(points, level, step_size, my_turtle):#, counter):
    """
    I/P : midpoints, current level, step size, turtle object
    O/P : visualization of Sierpinski Triangle
    """
    
    print("level is" + str(level)  )
    
    if  level > 0:
    
        p0 = points[0]
        p1 = points[1]
        p2 = points[2]

        #turtl fill color
        color_val = level * step_size
        my_turtle.fillcolor(color_val,color_val,color_val)
        
        #go to 1st corner
        my_turtle.up()
        my_turtle.goto(p0[0],p0[1])
        my_turtle.down()

        #p0 --> p1 and start filling
        my_turtle.begin_fill()
        my_turtle.goto(p1[0],p1[1])

        #p1 --> p2
        my_turtle.goto(p2[0],p2[1])

        #p2 -->p0
        my_turtle.goto(p0[0],p0[1])

        #stop filling
        my_turtle.end_fill()

        
        #generate mid points for each sides
        
        gen_sierpinski([p0, get_midpoints(p0,p1), get_midpoints(p0,p2)], level -1 , step_size, my_turtle)
        gen_sierpinski([p1, get_midpoints(p0,p1), get_midpoints(p1,p2)], level -1 , step_size, my_turtle)
        gen_sierpinski([p2, get_midpoints(p2,p1), get_midpoints(p0,p2)], level -1 , step_size, my_turtle)
        
   
def main():    
    
    import turtle

    my_turtle = turtle.Turtle()
    my_turtle.speed(1)
    screen = turtle.Screen()
    screen.colormode(255)


    level = 3
    points =[[-100,-50],[0,100],[100,-50]]
    step_size = 255 // level

    #counter to create gif
    counter = 0
    gen_sierpinski(points, level, step_size,my_turtle)
    
    #hide the turtle when done! also save the image!
    my_turtle.hideturtle()
    my_turtle.done()
    
    
#excecute code    
main()
