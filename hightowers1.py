# Hightower's Algorithm in Python

# point = (a, b)
# line = (point, point)
# obstacles = [line, line, ... , line]


# Return True or False (DONE)
def is_between(point, obstacle):
    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    point1, point2 = obstacle
    return distance(point, point1) + distance(point, point2) == distance(point1, point2)


# Return True or False (DONE)
def find_obstacle(point, obstacles):
    for obstacle in obstacles:
        if is_between(point, obstacle):
            return True
    return False


# Return a line or None
def construct_escape_line(point, obstacles, vertical, limit):
    # Condition 1: just before the line hits an obstacle
    if vertical:
        for i in range(1, limit):
            if find_obstacle((point[0], point[1]+i), obstacles):
                return (point, (point[0], point[1]+i-1))
            if find_obstacle((point[0], point[1]-i), obstacles):
                return (point, (point[0], point[1]-i+1))
    else:
        for i in range(1, limit):
            if find_obstacle((point[0]+i, point[1]), obstacles):
                return (point, (point[0]+i-1, point[1]))
            if find_obstacle((point[0]-i, point[1]), obstacles):
                return (point, (point[0]-i+1, point[1]))
    
    # Condition 2: just passing one of the mearest parallel obstacle line segments
    
    # TODO: return (point, escape_point) when parallel obstable
    return None


# Return a point or None (NOT DONE, DOES NOT ACCOUNT FOR OBSTACLES)
def find_intersection(line1, line2):
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


def hightowers(source, target, obstacles, limit):
    point1 = source
    point2 = target

    vertical = True
    while True:
        line1 = construct_escape_line(point1, obstacles, vertical, limit)
        vertical = not vertical
        line2 = construct_escape_line(point2, obstacles, vertical, limit)
        if line1 != None and line2 != None:
            intersection = find_intersection(line1, line2)
            if intersection != None:
                path1.append((point1, intersection))
                path2.append((intersection, point2))
                return path1 + path2
            point1 = path1[1]
            point2 = path2[0]


print(hightowers((1, 3), (3, 1), [((0, 0), (0, 4)), ((
    0, 4), (4, 4)), ((4, 4), (4, 0)), ((4, 0), (0, 0))], 5))
