# Hightower's Algorithm in Python

# point = (a, b)
# finite line = point array
# infinite line = (point, point)
# obstacles = line array


# Return True or False (DONE)
def __is_between(point, obstacle):
    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    point1, point2 = obstacle
    return distance(point, point1) + distance(point, point2) == distance(point1, point2)


# Return True or False (DONE)
def hit_obstacle(point, obstacles):
    for obstacle in obstacles:
        if __is_between(point, obstacle):
            return True
    return False


# Return a line
# CAN RETURN THE SAME POINT, CHANGE RANGE START TO 2 TO ELIMINATE RETURNING THE SAME POINT
def get_escape_line(point, obstacles, vertical, limit):
    # Condition 1: just before the line hits an obstacle
    if vertical:
        for i in range(1, limit):
            if hit_obstacle((point[0], point[1]+i), obstacles):
                return (point, (point[0], point[1]+i-1))
            if hit_obstacle((point[0], point[1]-i), obstacles):
                return (point, (point[0], point[1]-i+1))
    else:
        for i in range(1, limit):
            if hit_obstacle((point[0]+i, point[1]), obstacles):
                return (point, (point[0]+i-1, point[1]))
            if hit_obstacle((point[0]-i, point[1]), obstacles):
                return (point, (point[0]-i+1, point[1]))
    # Condition 2: just passing one of the nearest parallel obstacle line segments

    
    # Condition 3: no escape point
    if vertical:
        return (point, (point[0], point[1]+1))
    else:
        return (point, (point[0]+1, point[1]))


# Return a point or None 
def get_intersection(line1, line2):
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    div = det(xdiff, ydiff)
    if div == 0:
        return None
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (int(x), int(y))


# Return True or False
def check_obstacles(line1, line2, obstacles):
    pass


def hightowers(source, target, obstacles, limit):
    path = []

    point1 = source
    point2 = target

    vertical = True

    line1 = get_escape_line(point1, obstacles, vertical, limit)
    vertical = not vertical
    line2 = get_escape_line(point2, obstacles, vertical, limit)
    intersection = get_intersection(line1, line2)
    if intersection != None:
        check_obstacle(line1, line2, obstacles)