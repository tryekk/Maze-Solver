class Node:
    def __init__(self, name, distance, working_val, came_from):
        self.name = name
        self.distance = distance
        self.working_val = working_val
        self.came_from = came_from
