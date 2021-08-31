from queue import *  # Importing the Queue data structure
from nodes import Node  # Importing Node class from file


class Dijkstra:
    def __init__(self, a, start_input, end_input, manual_mode):
        self.start = int(ord(start_input)-97)  # Retrieving input from GUI and converting it to an int
        # Conversion is automatic so a human doesn't have to if they want to change this
        self.end = int(ord(end_input)-97)
        self.frontier = PriorityQueue()  # Frontier is added to priority queue (shortest arc length first)

        self.open_set = []  # List of nodes yet to be explored
        self.visited = []  # For final path output
        self.open_neighbour_names = []
        self.closed_set = []  # Nodes that have been assigned working values
        self.came_from = self.start  # came_from is defined as prev node so that current nodes know where they came from
        self.path = []  # Creating the final path
        self.traversal_path = []  # List of nodes that have been evaluated in order
        self.total_length = 0  # Total length of path
        self.matrix = []  # Creating adjacency matrix for reading arc lengths from file
        self.manual_mode = manual_mode.get()  # Either run automatically or use manual stepping
        self.manual_instruction_1 = None  # The current instruction for manual mode
        self.manual_instruction_2 = None
        self.manual_instruction_3 = None
        self.manual_instruction_4 = None

        # Setting start node's attributes (name, working_val, permanent_val, came_from)
        self.current = Node(self.start, 0, 0, self.start)
        # Setting current instruction
        self.manual_instruction_1 = 'Set start node as current\nCreate working values for all neighbours'

        # Running functions
        self.build_matrix()
        self.create_sets()
        # Auto run function if manual is off
        if self.manual_mode == 0:
            self.solve()
        else:
            pass

    def get_step(self):
        return self.manual_instruction_1, self.manual_instruction_2, self.manual_instruction_3, self.manual_instruction_4

    def build_matrix(self):
        # Building a 2D array to store all of the arc lengths (connections) between nodes on grid
        # Reading matrix values from file
        with open('matrix_values.txt') as f:
            # first_line = [int(x) for x in next(f).split()]  # Reading first line
            self.matrix = []
            for line in f:  # Reading rest of lines
                if '/' not in line:
                    # Append rows to matrix as list of objects
                    self.matrix.append([Node(0, int(x), 0, None) for x in line.split()])

    def create_sets(self):
        # Creating open set
        node_name = 0
        for node in self.matrix[0]:  # For each neighbour of current (start) node
            node.name = node_name
            node.working_val = 10000
            self.open_set.append(node)  # Add nodes to open set
            node_name += 1
        # Removing current from open_set
        for node in self.open_set:
            if node.name == self.current.name:
                self.open_set.remove(node)
        # Add start node to closed set
        self.closed_set.append(self.current)
        # Naming the nodes
        for row in self.matrix:
            node_name = 0
            for node in row:  # For each neighbour of current (start) node
                node.name = node_name
                if node.name != self.start:
                    node.working_val = 10000
                else:
                    node.working_val = 0
                node_name += 1

    def manual_solve(self):
        self.solve()
        # Stops function form looping when end is reached
        if self.current.name == self.end:  # If end reached then output
            if self.path != 'FAILED: Dead End':
                self.create_path(self.current.name)  # Runs output function
                self.traversal_path = self.create_traversal_path()
                return self.traversal_path
            else:
                return self.path
        else:  # Otherwise output path so far
            self.traversal_path = self.create_traversal_path()
            return self.traversal_path

    def solve(self):
        # Searching columns that correspond to neighbours of the row_no that represents the current node
        neighbour_node = 0
        # Resetting values
        working_list = []
        frontier_list = []
        old_working_list = []
        updated_nodes = []
        not_updated_nodes = []
        # to find out if they are connected
        for main_node in self.matrix[self.current.name]:  # Iterating through matrix row of current node
            # co-ordinates in matrix [x][y] must have an arc length of 1 or more (to be connected to each other)
            if main_node.distance >= 1:  # if nodes are connected
                # Getting neighbour names from open_set
                self.open_neighbour_names = []
                for node in self.open_set:
                    self.open_neighbour_names.append(node.name)
                # ---
                if neighbour_node in self.open_neighbour_names:
                    # Calculating working val (current value + it's distance from current node)
                    working_value = self.current.working_val + main_node.distance
                    # Getting neighbour from open_set
                    for node in self.open_set:
                        if node.name == neighbour_node:
                            previous_working_value = node.working_val
                            # print previous_working_value
                # ---
                    # Adding each node with values to corresponding list for display in manual mode
                    working_list.append(str(working_value))
                    frontier_list.append(chr(main_node.name+97).upper())
                    old_working_list.append(str(previous_working_value))
                    # Displaying manual instruction
                    if len(working_list) == 1:
                        self.manual_instruction_1 = "Calculate working values for nodes connected to current ({}):\n" \
                                                    "{} is {}'s new value,\n with {} as it's previously calculated" \
                                                    " value".format(chr(self.current.name+97).upper(),
                                                                   (', '.join(working_list)), (', '.join(frontier_list)),
                                                                   (', '.join(old_working_list)))
                    else:
                        self.manual_instruction_1 = "Calculate working values for nodes connected to current ({}):\n" \
                                                    "{} are {}'s new values,\n with {} as their previously calculated" \
                                                    " values".format(chr(self.current.name+97).upper(),
                                                                   (', '.join(working_list)), (', '.join(frontier_list)),
                                                                   (', '.join(old_working_list)))

                    # If this is less then the node's existing working val
                    if working_value < previous_working_value:
                        updated_nodes.append(chr(main_node.name+97).upper())
                        # Display manual instruction
                        if len(working_list) == 1:
                            self.manual_instruction_2 = "The new working value for {} is less so can be updated"\
                                .format(', '.join(updated_nodes))
                        else:
                            self.manual_instruction_2 = "The new working values for {} are less so can be updated"\
                                .format(', '.join(updated_nodes))
                        # Set the new working val for neighbour in open_set
                        for node in self.open_set:
                            if node.name == neighbour_node:
                                node.working_val = working_value
                                # Setting on graph as well #
                                row_no = 0
                                for row in self.matrix:
                                    self.matrix[row_no][neighbour_node].working_val = working_value
                                    row_no += 1
                    else:
                        not_updated_nodes.append(chr(main_node.name + 97).upper())
                        # Display manual instruction
                        if len(working_list) == 1:
                            self.manual_instruction_2 = "The new working value for {} is greater so won't be updated" \
                                .format(', '.join(not_updated_nodes))
                        else:
                            self.manual_instruction_2 = "The new working values for {} are greater so won't be updated" \
                                .format(', '.join(not_updated_nodes))

                    # Adding neighbour to queue
                    for node in self.open_set:
                        if node.name == neighbour_node:  # Only if in open set
                            # print(node.working_val, chr(neighbour_node + 97), 'added to queue')
                            self.frontier.put((node.working_val, chr(neighbour_node + 97)))
            # Next neighbour
            neighbour_node += 1

        # Dead end reached
        if self.frontier.empty():
            if self.current.name != self.end:
                # RETURN TO PREVIOUS NODE IN CLOSED SET #
                # came_from is the node that are currently on, before setting new current below
                came_from = self.current
                # Set previous in closed_set as new current
                self.current = self.closed_set[-2]  # -2 so that it doesnt repeat the last node
                self.current.came_from = came_from  # Set it's came_from node
                self.closed_set.remove(self.closed_set[-1])
        else:
            # Setting new node's came_from to the current node
            came_from = self.current
            # came_from is the neighbour with the lowest permanent value

            # Setting new current node based of lowest in queue
            current = self.frontier.get()
            # Splitting the node name and arc number
            for i in current:
                try:
                    str(i)  # Only using CHARACTER from tuple of current node as current name
                    current = i  # Setting top of frontier priority queue to CURRENT node name
                except ValueError:
                    pass
                try:
                    int(i)  # Setting only NUMBER of current node as working_value
                    working_value = i
                except ValueError:
                    pass

            # Setting new current node
            self.current = Node(ord(current) - 97, 0, working_value, came_from)

            # Display manual instructions
            self.manual_instruction_3 = "{} has been selected as the lowest cost unexplored node ({}),\n" \
                                        "it's working value will be changed to it's permanent value"\
                .format(chr(self.current.name+97).upper(), self.current.working_val)

            self.manual_instruction_4 = "- {} is now the current node to be explored from -".format(
                chr(self.current.name + 97).upper())

            # Clears old items from the priority queue
            while not self.frontier.empty():
                self.frontier.get()

            # Removing current from open_set, and adding to closed set
            for node in self.open_set:
                if node.name == self.current.name:
                    self.open_set.remove(node)
                    # Appending node to closed set, if it's not already
                    if node not in self.closed_set:
                        self.closed_set.append(node)

        # if automatic mode
        if self.manual_mode == 0:
            # Stops function form looping when end is reached
            if self.current.name != self.end:  # If end not reached, restart function
                # print 'running again'
                self.solve()
            else:  # If end reached (output values)
                if self.path != 'FAILED: Dead End':
                    self.create_path(self.current.name)  # Runs output function

    def create_path(self, current_node):
        # Creating priority queue for lowest cost previous node
        lowest_cost_neighbour = PriorityQueue()
        ## print('\n'.join(['   '.join(['{:4}'.format(item.working_val) for item in row]) for row in self.matrix]))
        # Adding nodes to final path
        self.path.append(chr(current_node + 97))
        # For each node connected to the current (last node in path)
        for node in self.matrix[current_node]:
            if node.distance >= 1:
                ## print [node.working_val + node.distance, chr(node.name + 97)]
                # Adding nodes to queue (adding the distance from node to total cost value)
                lowest_cost_neighbour.put([node.working_val + node.distance, chr(node.name + 97)])

        # Getting neighbour with lowest total cost from start
        current = lowest_cost_neighbour.get()
        for i in current:
            try:
                str(i)  # Only using CHARACTER from tuple of current node as current name
                current = i  # Setting top of frontier priority queue to CURRENT node name
            except ValueError:
                pass

        # Adding arc length between nodes to final path length
        self.total_length += self.matrix[current_node][ord(current) - 97].distance

        # If the start is reached again then end the loop
        if ord(current) - 97 == self.start:
            self.path.append(current)  # Adding final node to path
            self.path.reverse()
            self.create_traversal_path()
        else:
            # Run again
            self.create_path(ord(current) - 97)

        # if isinstance(temp_node.came_from, types.ClassType):  # Checking if object

    def create_traversal_path(self):
        self.traversal_path = []  # resetting path
        # All node that have been
        temp_node = self.current
        self.traversal_path.append(chr(temp_node.name + 97))
        # Stop when start node is reached
        while not isinstance(temp_node.came_from, int):  # Checking if object
            self.traversal_path.append(chr(temp_node.came_from.name + 97))
            temp_node = temp_node.came_from
        self.traversal_path.reverse()
        if self.manual_mode == 1:
            return self.traversal_path


def main():
    Dijkstra()


if __name__ == '__main__':
    main()
