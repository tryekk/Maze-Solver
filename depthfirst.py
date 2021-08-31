import stack_class


class DepthFirst:
    def __init__(self, a, start_input, manual_mode):
        # Building a 2D array to store all of the arc lengths (connections) between nodes on grid
        # Reading matrix values from file
        with open('matrix_values.txt') as f:
            # first_line = [int(x) for x in next(f).split()]  # Reading first line
            self.matrix = []
            for line in f:  # Reading rest of lines
                if '/' not in line:
                    self.matrix.append([int(x) for x in line.split()])  # Append rows to matrix

        # Making stack object from stack_class.py file
        self.stack = stack_class.Stack()

        self.node_input = start_input  # Taking node input value from GUI file through association
        self.manual_mode = manual_mode.get()  # Choice of manual mode or not

        self.visited = []  # Creating visited list to prevent nodes being revisited
        self.path = []  # Nodes will be added to this list to create the final path
        self.current = None  # Creating variable for current node
        self.output_node = None  # Value to be displayed on GUI
        self.total_distance = 0  # Total distance travelled
        self.backtracking = False  # Has dead end been reached

        # Instructions for manual mode
        self.manual_instruction_1 = None
        self.manual_instruction_2 = None
        self.manual_instruction_3 = None
        self.manual_instruction_4 = None

        # Converting the string input to it's ordinal place in alphabet -97 [a = 0 etc]
        start_node = ord(self.node_input)-97

        self.stack.push(start_node)  # Adding start node to stack

        self.manual_instruction_1 = "Set start node to stack and mark as visited"

        # Only run this in automatic mode
        if self.manual_mode == 0:
            # Runs the search function
            self.depth_first()
            # Calculating values to be output to GUI
            self.output()

    def get_step(self):
        return self.manual_instruction_1, self.manual_instruction_2, self.manual_instruction_3, self.manual_instruction_4

    def manual_solve(self):
        self.depth_first()
        return self.path

    def depth_first(self):
        # UPDATE CURRENT
        self.current = self.stack.stack_items[-1]  # Setting current node as first out of stack
        if self.current not in self.visited:  # Will only add to path if node has not already been visited
            # print(chr(self.current + 97))  # Outputting the current node
            self.path.append(chr(self.current + 97))  # Adding current node to path list
            # self.output_node = chr(self.current + 97)
        self.visited.append(self.current)  # Setting current node as visited, so it won't be printed again

        if not self.backtracking:
            self.manual_instruction_3 = ""
            self.manual_instruction_4 = ""

        pos = 0
        # Checks for neighbouring nodes
        for node in self.matrix[self.current]:
            # Checks for existing neighbour and if it is unvisited
            if self.matrix[self.current][pos] >= 1 and pos not in self.visited:
                    self.stack.push(pos)  # Adding the neighbour node to stack
                    self.backtracking = False
                    break
            # Backtracking once leaf node is reached until node with unexplored neighbours is found
            elif pos+1 == len(self.matrix[self.current]):  # At end without (elif) having found a neighbour
                self.backtracking = True
                self.manual_instruction_1 = "DEAD END REACHED:"
                self.manual_instruction_3 = "Dead end reached; backtrack until node with\n" \
                                            "unexplored neighbours found"
                self.manual_instruction_4 = "If stack is emptied without finding unexplored nodes,\n" \
                                            "traversal is complete"
                self.stack.pop()  # Drop back
            pos += 1  # Moving to next node in array
            # Otherwise loop and promote neighbour to current

        # Translate stack items for display
        translated_items = []
        for item in self.stack.stack_items:
            translated_items.append(chr(item+97))
        self.manual_instruction_2 = "Updated stack contents: {}".format(translated_items)
        # Shows next neighbour in manual display
        if not self.backtracking:
            self.manual_instruction_1 = "Choose {}'s first connected node alphabetically ({}), push it to stack\n" \
                                        "and mark as visited".format(chr(self.current+97),
                                                                     chr(self.stack.stack_items[-1] + 97))

        # Only run again in automatic mode
        if self.manual_mode == 0:
            # Only loops the function when stack is not empty [terminates when stack is empty]
            if not self.stack.is_empty:
                self.depth_first()

    def output(self):
        self.total_distance = 0
        for row in self.matrix:
            for node in row:
                self.total_distance += node
        # Removing the duplicates
        self.total_distance /= 2
        return self.total_distance


def main():
    DepthFirst()


if __name__ == '__main__':
    main()
