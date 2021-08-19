import cairo


def render(name, start, end, obstacles, width, height, path):
    width, height = width + 2, height + 2
    path = [] if path == None else path

    scale = 100

    surface = cairo.SVGSurface(name + ".svg", width*scale, height*scale)
    context = cairo.Context(surface)
    context.scale(scale, scale)
    
    # draw start and end point
    context.set_line_width(0.05 * min(width, height))
    context.set_source_rgb(0, 0, 0)
    for x1, y1 in [start, end]:
        context.arc(x1+1, y1+1, 0.1, 0, 2*3.14159)
        context.fill()

    # draw the obstacles
    context.set_line_width(0.01 * min(width, height))
    context.set_source_rgb(255, 0, 0)
    for obstacle in obstacles:
        x1, y1 = obstacle[0]
        x2, y2 = obstacle[1]
        context.move_to(x1+1, y1+1)
        context.line_to(x2+1, y2+1)
        context.stroke()
    
    # draw the path
    context.set_source_rgb(0, 255, 0)
    for segment in path:
        x1, y1 = segment[0]
        x2, y2 = segment[1]
        context.move_to(x1+1, y1+1)
        context.line_to(x2+1, y2+1)
        context.stroke()

    surface.finish()
