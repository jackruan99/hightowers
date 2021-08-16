# Hightower's Algorithm in Python


class Line:
    def __init__(self, line, orientation):
        self.line = line
        self.orientation = orientation

    def get_line(self):
        return self.line

    def get_orientation(self):
        return self.orientation

    def set_orientation(self, orientation):
        self.orientation = orientation


def separate_obstacles(obstacles):
    horizontal_obstacles, vertical_obstacles = [], []
    for point1, point2 in obstacles:
        if point1[0] - point2[0] != 0:
            horizontal_obstacles.append(Line((point1, point2), 'H'))
        elif point1[1] - point2[1] != 0:
            vertical_obstacles.append(Line((point1, point2), 'V'))
    return horizontal_obstacles, vertical_obstacles


def create_escape_line(object_point, orientation, grid_width, grid_height):
    if orientation == 'H':
        return Line(((0, object_point[1]), (grid_width, object_point[1])), 'H')
    if orientation == 'V':
        return Line(((object_point[0], 0), (object_point[0], grid_height)), 'V')


def get_intersection(line1, line2):
    line1, line2 = line1.get_line(), line2.get_line()
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


def intersect(line1, line2):
    line1, orientation1 = line1.get_line(), line1.get_orientation()
    line2, orientation2 = line2.get_line(), line2.get_orientation()
    if orientation1 == 'H' and orientation2 == 'V':
        point11, point12 = line1
        point21, point22 = line2
        if point11[0] < point12[0] and point21[1] < point22[1]:
            return point11[0] <= point21[0] and point22[0] <= point12[0] and point21[1] <= point11[1] and point12[1] <= point22[1]
        elif point11[0] > point12[0] and point21[1] < point22[1]:
            return point12[0] <= point21[0] and point22[0] <= point11[0] and point21[1] <= point12[1] and point11[1] <= point22[1]
        elif point11[0] < point12[0] and point21[1] > point22[1]:
            return point11[0] <= point22[0] and point21[0] <= point12[0] and point22[1] <= point11[1] and point12[1] <= point21[1]
        elif point11[0] > point12[0] and point21[1] > point22[1]:
            return point12[0] <= point22[0] and point21[0] <= point11[0] and point22[1] <= point12[1] and point11[1] <= point21[1]
    elif orientation1 == 'V' and orientation2 == 'H':
        point11, point12 = line2
        point21, point22 = line1
        if point11[0] < point12[0] and point21[1] < point22[1]:
            return point11[0] <= point21[0] and point22[0] <= point12[0] and point21[1] <= point11[1] and point12[1] <= point22[1]
        elif point11[0] > point12[0] and point21[1] < point22[1]:
            return point12[0] <= point21[0] and point22[0] <= point11[0] and point21[1] <= point12[1] and point11[1] <= point22[1]
        elif point11[0] < point12[0] and point21[1] > point22[1]:
            return point11[0] <= point22[0] and point21[0] <= point12[0] and point22[1] <= point11[1] and point12[1] <= point21[1]
        elif point11[0] > point12[0] and point21[1] > point22[1]:
            return point12[0] <= point22[0] and point21[0] <= point11[0] and point22[1] <= point12[1] and point11[1] <= point21[1]   
    return False


def check_obstacles(intersection, object_point1, object_point2, line1_orientation, line2_orientation, horizontal_obstacles, vertical_obstacles):
    if line1_orientation == 'H' and line2_orientation == 'V':
        line1 = (intersection, object_point1) if intersection[0] < object_point1[0] else (object_point1, intersection)
        obstacles = vertical_obstacles
        for obstacle in obstacles:
            if intersect(Line(line1, line1_orientation), obstacle):
                return True
        line2 = (intersection, object_point2) if intersection[1] < object_point2[1] else (object_point2, intersection)
        obstacles = horizontal_obstacles
        for obstacle in obstacles:
            if intersect(Line(line2, line2_orientation), obstacle):
                return True
    elif line1_orientation == 'V' and line2_orientation == 'H':
        line1 = (intersection, object_point1) if intersection[1] < object_point1[1] else (object_point1, intersection)
        obstacles = horizontal_obstacles
        for obstacle in obstacles:
            if intersect(Line(line1, line1_orientation), obstacle):
                return True
        line2 = (intersection, object_point2) if intersection[0] < object_point2[0] else (object_point2, intersection)
        obstacles = vertical_obstacles
        for obstacle in obstacles:
            if intersect(Line(line2, line2_orientation), obstacle):
                return True
    return False 


def on_the_line(point, line):
    if line.get_orientation() == 'H':
        return (line.get_line()[0][1] == point[1]) and ((line.get_line()[0][0] <= point[0] and point[0] <= line.get_line()[1][0]) or (line.get_line()[0][0] >= point[0] and point[0] >= line.get_line()[1][0]))
    elif line.get_orientation() == 'V':
        return (line.get_line()[0][0] == point[0]) and ((line.get_line()[0][1] <= point[1] and point[1] <= line.get_line()[1][1]) or (line.get_line()[0][1] >= point[1] and point[1] >= line.get_line()[1][1]))
    return False


