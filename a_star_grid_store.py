# Class for the nodes to be stored on the grid
class NodeOnGrid:
    def __init__(self, value, cost):
        self.value = value
        self.cost = cost


# Class for the grid
class Grid:
    def __init__(self):
        # Defining the adjacency matrix externally for multiple files to access
        # Individual node objects are easily accessed and updated
        matrix = [[node00, node01, node02, node03, node04, node05, node06, node07],
                  [node10, node11, node12, node13, node14, node15, node16, node17],
                  [node20, node21, node22, node23, node24, node25, node26, node27],
                  [node30, node31, node32, node33, node34, node35, node36, node37],
                  [node40, node41, node42, node43, node44, node45, node46, node47],
                  [node50, node51, node52, node53, node54, node55, node56, node57],
                  [node60, node61, node62, node63, node64, node65, node66, node67],
                  [node70, node71, node72, node73, node74, node75, node76, node77]]
        self.matrix = matrix


def update_grid(final_path, path_nodes, start_x, start_y, end_x, end_y):
    # Changing start and end node back to original colours
    for Node in path_nodes:
        if Node.location_x == start_x and Node.location_y == start_y:
            Grid().matrix[Node.location_x][Node.location_y].value = 2
        elif Node.location_x == end_x and Node.location_y == end_y:
            Grid().matrix[Node.location_x][Node.location_y].value = 3
        # Final path of node locations to have unique colour
        else:
            Grid().matrix[Node.location_x][Node.location_y].value = 4
    # Overriding explored nodes if they are in final path
    for Node in final_path:
        if Node.location_x == start_x and Node.location_y == start_y:
            Grid().matrix[Node.location_x][Node.location_y].value = 2
        elif Node.location_x == end_x and Node.location_y == end_y:
            Grid().matrix[Node.location_x][Node.location_y].value = 3
        # Final path of node locations to have unique colour
        else:
            Grid().matrix[Node.location_x][Node.location_y].value = 5


def refresh_grid():
    # Clearing old explored nodes and path from grid
    row_no = 0
    col_no = 0
    for row in Grid().matrix:
        for col in row:
            cell_contents = Grid().matrix[row_no][col_no].value
            # If node is part of previously explored path
            if cell_contents == 4 or cell_contents == 5 or cell_contents == 9:
                Grid().matrix[row_no][col_no].value = 0
            if cell_contents == 2 or cell_contents == 3:
                Grid().matrix[row_no][col_no].cost = '11.1+11.1\n11.1'
            col_no += 1
            col_no = col_no % 8  # Max col no = 6
        row_no += 1


def reset_grid():
    # Changing value of each node at co-ordinate to 0
    row_no = 0
    col_no = 0
    for row in Grid().matrix:
        for col in row:
            Grid().matrix[row_no][col_no].value = 0
            col_no += 1
            col_no = col_no % 8  # Max col no = 6
        row_no += 1


# Instantiating nodes with value 0 and starting cost of '11.1+11.1\n11.1' for better formatting
node00 = NodeOnGrid(0, '11.1+11.1\n11.1')
node01 = NodeOnGrid(0, '11.1+11.1\n11.1')
node02 = NodeOnGrid(0, '11.1+11.1\n11.1')
node03 = NodeOnGrid(0, '11.1+11.1\n11.1')
node04 = NodeOnGrid(0, '11.1+11.1\n11.1')
node05 = NodeOnGrid(0, '11.1+11.1\n11.1')
node06 = NodeOnGrid(0, '11.1+11.1\n11.1')
node07 = NodeOnGrid(0, '11.1+11.1\n11.1')

node10 = NodeOnGrid(0, '11.1+11.1\n11.1')
node11 = NodeOnGrid(0, '11.1+11.1\n11.1')
node12 = NodeOnGrid(0, '11.1+11.1\n11.1')
node13 = NodeOnGrid(0, '11.1+11.1\n11.1')
node14 = NodeOnGrid(0, '11.1+11.1\n11.1')
node15 = NodeOnGrid(0, '11.1+11.1\n11.1')
node16 = NodeOnGrid(0, '11.1+11.1\n11.1')
node17 = NodeOnGrid(0, '11.1+11.1\n11.1')

