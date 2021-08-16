# Hightower's Algorithm in Python


def construct_obstacles(obstacles):
    new_obstacles = []
    for point1, point2 in obstacles:
        new_obstacle = []
        changex = point2[0] - point1[0]
        changey = point2[1] - point1[1]
        if changex != 0:
            step = 1 if changex > 0 else -1
            for i in range(0, changex+1, step):
                new_obstacle.append((point1[0]+i, point1[1]))
        if changey != 0:
            step = 1 if changey > 0 else -1
            for i in range(0, changey+step, step):
                new_obstacle.append((point1[0], point1[1]+i))
        new_obstacles.append(new_obstacle)
    return new_obstacles





def find_target(point, target, limit):
    for i in range(1, limit):
        if (point[0]+i, point[1]) == target:
            return True
        if (point[0]-i, point[1]) == target:
            return True
        if (point[0], point[1]+i) == target:
            return True
        if (point[0], point[1]-i) == target:
            return True
    return False


def closest_point(point, all_obstacles, limit):
    for i in range(1, limit):
        if find_obstacle((point[0]+i, point[1]), all_obstacles) and (point[0]+i-1, point[1]) != point:
            return (point[0]+i-1, point[1])
        if find_obstacle((point[0]-i, point[1]), all_obstacles) and (point[0]-i+1, point[1]) != point:
            return (point[0]-i+1, point[1])
        if find_obstacle((point[0], point[1]+i), all_obstacles) and (point[0], point[1]+i-1) != point:
            return (point[0], point[1]+i-1)
        if find_obstacle((point[0], point[1]-i), all_obstacles) and (point[0], point[1]-i+1) != point:
            return (point[0], point[1]-i+1)
    return None


def construct_path(point, target, all_obstacles, limit):
    if find_target(point, target, limit):
        return (point, target)
    next_point = closest_point(point, all_obstacles, limit)
    if next_point != None:
        return (point, next_point)
    else:
        return None  # NOT DONE


def hightowers(source, target, obstacles, limit):
    paths = []

    all_obstacles = construct_obstacles(obstacles)
    next_point = source
    while next_point != target:
        path = construct_path(next_point, target, all_obstacles, limit)
        next_point = path[1]
        paths.append(path)

    return paths


# source = (0, 4)
# target = (3, 3)
# obstacles = [((1, 0), (1, 4)), ((1, 4), (4, 4)), ((4, 4), (4, 1))]

# all_obstacles = construct_obstacles(obstacles)
# print(closest_point(source, all_obstacles, 10))

print(hightowers((1, 3), (2, 2), [((0, 0), (0, 4)), ((
    0, 4), (4, 4)), ((4, 4), (4, 0)), ((4, 0), (0, 0))], 5))
