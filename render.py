import cairo


def render(name, obstacles, width, height, path):
    surface = cairo.SVGSurface(name + ".svg", width, height)
    context = cairo.Context(surface)
    context.scale(width, height)
    context.set_line_width(0.04)
    # draw the obstacles
    for obstacle in obstacles:
        x1, y1 = obstacle[0]
        x2, y2 = obstacle[1]
        context.move_to(x1, y1)
        context.line_to(x2, y2)
        context.stroke()
    # change color to green
    context.set_source_rgb(0, 255, 0)
    # draw the path
    for segment in path:
        x1, y1 = segment[0]
        x2, y2 = segment[1]
        context.move_to(x1, y1)
        context.line_to(x2, y2)
        context.stroke()

    surface.finish()