node20 = NodeOnGrid(0, '11.1+11.1\n11.1')
node21 = NodeOnGrid(0, '11.1+11.1\n11.1')
node22 = NodeOnGrid(0, '11.1+11.1\n11.1')
node23 = NodeOnGrid(0, '11.1+11.1\n11.1')
node24 = NodeOnGrid(0, '11.1+11.1\n11.1')
node25 = NodeOnGrid(0, '11.1+11.1\n11.1')
node26 = NodeOnGrid(0, '11.1+11.1\n11.1')
node27 = NodeOnGrid(0, '11.1+11.1\n11.1')

node30 = NodeOnGrid(0, '11.1+11.1\n11.1')
node31 = NodeOnGrid(0, '11.1+11.1\n11.1')
node32 = NodeOnGrid(0, '11.1+11.1\n11.1')
node33 = NodeOnGrid(0, '11.1+11.1\n11.1')
node34 = NodeOnGrid(0, '11.1+11.1\n11.1')
node35 = NodeOnGrid(0, '11.1+11.1\n11.1')
node36 = NodeOnGrid(0, '11.1+11.1\n11.1')
node37 = NodeOnGrid(0, '11.1+11.1\n11.1')

node40 = NodeOnGrid(0, '11.1+11.1\n11.1')
node41 = NodeOnGrid(0, '11.1+11.1\n11.1')
node42 = NodeOnGrid(0, '11.1+11.1\n11.1')
node43 = NodeOnGrid(0, '11.1+11.1\n11.1')
node44 = NodeOnGrid(0, '11.1+11.1\n11.1')
node45 = NodeOnGrid(0, '11.1+11.1\n11.1')
node46 = NodeOnGrid(0, '11.1+11.1\n11.1')
node47 = NodeOnGrid(0, '11.1+11.1\n11.1')

node50 = NodeOnGrid(0, '11.1+11.1\n11.1')
node51 = NodeOnGrid(0, '11.1+11.1\n11.1')
node52 = NodeOnGrid(0, '11.1+11.1\n11.1')
node53 = NodeOnGrid(0, '11.1+11.1\n11.1')
node54 = NodeOnGrid(0, '11.1+11.1\n11.1')
node55 = NodeOnGrid(0, '11.1+11.1\n11.1')
node56 = NodeOnGrid(0, '11.1+11.1\n11.1')
node57 = NodeOnGrid(0, '11.1+11.1\n11.1')

node60 = NodeOnGrid(0, '11.1+11.1\n11.1')
node61 = NodeOnGrid(0, '11.1+11.1\n11.1')
node62 = NodeOnGrid(0, '11.1+11.1\n11.1')
node63 = NodeOnGrid(0, '11.1+11.1\n11.1')
node64 = NodeOnGrid(0, '11.1+11.1\n11.1')
node65 = NodeOnGrid(0, '11.1+11.1\n11.1')
node66 = NodeOnGrid(0, '11.1+11.1\n11.1')
node67 = NodeOnGrid(0, '11.1+11.1\n11.1')

node70 = NodeOnGrid(0, '11.1+11.1\n11.1')
node71 = NodeOnGrid(0, '11.1+11.1\n11.1')
node72 = NodeOnGrid(0, '11.1+11.1\n11.1')
node73 = NodeOnGrid(0, '11.1+11.1\n11.1')
node74 = NodeOnGrid(0, '11.1+11.1\n11.1')
node75 = NodeOnGrid(0, '11.1+11.1\n11.1')
node76 = NodeOnGrid(0, '11.1+11.1\n11.1')
node77 = NodeOnGrid(0, '11.1+11.1\n11.1')