def on_the_line2(point, line):
    if line.get_orientation() == 'H':
        return line.get_line()[0][1] == point[1]
    elif line.get_orientation() == 'V':
        return line.get_line()[0][0] == point[0]
    return False

def hit_obstacle(point, obstacles):
    if point != None:
        for obstacle in obstacles:
            if on_the_line(point, obstacle):
                return True
    return False


def get_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


def get_closest_parallel_obstacles(object_point, escape_line, horizontal_obstacles, vertical_obstacles, grid_width, grid_height):
    closest_parallel_obstacles1, closest_parallel_obstacles2 = [], []
    if escape_line.get_orientation() == 'V':
        obstacles = vertical_obstacles
        go_left, go_right = object_point[0] > 0, object_point[0] < grid_width
        step = 1
        while True:
            if go_left:
                left = object_point[0] - step
                for obstacle in obstacles:
                    if on_the_line2((left, object_point[1]), obstacle):
                        closest_parallel_obstacles1.append(obstacle)
                if left <= 0:
                    go_left = False
            if go_right:
                right = object_point[0] + step
                for obstacle in obstacles:
                    if on_the_line2((right, object_point[1]), obstacle):
                        closest_parallel_obstacles1.append(obstacle)
                if right >= grid_width:
                    go_right = False
            if len(closest_parallel_obstacles1) > 0 or not (go_left or go_right):
                break
            step += 1
    elif escape_line.get_orientation() == 'H':
        obstacles = horizontal_obstacles
        go_down, go_up = object_point[1] > 0, object_point[1] < grid_height
        step = 1
        while True:
            if go_down:
                down = object_point[1] - step
                for obstacle in obstacles:
                    if on_the_line2((object_point[0], down), obstacle):
                        closest_parallel_obstacles2.append(obstacle)
                if down <= 0:
                    go_down = False
            if go_up:
                up = object_point[1] + step
                for obstacle in obstacles:
                    if on_the_line2((object_point[0], up), obstacle):
                        closest_parallel_obstacles2.append(obstacle)
                if up >= grid_height:
                    go_up = False
            if len(closest_parallel_obstacles2) > 0 or not (go_down or go_up) :
                break
            step += 1
    if len(closest_parallel_obstacles1) > 1:
        closest_distance = grid_width + grid_height
        closest_obstacle = None
        for obstacle in closest_parallel_obstacles1:
            for point in obstacle.get_line():
                distance = get_distance(point, object_point)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_obstacle = obstacle
        closest_parallel_obstacles1 = [closest_obstacle]
    if len(closest_parallel_obstacles2) > 1:
        closest_distance = grid_width + grid_height
        closest_obstacle = None
        for obstacle in closest_parallel_obstacles2:
            for point in obstacle.get_line():
                distance = get_distance(point, object_point)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_obstacle = obstacle
        closest_parallel_obstacles2 = [closest_obstacle]
    return closest_parallel_obstacles1 + closest_parallel_obstacles2

def pass_closest_parallel_obstacle(point, orientation, obstacles, grid_width, grid_height):
    if orientation == 'H':
        line = create_escape_line(point, 'V', grid_width, grid_height)
        for obstacle in obstacles:
            if not intersect(line, obstacle):
                return True
    elif orientation == 'V':
        line = create_escape_line(point, 'H', grid_width, grid_height)
        for obstacle in obstacles:
            if not intersect(line, obstacle):
                return True
    return False


def get_escape_point(object_point, escape_line, escape_points, horizontal_obstacles, vertical_obstacles, grid_width, grid_height):
    # Condition 1 & 2
    closest_parallel_obstacles = get_closest_parallel_obstacles(object_point, escape_line, horizontal_obstacles, vertical_obstacles, grid_width, grid_height)
    if escape_line.get_orientation() == 'H':
        obstacles = vertical_obstacles + horizontal_obstacles
        go_left, go_right = object_point[0] > 0, object_point[0] < grid_width
        step = 1
        while True:
            if go_left:
                left = object_point[0] - step
                if left <= 0:
                    go_left = False
                if hit_obstacle((left, object_point[1]), obstacles):
                    if step == 1:
                        go_left = False
                    else:
                        return (left + 1, object_point[1])
                elif pass_closest_parallel_obstacle((left, object_point[1]), escape_line.get_orientation(), closest_parallel_obstacles, grid_width, grid_height):
                    return (left, object_point[1])
                elif (left, object_point[1]) in escape_points:
                    go_left = False
            if go_right:
                right = object_point[0] + step
                if right >= grid_width:
                    go_right = False
                if hit_obstacle((right, object_point[1]), obstacles):
                    if step == 1:
                        go_right = False
                    else:
                        return (right - 1, object_point[1])
                elif pass_closest_parallel_obstacle((right, object_point[1]), escape_line.get_orientation(), closest_parallel_obstacles, grid_width, grid_height):
                    return (right, object_point[1])
                elif (right, object_point[1]) in escape_points:
                    go_right = False
            if not go_left and not go_right:
                break
            step += 1
    if escape_line.get_orientation() == 'V':
        obstacles = vertical_obstacles + horizontal_obstacles
        go_down, go_up = object_point[1] > 0, object_point[1] < grid_height
        step = 1
        while True:
            if go_down:
                down = object_point[1] - step
                if down <= 0:
                    go_down = False
                if hit_obstacle((object_point[0], down), obstacles):
                    if step == 1:
                        go_down = False
                    else:
                        return (object_point[0], down + 1)
                elif pass_closest_parallel_obstacle((object_point[0], down), escape_line.get_orientation(), closest_parallel_obstacles, grid_width, grid_height):
                    return (object_point[0], down)
                elif (object_point[0], down) in escape_points:
                    go_down = False
            if go_up:
                up = object_point[1] + step
                if up >= grid_height:
                    go_up = False
                if hit_obstacle((object_point[0], up), obstacles):
                    if step == 1:
                        go_up = False
                    else:
                        return (object_point[0], up - 1)
                elif pass_closest_parallel_obstacle((object_point[0], up), escape_line.get_orientation(), closest_parallel_obstacles, grid_width, grid_height):
                    return (object_point[0], up)
                elif (object_point[0], up) in escape_points:
                    go_up = False
            if not go_down and not go_up:
                break
            step += 1
    # Condition 3
    return None


