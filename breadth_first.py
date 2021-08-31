from queue import *


class BreadthFirst:
    def __init__(self, a, start_input, manual_mode):
        # Building a 2D array to store all of the arc lengths (connections) between nodes on grid
        # Reading matrix values from file
        with open('matrix_values.txt') as f:
            # first_line = [int(x) for x in next(f).split()]  # Reading first line
            self.matrix = []
            for line in f:  # Reading rest of lines
                if '/' not in line:
                    self.matrix.append([int(x) for x in line.split()])  # Append rows to matrix

        # Creating the queue
        self.queue = Queue()
        # Variables
        self.manual_mode = manual_mode.get()  # Choice of manual mode or automatic mode
        self.node_input = start_input  # Inheriting node input value from GUI file
        self.visited = []  # Creating visited list to prevent nodes being revisited
        self.path = []  # Nodes will be added to this list to create the final path
        self.frontier_nodes = []  # List of nodes in frontier
        self.current = None  # Creating variable for current node
        self.output_node = None  # Value to be displayed on GUI
        self.total_distance = 0  # Total distance travelled

        # Instructions for manual mode
        self.manual_instruction_1 = None
        self.manual_instruction_2 = None
        self.manual_instruction_3 = None
        self.manual_instruction_4 = None

        # Converting the string input to it's ordinal place in alphabet -97 [a = 0 etc]
        start_node = ord(self.node_input)-97

        self.queue.put(start_node)  # Adding start node to the queue
        self.path.append(self.node_input)  # Adding first node to the path (using node input as it is a char not int)
        self.visited.append(start_node)  # Setting first node as visited

        self.manual_instruction_1 = "Push start node to queue"

        # Only run this in automatic mode
        if self.manual_mode == 0:
            # Runs the search function
            self.breadth_first()
            # Calculating values to be output to GUI
            self.output()

    def get_step(self):
        return self.manual_instruction_1, self.manual_instruction_2, self.manual_instruction_3, self.manual_instruction_4

    def manual_solve(self):
        self.breadth_first()
        return self.path

    def breadth_first(self):
        # UPDATE CURRENT
        self.current = self.queue.get()  # Setting current node as first out of queue

        # Frontier list for displaying in manual mode as different colour
        self.frontier_nodes = []  # Resets each time

        self.manual_instruction_1 = "Push connected nodes to queue (in orange)"

        neighbour_pos = 0
        # Checks for neighbouring nodes
        for _ in self.matrix[self.current]:
            # Checks for existing neighbour and if it is unvisited
            if self.matrix[self.current][neighbour_pos] >= 1 and neighbour_pos not in self.visited:
                # Adding the neighbour node to queue
                self.queue.put(neighbour_pos)
                # Setting the connected neighbour as visited
                self.visited.append(neighbour_pos)
                # Adding current nodes to frontier
                self.frontier_nodes.append(chr(neighbour_pos+97))
                # Adding the connected neighbour to final path
                self.path.append(chr(neighbour_pos+97))

            neighbour_pos += 1  # Moving to next node in array

        queue_contents = []
        for item in list(self.queue.queue):
            queue_contents.append(chr(item+97))
        self.manual_instruction_2 = "Updated queue contents: {}".format(queue_contents)

        self.manual_instruction_3 = "Mark nodes as visited and make the first node in the queue ({}),\n" \
                                    "the new current node and remove it from queue".format(queue_contents[0])

        # Only run in automatic mode
        if self.manual_mode == 0:
            # Only loops the function when queue is not empty [terminates when queue is empty]
            if not self.queue.empty():
                self.breadth_first()

    def output(self):
        self.total_distance = 0
        for row in self.matrix:
            for node in row:
                self.total_distance += node
        # Removing the duplicates
        self.total_distance /= 2
        return self.total_distance


def main():
    BreadthFirst()


if __name__ == '__main__':
    main()
