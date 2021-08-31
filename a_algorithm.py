from nodes_a import Node
import a_star_grid_store


class Algorithm:
    def __init__(self, heuristic_choice, diagonal_enabled, a_star_grid_top):
        # Refresh grid (clear old path)
        a_star_grid_store.refresh_grid()
        # Calling A* adjacency matrix from file
        self.matrix = a_star_grid_store.Grid().matrix

        self.a_star_grid_top = a_star_grid_top

        # Setting start and end point from grid
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if self.matrix[row][col].value == 2:
                    start_x = row
                    start_y = col
                elif self.matrix[row][col].value == 3:
                    end_x = row
                    end_y = col

        # Setting start and end node
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

        # Defining variables
        self.end_node = [end_x, end_y]  # Setting end_node's location
        self.open_set = []  # List of all unexplored nodes
        self.closed_set = []  # List of calculated nodes
        self.neighbours = []  # List of node's neighbours
        self.heuristic = None  # Defining heuristic variable
        self.path_nodes = []  # Explored nodes
        self.path = None  # Output to display on GUI
        self.final_path = []  # Final path
        self.current_location = None  # Defining current location of node as tuple
        self.wall_count = 0  # Number of walls
        # Controls main loop for algorithm
        self.looping = True

        # Algorithm parameters from user input in GUI
        self.heuristic_choice = heuristic_choice  # Getting from GUI file
        self.diagonal_enabled = diagonal_enabled  # Option for diagonal paths
        self.round_costs = 1  # Choose to round displayed costs

        # Calculating number of walls for output on GUI
        row_no = 0
        col_no = 0
        for row in self.matrix:
            for col in row:
                if self.matrix[row_no][col_no].value == 1:
                    self.wall_count += 1
                col_no += 1
                col_no = col_no % 8  # Max col no = 6
            row_no += 1

        # Setting start node's attributes
        self.current = Node(start_x, start_y, 0, 0, 0, self.neighbours)
        # Adding start to open set in order to have values calculated
        self.open_set.append(self.current)

        # Displaying cost for start node
        if self.round_costs == 0:
            g_split = str(float(self.calculate_heuristic(self.current, None, 'g'))).split('.')
            g_value = '%2d.%s' % (int(g_split[0]), str(g_split[1])[:1])
            h_split = str(float(self.calculate_heuristic(self.current, None, 'h'))).split('.')
            h_value = '%2d.%s' % (int(h_split[0]), str(h_split[1])[:1])
            f_split = str(float(self.calculate_heuristic(self.current, None, 'f'))).split('.')
            f_value = '%.0f.%s' % (int(f_split[0]), str(f_split[1])[:1])
            self.matrix[self.current.location_x][self.current.location_y].cost = '{} {}\n{}'.format(
                g_value, h_value, f_value)
        else:
            g_split = str(float(self.calculate_heuristic(self.current, None, 'g'))).split('.')
            g_value = '%2d.%s' % (int(g_split[0]), str(round(float(
                g_split[1]), -(len(str(g_split[1])) - 1)))[:1])
            h_split = str(float(self.calculate_heuristic(self.current, None, 'h'))).split('.')
            h_value = '%2d.%s' % (int(h_split[0]), str(round(float(
                h_split[1]), -(len(str(h_split[1])) - 1)))[:1])
            f_split = str(float(self.calculate_heuristic(self.current, None, 'f'))).split('.')
            f_value = '%d.%s' % (int(f_split[0]), str(round(float(
                f_split[1]), -(len(str(f_split[1])) - 1)))[:1])
            self.matrix[self.current.location_x][self.current.location_y].cost = '{} {}\n{}'.format(
                g_value, h_value, f_value)

        # Running next functions
        self.calculate_cost()

    def calculate_heuristic(self, node, target, cost):
        if cost == 'dist':
            # Euclidean distance from current neighbour to previous node (distance to moved to get to this node)
            x = node.location_x - target.location_x
            y = node.location_y - target.location_y
            distance = ((x ** 2) + (y ** 2)) ** 0.5
            # Returning distance
            self.heuristic = distance
            # Round if using algorithm #3
            if self.heuristic_choice == 2:
                if len(str(self.heuristic)) > 12:
                    self.heuristic = round(float(self.heuristic), 12)
        # <None> (target) by default will be start or end depending on choice of cost
        # If manhattan chosen or Euclidean chosen calculate differently
        if self.heuristic_choice == 0:
            # Manhattan distance
            if cost == 'f':
                # g_cost = manhattan distance from start
                x = node.location_x - self.start_x
                y = node.location_y - self.start_y
                g_distance = abs(x) + abs(y)
                # h_cost = manhattan distance from end
                a = self.end_x - node.location_x
                b = self.end_y - node.location_y
                h_distance = abs(a) + abs(b)
                # Returning final f_cost
                self.heuristic = h_distance + g_distance
            elif cost == 'g':
                # g_cost = manhattan distance from current to start
                x = node.location_x - self.start_x
                y = node.location_y - self.start_y
                g_distance = abs(x) + abs(y)
                # Returning g_cost
                self.heuristic = g_distance
            elif cost == 'h':
                # h_cost = manhattan distance from end
                a = self.end_x - node.location_x
                b = self.end_y - node.location_y
                h_distance = abs(a) + abs(b)
                # Returning h_cost
                self.heuristic = h_distance
        elif self.heuristic_choice == 1:
            # Euclidean distance
            if cost == 'f':
                # g_cost = euclidean distance from start
                x = node.location_x - self.start_x
                y = node.location_y - self.start_y
                g_distance = ((x ** 2) + (y ** 2)) ** 0.5
                # h_cost = euclidean distance from end
                a = self.end_x - node.location_x
                b = self.end_y - node.location_y
                h_distance = ((a ** 2) + (b ** 2)) ** 0.5
                # Returning final f_cost
                self.heuristic = h_distance + g_distance
            elif cost == 'g':
                # g_cost = euclidean distance from current to start
                x = node.location_x - self.start_x
                y = node.location_y - self.start_y
                g_distance = ((x ** 2) + (y ** 2)) ** 0.5
                # Returning g_cost
                self.heuristic = g_distance
            elif cost == 'h':
                # h_cost = euclidean distance from end
                a = self.end_x - node.location_x
                b = self.end_y - node.location_y
                h_distance = ((a ** 2) + (b ** 2)) ** 0.5
                # Returning h_cost
                self.heuristic = h_distance
        elif self.heuristic_choice == 2:
            # Tom's Heuristic
            # Path distance
            if cost == 'f':
                # g_cost = distance from start
                x = node.location_x - self.start_x
                y = node.location_y - self.start_y
                x = abs(x)
                y = abs(y)
                if x < y:
                    # Euclidean for shortest side + Manhattan for remaining len of longer
                    g_distance_euclidean = ((x ** 2) + (x ** 2)) ** 0.5
                    g_distance_manhattan = y - x
                else:
                    g_distance_euclidean = ((y ** 2) + (y ** 2)) ** 0.5
                    g_distance_manhattan = x - y
                # Final g cost
                g_distance = g_distance_euclidean + g_distance_manhattan
                # h_cost = distance from end
                a = self.end_x - node.location_x
                b = self.end_y - node.location_y
                a = abs(a)
                b = abs(b)
                if a < b:
                    # Euclidean for shortest side + Manhattan for remaining len of longer
                    h_distance_euclidean = ((a ** 2) + (a ** 2)) ** 0.5
                    h_distance_manhattan = b - a
                else:
                    h_distance_euclidean = ((b ** 2) + (b ** 2)) ** 0.5
                    h_distance_manhattan = a - b
                # Final h cost
                h_distance = h_distance_euclidean + h_distance_manhattan
                # Returning final f_cost
                self.heuristic = h_distance + g_distance
                if len(str(self.heuristic)) > 12:
                    self.heuristic = round(float(self.heuristic), 12)
            elif cost == 'g':
                x = node.location_x - self.start_x
                y = node.location_y - self.start_y
                x = abs(x)
                y = abs(y)
                if x < y:
                    # Euclidean for shortest side + Manhattan for remaining len of longer
                    g_distance_euclidean = ((x ** 2) + (x ** 2)) ** 0.5
                    g_distance_manhattan = y - x
                else:
                    g_distance_euclidean = ((y ** 2) + (y ** 2)) ** 0.5
                    g_distance_manhattan = x - y
                # Returning g_cost - Euclidean + Manhattan
                self.heuristic = g_distance_euclidean + g_distance_manhattan
            elif cost == 'h':
                a = self.end_x - node.location_x
                b = self.end_y - node.location_y
                a = abs(a)
                b = abs(b)
                if a < b:
                    # Euclidean for shortest side + Manhattan for remaining len of longer
                    h_distance_euclidean = ((a ** 2) + (a ** 2)) ** 0.5
                    h_distance_manhattan = b - a
                else:
                    h_distance_euclidean = ((b ** 2) + (b ** 2)) ** 0.5
                    h_distance_manhattan = a - b
                # Returning h_cost - Euclidean + Manhattan
                self.heuristic = h_distance_euclidean + h_distance_manhattan
        return self.heuristic

    def calculate_cost(self):
        while self.looping and len(self.open_set) > 0:
            # When end is reached update and output
            if [self.current.location_x, self.current.location_y] == self.end_node:
                self.display_on_grid()
            else:
                # Current node is set as the node with lowest F cost in openSet
                f_cost_list = {}
                item_position = 0
                for item in self.open_set:
                    # Appending f_cost attribute with an ord number to dict
                    f_cost_list[item_position] = item.f_cost
                    item_position += 1  # Increasing item position as lost is iterated through
                # Getting all nodes with the lowest (equal) f_cost
                min_value = min(f_cost_list.values())
                lowest_nodes = [k for k in f_cost_list if f_cost_list[k] == min_value]
                # Checking for node with lowest h_cost if multiple with same f_cost
                h_cost_list = {}
                item_position = 0
                # For each node in the lowest f_cost list
                for node_position in lowest_nodes:
                    node = self.open_set[node_position]
                    # Add the node's h_cost to h_cost dict
                    h_cost_list[item_position] = node.h_cost
                    item_position += 1
                # Choose lowest h_cost from dict
                node_choice = min(h_cost_list, key=h_cost_list.get)
                # Setting current as the node with lowest h_cost from list of lowest f_cost positions
                self.current = self.open_set[lowest_nodes[node_choice]]

                # Removing current node from open-set now it has been evaluated
                del self.open_set[lowest_nodes[node_choice]]
                # Current to closed now it has been evaluated
                self.closed_set.append(self.current)

                # Adding nodes to explored nodes list to be displayed on grid
                self.path_nodes.append(Node(self.current.location_x, self.current.location_y, self.current.g_cost,
                                            self.current.h_cost, self.current.f_cost, self.current.neighbours))

                # Marking current node on grid with '#'
                if self.matrix[self.current.location_x][self.current.location_y].value != 3:
                    self.matrix[self.current.location_x][self.current.location_y].value = 4  # Colour value

                # Stop evaluating neighbours once end is reached
                if [self.current.location_x, self.current.location_y] == self.end_node:
                    self.looping = False
                    self.output_data()
                else:
                    # Adding node's neighbours to current.neighbour list attribute
                    if self.current.location_x < 7:  # If the node is at least one place away from the edge
                        if self.matrix[self.current.location_x + 1][self.current.location_y].value != 1:
                            self.current.neighbours.append(Node(self.current.location_x + 1, self.current.location_y, 0,
                                                                0, 0, None))
                    if self.current.location_x > 0:
                        if self.matrix[self.current.location_x - 1][self.current.location_y].value != 1:
                            self.current.neighbours.append(Node(self.current.location_x - 1, self.current.location_y, 0,
                                                                0, 0, None))
                    if self.current.location_y < 7:
                        if self.matrix[self.current.location_x][self.current.location_y + 1].value != 1:
                            self.current.neighbours.append(Node(self.current.location_x, self.current.location_y + 1, 0,
                                                                0, 0, None))
                    if self.current.location_y > 0:
                        if self.matrix[self.current.location_x][self.current.location_y - 1].value != 1:
                            self.current.neighbours.append(Node(self.current.location_x, self.current.location_y - 1, 0,
                                                                0, 0, None))
                    # Only add diagonals is the option is enabled
                    if self.diagonal_enabled == 1:
                        # Diagonal neighbours (will have a distance from current of 1.42 instead of 1)
                        if self.current.location_x < 7 and self.current.location_y < 7:
                            # Diagonal
                            if self.matrix[self.current.location_x + 1][self.current.location_y + 1].value != 1:
                                self.current.neighbours.append(Node(self.current.location_x + 1, self.current.location_y
                                                                    + 1, 0, 0, 0, None))
                        if self.current.location_x > 0 and self.current.location_y > 0:
                            # Diagonal
                            if self.matrix[self.current.location_x - 1][self.current.location_y - 1].value != 1:
                                self.current.neighbours.append(Node(self.current.location_x - 1, self.current.location_y
                                                                    - 1, 0, 0, 0, None))
                        if self.current.location_x > 0 and self.current.location_y < 7:
                            # Diagonal
                            if self.matrix[self.current.location_x - 1][self.current.location_y + 1].value != 1:
                                self.current.neighbours.append(Node(self.current.location_x - 1, self.current.location_y
                                                                    + 1, 0, 0, 0, None))
                        if self.current.location_x < 7 and self.current.location_y > 0:
                            # Diagonal
                            if self.matrix[self.current.location_x + 1][self.current.location_y - 1].value != 1:
                                self.current.neighbours.append(Node(self.current.location_x + 1, self.current.location_y
                                                                    - 1, 0, 0, 0, None))

                    # Creating list of locations of closed nodes for comparison to each neighbour node
                    closed_nodes = []
                    for node in self.closed_set:
                        closed_nodes.append([node.location_x, node.location_y])
                    # Creating list of locations of open nodes for comparison to each neighbour node
                    open_nodes = []
                    for node in self.open_set:
                        open_nodes.append([node.location_x, node.location_y])

                    for neighbour in self.current.neighbours:
                        # If in closed don't explore
                        if [neighbour.location_x, neighbour.location_y] in closed_nodes:
                            continue
                        # Adding the distance the current is from the neighbour being evaluated to the g_cost
                        move_distance = self.calculate_heuristic(self.current, neighbour, 'dist')  # Move distance
                        # Adding distance moved to g cost
                        temporary_g = self.current.g_cost + move_distance
                        # Subtracting distance moved from the h cost
                        temporary_h = self.calculate_heuristic(neighbour, None, 'h')  # - move_distance

                        if [neighbour.location_x, neighbour.location_y] not in open_nodes:
                            # If neighbour not already in open set assign it a cost and append it
                            neighbour.g_cost = temporary_g
                            # New f cost is (h cost + g cost)
                            neighbour.h_cost = temporary_h
                            # neighbour.f_cost = self.calculate_heuristic(neighbour, None, 'f')
                            neighbour.f_cost = neighbour.h_cost + neighbour.g_cost
                            self.open_set.append(neighbour)
                            if self.matrix[neighbour.location_x][neighbour.location_y].value != 3:
                                self.matrix[neighbour.location_x][neighbour.location_y].value = 9  # Colour value
                            # Runs function that formats costs for display
                            self.display_costs(neighbour)

                        elif temporary_g < neighbour.g_cost:
                            neighbour.g_cost = temporary_g
                            # New f cost is (h cost + g cost)
                            neighbour.h_cost = temporary_h
                            neighbour.f_cost = self.calculate_heuristic(neighbour, None, 'f')
                            # neighbour.f_cost = neighbour.h_cost + neighbour.g_cost
                            self.open_set.append(neighbour)
                            if self.matrix[neighbour.location_x][neighbour.location_y].value != 3:
                                self.matrix[neighbour.location_x][neighbour.location_y].value = 9  # Colour value
                            # Runs function that formats costs for display
                            self.display_costs(neighbour)
                        # Adding the current node as the one that the neighbour was on previously (for final path)
                        neighbour.came_from = self.current
            # Update the matrix values for analysis
            self.display_on_grid()

    def display_costs(self, neighbour):
        # Displaying cost
        if self.round_costs == 0:  # Don't round
            g_split = str(float(neighbour.g_cost)).split('.')
            # Rounds integer to 2sf and shortens decimal to 1sf then joins
            g_value = '%2d.%s' % (int(g_split[0]), str(g_split[1])[:1])
            h_split = str(float(neighbour.h_cost)).split('.')
            h_value = '%2d.%s' % (int(h_split[0]), str(h_split[1])[:1])
            f_split = str(float(neighbour.f_cost)).split('.')
            f_value = '%d.%s' % (int(f_split[0]), str(f_split[1])[:1])
            self.matrix[neighbour.location_x][neighbour.location_y].cost = '{} {}\n{}'.format(
                g_value, h_value, f_value)
        else:  # Do round
            g_split = str(float(neighbour.g_cost)).split('.')
            # Rounds integer to 2sf and rounds decimal to 1sf then joins
            g_value = '%2d.%s' % (int(g_split[0]), str(round(float(
                g_split[1]), -(len(str(g_split[1])) - 1)))[:1])
            h_split = str(float(neighbour.h_cost)).split('.')
            h_value = '%2d.%s' % (int(h_split[0]), str(round(float(
                h_split[1]), -(len(str(h_split[1])) - 1)))[:1])
            f_split = str(float(neighbour.f_cost)).split('.')
            f_value = '%d.%s' % (int(f_split[0]), str(round(float(
                f_split[1]), -(len(str(f_split[1])) - 1)))[:1])
            self.matrix[neighbour.location_x][neighbour.location_y].cost = '{} {}\n{}'.format(
                g_value, h_value, f_value)

    def display_on_grid(self):
        # Printing grid for analysis
        # for row in self.matrix:
        #    for i in range(len(row)):
        #        print(row[i].value),

        # Running external update function for grid values
        a_star_grid_store.update_grid(self.final_path, self.path_nodes, self.start_x, self.start_y, self.end_x,
                                      self.end_y)
        self.output_data()

    def output_data(self):
        # Ending loop once all nodes have been evaluated or end has been reached
        if [self.current.location_x, self.current.location_y] == self.end_node:
            # Creating final path
            temp_node = self.current
            self.final_path.append(temp_node)
            # Stop when start node is reached
            while temp_node.came_from:
                self.final_path.append(temp_node.came_from)
                temp_node = temp_node.came_from
            # print('Done')  # End reached
            self.path = 'Done'
        elif len(self.open_set) <= 0:  # If all nodes have been evaluated and end has not been reached; no solution
            self.path = 'No solution'
        else:
            self.calculate_cost()  # If none of the conditions have been met then run function again until they are


class Check:
    def __init__(self):
        # Calling A* adjacency matrix from file
        matrix = a_star_grid_store.Grid().matrix

        # Setting start and end point from grid
        start_count = 0  # Counting number of start nodes
        end_count = 0  # Counting number of end nodes
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col].value == 2:
                    start_count += 1
                elif matrix[row][col].value == 3:
                    end_count += 1
        # If there are the same amount of nodes that aren't a start or end node as there are total nodes then don't run
        normal_nodes = (len(matrix[row]) * len(matrix[col])) - (start_count + end_count)
        if normal_nodes >= (len(matrix[row]) * len(matrix[col])) - 1:
            self.path = 'Start or end node missing!'
        # More than one start or end node present
        elif start_count > 1 or end_count > 1:
            self.path = 'Duplicate start or end nodes!'
        else:
            # Otherwise run the algorithm from the main GUI file
            self.path = 'Running'