def change_orientation(orientation):
    if orientation == 'V':
        return 'H'
    if orientation == 'H':
        return 'V'


# Hightower's Algorithm
def hightowers(source, target, obstacles, grid_width, grid_height):
    object_point1, object_point2 = source, target
    orientation1, orientation2 = 'H', 'V'
    horizontal_obstacles, vertical_obstacles = separate_obstacles(obstacles)
    escape_points = [source, target]
    
    path1, path2 = [], []
    tries = 1
    while True:
        # STEP 1
        line1 = create_escape_line(object_point1, orientation1, grid_width, grid_height)
        line2 = create_escape_line(object_point2, orientation2, grid_width, grid_height)
        intersection = get_intersection(line1, line2)
        if intersection != None:
            if not check_obstacles(intersection, object_point1, object_point2, line1.get_orientation(), line2.get_orientation(), horizontal_obstacles, vertical_obstacles):
                if object_point1 != intersection:
                    path1.append((object_point1, intersection))
                if object_point2 != intersection:
                    path2.append((intersection, object_point2))
                path2.reverse()
                return path1 + path2
        else:
            raise ValueError('NO INTERSECTION!')
        # STEP 2
        escape_point1 = get_escape_point(object_point1, line1, escape_points, horizontal_obstacles, vertical_obstacles, grid_width, grid_height)
        print(escape_point1)
        escape_point2 = get_escape_point(object_point2, line2, escape_points, horizontal_obstacles, vertical_obstacles, grid_width, grid_height)
        print(escape_point2)
        if escape_point1 != None and escape_point2 != None:
            old_object_point1 = object_point1
            old_object_point2 = object_point2
            object_point1 = escape_point1
            object_point2 = escape_point2
            path1.append((old_object_point1, object_point1))
            path2.append((object_point2, old_object_point2))
            orientation1 = change_orientation(orientation1)
            orientation2 = change_orientation(orientation2)
            if old_object_point1 not in escape_points:
                escape_points.append(old_object_point1)
            if old_object_point2 not in escape_points:
                escape_points.append(old_object_point2)
            tries = 1
        elif escape_point1 != None:
            old_object_point1 = object_point1
            object_point1 = escape_point1
            path1.append((old_object_point1, object_point1))
            orientation1 = change_orientation(orientation1)
            orientation2 = change_orientation(orientation2)
            if old_object_point1 not in escape_points:
                escape_points.append(old_object_point1)
            tries = 1
        elif escape_point2 != None:
            old_object_point2 = object_point2
            object_point2 = escape_point2
            path2.append((object_point2, old_object_point2))
            orientation1 = change_orientation(orientation1)
            orientation2 = change_orientation(orientation2)
            if old_object_point2 not in escape_points:
                escape_points.append(old_object_point2)
            tries = 1
        else:
            if tries == 2:
                break
            else:
                orientation1 = change_orientation(orientation1)
                orientation2 = change_orientation(orientation2)
                tries += 1



# print(intersect(Line(((1, 1), (1, 3)), 'V'), Line(((0, 0), (3, 0)), 'H')))
# print(check_obstacles((3, 3), (1, 3), (3, 1), 'H', 'V', [Line(((0, 4), (4, 4)), 'H'), Line(((4, 0), (0, 0)), 'H')], [Line(((0, 0), (0, 4)), 'V'), Line(((4, 4), (4, 0)), 'V')]))
# print(get_closest_parallel_obstacles((2, 2), Line(((2, 0), (2, 4)), 'V'), [Line(((0, 4), (4, 4)), 'H'), Line(((4, 0), (0, 0)), 'H')], [Line(((0, 0), (0, 4)), 'V'), Line(((4, 4), (4, 0)), 'V')], 4, 4))
# print(pass_closest_parallel_obstacle((4, 2), 'H', [Line(((0, 4), (3, 4)), 'H'), Line(((4, 0), (0, 0)), 'H')], 4, 4))