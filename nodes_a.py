class Node:
    def __init__(self, location_x, location_y, g_cost, h_cost, f_cost, came_from):
        self.location_x = location_x
        self.location_y = location_y
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = f_cost
        neighbours = []
        self.neighbours = neighbours
        self.came_from = came_from
