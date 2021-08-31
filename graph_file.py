import networkx as nx


class Graph:
    def __init__(self):
        # Creating a network x graph
        self.g = nx.Graph()

        # READING MATRIX FROM FILE

        # Reading matrix values from file
        with open('matrix_values.txt') as f:
            # first_line = [int(x) for x in next(f).split()]  # Reading first line
            self.matrix = []
            for line in f:  # Reading rest of lines
                if '/' not in line:
                    self.matrix.append([int(x) for x in line.split()])  # Append rows to matrix

        # CREATING GRAPH FROM VALUES

        # Setting row and column no to 0
        row_no = 0
        col_no = 0
        # co-ordinates in matrix [x][y] must have an arc length of 1 or more (to be connected to each other)
        for row in self.matrix:
            # Creating and adding nodes to graph from number of rows in file
            self.g.add_node(chr(row_no + 97))
            for node_value in row:  # Iterating through matrix row of current node
                if node_value >= 1:  # If nodes are connected
                    # Creating edges between nodes with node names as the chr(position) from matrix and weight = value
                    self.g.add_edge(chr(row_no + 97), chr(col_no + 97), weight=node_value)
                col_no += 1
                col_no %= len(row)  # Making sure col_no resets at end of each row
            row_no += 1

        # Largest character to be used for input validation in GUI file
        self.largest_character = chr(row_no + 96)  # 96 instead of 97 as row count increases by 1 too many

        # print(dijkstra_path_length(g, 'A', 'G'))
