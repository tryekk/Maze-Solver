# coding:utf-8
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib
import networkx as nx
import time
import re

import graph_file
import a_star_grid
import a_star_grid_store
import depthfirst
import breadth_first
import dijkstra_oop
import a_algorithm
import instruction_window
# from testing import graph_input

matplotlib.use('TkAgg')


class Gui:
    def __init__(self, master):
        # Drawing window and setting title
        master.wm_title("Path-Finder")
        master.geometry('700x700+100+50')
        self.master = master

        # FRAMES
        # Creating main frame
        mainframe = Frame(self.master)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        mainframe.grid(column=0, row=0)
        self.label = Label(mainframe, text="Path-Finder", font=('Helvetica', 25, 'bold'))
        self.label.grid(column=1, row=0, pady=8)

        # Help button
        self.frame_subhead = Frame(mainframe)
        self.frame_subhead.grid(column=1, row=2)
        self.help_button = Button(mainframe, text="HELP", font=('Helvetica', 12, 'bold'), command=self.display_help)
        self.help_button.grid(column=1, row=2, pady=6)
        # Set parameters
        self.frame2 = Frame(mainframe)
        self.frame2.grid(column=1, row=3)
        # Enter start and end
        self.frame3 = Frame(mainframe)
        self.frame3.grid(column=1, row=4)
        # Buttons
        self.frame4 = Frame(mainframe)
        self.frame4.grid(column=1, row=5)
        # Path output
        self.frame5 = Frame(mainframe)
        self.frame5.grid(column=1, row=6)
        # Totals
        self.frame6 = Frame(mainframe)
        self.frame6.grid(column=1, row=7)

        # LEFT
        self.frame_left = Frame(self.frame6)
        self.frame_left.grid(column=0, row=5, padx=10)
        # CENTRE
        self.frame_centre = Frame(self.frame6)
        self.frame_centre.grid(column=1, row=5, padx=10)
        # RIGHT
        self.frame_right = Frame(self.frame6)
        self.frame_right.grid(column=2, row=5, padx=10)

        # WIDGETS
        # Setting variables
        self.output = None
        self.grid_view = False
        self.a_star_window = None
        self.start_input = StringVar()  # Defining start node
        self.end_input = StringVar()  # Defining end node
        self.choice = IntVar()  # Choice of algorithm
        self.heuristic_choice = IntVar()  # Choice of heuristic for A*
        self.diagonal_enabled = IntVar()  # Choice of diagonals for A*
        self.display_costs = IntVar()  # Display costs for A*
        self.a_star_grid_top = None  # Top level widget for A* grid
        self.manual_mode = IntVar()  # Option for manual stepping mode
        self.next_step = False  # If next step is true for manual mode
        self.grid_open = False  # Is grid top-level window running
        self.character = graph_file.Graph().largest_character  # Amount of nodes
        self.path = []  # Path for traversal algorithms
        self.total_distance = 0  # Distance for traversal algorithms
        self.step_number = 1  # Step number for manual mode
        self.traversal_path = []  # Traversal path for graph algorithms
        self.instruction_window = None  # Instruction window instance
        self.instruction_window_open = False  # Is window open
        # Creating the variables that will contain the final values
        self.output_value = StringVar()
        self.number_nodes_explored = StringVar()
        self.number_nodes_explored.set('Nodes: 0')
        self.output_value_2 = StringVar()
        self.output_value_2.set('Length: 0')
        self.output_value_3 = StringVar()
        self.total_time = StringVar()
        self.total_time.set('Time taken: 0µs')
        # Creating variables for time calculation
        self.start_time = 0
        self.end_time = 0

        # CREATING THE LABELS
        # OUTPUTS
        self.path_output = Label(self.frame4, text='Traversal / Path:', font=('Helvetica', 17))
        self.path_output.grid(column=1, row=1)
        self.path_output = Label(self.frame5, textvariable=self.output_value, font=('Helvetica', 20, 'bold'))
        self.path_output.grid(column=1, row=1)
        self.dijkstra_traversal_output = Label(self.frame5, textvariable=self.output_value_3, font=('Helvetica', 20))
        self.dijkstra_traversal_output.grid(column=1, row=2)
        # TOTALS
        self.total_nodes_explored = Label(self.frame_left, textvariable=self.number_nodes_explored,
                                          font=('Helvetica', 16))
        self.total_nodes_explored.grid(column=0, row=0)
        self.path_length = Label(self.frame_centre, textvariable=self.output_value_2,
                                 font=('Helvetica', 16))
        self.path_length.grid(column=0, row=0)
        self.time_taken = Label(self.frame_right, textvariable=self.total_time,
                                font=('Helvetica', 16))
        self.time_taken.grid(column=0, row=0)

        # USER INTERACTION
        # CHOICE OF ALGORITHM
        self.label = Label(self.frame2, text="Select\nAlgorithm", font=('Helvetica', 16, 'bold'))
        self.label.config(width=12)
        self.label.grid(column=0, row=2, pady=5)
        # Creating the radio button to choose algorithm
        # Setting the current selection to none of the algorithms
        self.choice.set(4)
        Radiobutton(self.frame2, text='Depth-First', font=('Helvetica', 13), variable=self.choice, value=0,
                    command=self.draw).grid(row=3, column=0, padx=20)
        Radiobutton(self.frame2, text='Breadth-First', font=('Helvetica', 13), variable=self.choice, value=1,
                    command=self.draw).grid(row=4, column=0, padx=20)
        Radiobutton(self.frame2, text='Dijkstra', font=('Helvetica', 13), variable=self.choice, value=2,
                    command=self.draw).grid(row=5, column=0, padx=20)
        Radiobutton(self.frame2, text='A*', font=('Helvetica', 13), variable=self.choice, value=3,
                    command=self.draw).grid(row=6, column=0, padx=20)

        # CHOICE OF HEURISTIC
        self.label = Label(self.frame2, text="Select\nHeuristic", font=('Helvetica', 16, 'bold'))
        self.label.config(width=12)
        self.label.grid(column=1, row=2, pady=5)
        # Creating the radio button to choose heuristic
        # Setting default to manhattan
        self.choice.set(0)
        Radiobutton(self.frame2, text='Manhattan', font=('Helvetica', 13), variable=self.heuristic_choice, value=0)\
            .grid(row=3, column=1, padx=20)
        Radiobutton(self.frame2, text='Euclidean', font=('Helvetica', 13), variable=self.heuristic_choice, value=1)\
            .grid(row=4, column=1, padx=20)
        Radiobutton(self.frame2, text="Tom's Heuristic", font=('Helvetica', 13), variable=self.heuristic_choice, value=2)\
            .grid(row=5, column=1, padx=20)

        # CHOICE OF DIAGONALS
        self.label = Label(self.frame2, text="Choose\nDiagonals", font=('Helvetica', 16, 'bold'))
        self.label.config(width=12)
        self.label.grid(column=2, row=2, pady=5)
        # Creating the radio button to turn diagonals on or off
        # Setting default to off
        self.choice.set(0)
        Radiobutton(self.frame2, text='Off', font=('Helvetica', 13), variable=self.diagonal_enabled, value=0) \
            .grid(row=3, column=2, padx=20)
        Radiobutton(self.frame2, text='On', font=('Helvetica', 13), variable=self.diagonal_enabled, value=1) \
            .grid(row=4, column=2, padx=20)

        # DISPLAY COSTS
        self.label = Label(self.frame2, text="Display\nCosts", font=('Helvetica', 16, 'bold'))
        self.label.config(width=12)
        self.label.grid(column=3, row=2, pady=5)
        # Creating the radio button to display costs
        # Setting default to off
        self.choice.set(0)
        Radiobutton(self.frame2, text='Off', font=('Helvetica', 13), variable=self.display_costs, value=0) \
            .grid(row=3, column=3, padx=20)
        Radiobutton(self.frame2, text='On', font=('Helvetica', 13), variable=self.display_costs, value=1) \
            .grid(row=4, column=3, padx=20)

        # ENTER START AND END NODE
        self.label = Label(self.frame3, text="Enter start and end node",
                           font=('Helvetica', 17, 'bold'))
        self.label.grid(column=0, row=0, columnspan=2, pady=4, padx=20)
        self.label = Label(self.frame3, text="Not for A* algorithm",
                           font=('Helvetica', 14))
        self.label.grid(column=0, row=1, columnspan=2)
        # Choose auto or manual
        self.label = Label(self.frame3, text="Choose\nMode",
                           font=('Helvetica', 16, 'bold'))
        self.label.grid(column=3, row=0, columnspan=1, padx=20)
        # Creating the radio button to turn diagonals on or off
        # Setting default to automatic
        self.manual_mode.set(0)
        Radiobutton(self.frame3, text='Automatic', font=('Helvetica', 13, 'bold'), command=self.set_manual_button,
                    variable=self.manual_mode, value=0).grid(row=1, column=3, padx=20)
        Radiobutton(self.frame3, text='Manual', font=('Helvetica', 13, 'bold'),
                    variable=self.manual_mode, value=1).grid(row=2, column=3, padx=20)
        # Next step in algorithm (MANUAL)
        self.next_step_button = Button(self.frame3, text='NEXT STEP', font=('Helvetica', 14, 'bold'))
        self.next_step_button.config(width=10, relief=SUNKEN, bg='grey')
        self.next_step_button.grid(row=3, column=3, padx=8, pady=12)

        # Start node
        self.start_node = Label(self.frame3, text='Start Node', font=('Helvetica', 13, 'bold'))
        self.start_node.grid(column=0, row=2, padx=14, pady=6)
        # Start node
        self.end_node = Label(self.frame3, text='End for Dijkstra', font=('Helvetica', 13, 'bold'))
        self.end_node.grid(column=1, row=2, padx=14, pady=6)
        # Taking user input for start node for algorithm
        node_entry_start = Entry(self.frame3, textvariable=self.start_input)
        node_entry_start.grid(column=0, row=3, padx=14, pady=4)
        node_entry_end = Entry(self.frame3, textvariable=self.end_input)
        node_entry_end.grid(column=1, row=3, padx=14, pady=4)

        # RUN algorithm
        # Runs validation function before algorithm
        run_algorithm = Button(self.frame4, text='START', font=('Helvetica', 14, 'bold'), command=self.validate_input)
        run_algorithm.config(width=10)
        run_algorithm.grid(row=0, column=0, padx=8, pady=12)

        # RESET graph or grid display
        reset = Button(self.frame4, text='RESET', font=('Helvetica', 14, 'bold'), command=self.reset_display)
        reset.config(width=10)
        reset.grid(row=0, column=1, padx=8, pady=12)

        # REFRESH graph or grid display
        refresh = Button(self.frame4, text='REFRESH', font=('Helvetica', 14, 'bold'), command=self.refresh_display)
        refresh.config(width=10)
        refresh.grid(row=0, column=2, padx=8, pady=12)

        '''
        # Graph input
        refresh = Button(self.frame4, text='GRAPH', font=('Helvetica', 14, 'bold'), command=self.draw_graph_input)
        refresh.config(width=10)
        refresh.grid(row=0, column=3, padx=8, pady=12)
        '''

    def display_help(self):
        help_top = Toplevel()
        help_top.title("Help")

        # Scroll bar
        scroll_bar = Scrollbar(help_top, orient=VERTICAL)
        scroll_bar.grid(row=0, column=1, sticky="ns")

        # Create canvas
        help_canvas = Canvas(help_top, width=610, height=800, scrollregion=(0, 0, 0, 1400))
        help_canvas.grid(row=0, column=0, sticky="nsew")

        scroll_bar.config(command=help_canvas.yview)
        help_canvas.config(yscrollcommand=scroll_bar.set)

        # Read file
        help_text = open('instructions_internal.txt', 'r+')
        file_contents = help_text.read()
        # Write text
        help_canvas.create_text(300, 680, text=file_contents, font=11)

        help_top.rowconfigure(0, weight=1)
        help_top.columnconfigure(0, weight=1)

    def set_manual_button(self):
        # DISABLING MANUAL NEXT STEP BUTTON
        # Sink button when not in use
        self.next_step_button.config(relief=SUNKEN, bg='grey')
        # Don't allow button to run next step function
        self.next_step_button.config(command=self.set_manual_button)

    def reset_display(self):
        if self.grid_view:
            # Resetting grid
            a_star_grid_store.reset_grid()
            # Updating grid by running function
            self.grid_app.update_grid(self.display_costs.get())
        else:
            # RESET GRAPH
            pass

    def refresh_display(self):
        if self.grid_view:
            # Refreshing grid
            a_star_grid_store.refresh_grid()
            # Updating grid by running function
            self.grid_app.update_grid(self.display_costs.get())

    def draw_graph_input(self):
        # Creating new window
        self.graph_input_top = Toplevel(self.master)
        self.graph_input_app = graph_input.Grid(self.graph_input_top)
        self.graph_input_open = True

    def draw(self):
        plt.close('all')  # Closing all previously opened graphs
        # If grid is open close it
        if self.grid_open:
            self.close_grid()
        # DRAWING GRID OR GRAPH
        # Draw if A* algorithm is selected, otherwise draw graph
        if self.choice.get() == 3:
            self.grid_view = True  # Allowing the program to display differently when grid is used
            # Creating new window
            self.a_star_grid_top = Toplevel(self.master)
            self.grid_app = a_star_grid.Grid(self.a_star_grid_top)
            self.grid_open = True
        elif self.choice.get() == 0 or self.choice.get() == 1 or self.choice.get() == 2:
            self.grid_view = False
            # Setting window position for graph
            manager = plt.get_current_fig_manager()
            manager.window.wm_geometry('700x700+810+50')
            manager.window.title('Path-Finder (Graph view)')
            # Using network x and maptlotlib draw function to show graph
            graph_object = graph_file.Graph()
            # Getting node positions
            pos = nx.circular_layout(graph_object.g)
            nx.draw(graph_object.g, pos, with_labels=True)
            # Displaying weighted edges
            labels = nx.get_edge_attributes(graph_object.g, 'weight')
            nx.draw_networkx_edge_labels(graph_object.g, pos, edge_labels=labels)
            plt.show()

    def close_grid(self):
        self.a_star_grid_top.destroy()
        self.grid_open = False  # Grid is no longer open

    def validate_input(self):
        # Setting valid to false
        start_valid = False
        end_valid = False
        # Setting value of largest character that can be entered based off graph size
        upper_character = self.character.upper()

        # If A* is chosen then validation is done elsewhere
        if self.choice.get() == 3:
            self.run_algorithm()
        # If dijkstra then start and end node need to be validated
        elif self.choice.get() == 2:
            # Validating start node
            start_input = self.start_input.get()
            # Checking there is an entry and if it is too long
            if len(start_input) > 0:
                if len(start_input) > 1:
                    error_message = 0
                else:
                    # Checking is char between a and largest character
                    valid_start_input = re.findall(r'[a-{}A-{}\-]+'.format(self.character, upper_character),
                                                   start_input)
                    if len(valid_start_input) == len(start_input):
                        # All conditions have been passed and entry is valid
                        start_valid = True
                    else:
                        error_message = 2
            else:
                error_message = 3
            # Validating end node
            end_input = self.end_input.get()
            # Checking there is an entry and if it is too long
            if len(end_input) > 0:
                if len(end_input) > 1:
                    error_message = 1
                else:
                    # Checking is char between a and largest character
                    valid_end_input = re.findall(r'[a-{}A-{}\-]+'.format(self.character, upper_character), end_input)
                    if len(valid_end_input) == len(end_input):
                        # All conditions have been passed and entry is valid
                        end_valid = True
                    else:
                        error_message = 2
            else:
                error_message = 3
            # If both nodes are valid then run algorithm
            if start_valid and end_valid:
                self.run_algorithm()
            else:
                self.error_window(error_message, upper_character)
        # Otherwise only start node needs to be evaluated
        else:
            # Validating start node
            start_input = self.start_input.get()
            # Checking there is an entry and if it is too long
            if len(start_input) > 0:
                if len(start_input) > 1:
                    error_message = 0
                else:
                    # Checking is char between a and largest character
                    valid_start_input = re.findall(r'[a-{}A-{}\-]+'.format(self.character, upper_character),
                                                   start_input)
                    if len(valid_start_input) == len(start_input):
                        # All conditions have been passed and entry is valid
                        start_valid = True
                    else:
                        error_message = 2
            else:
                error_message = 4
            # If both nodes are valid then run algorithm
            if start_valid:
                self.run_algorithm()
            else:
                self.error_window(error_message, upper_character)

    def error_window(self, error_message, upper_character):
        error_top = Toplevel()
        error_top.title("Error")
        error_top.geometry('470x150+560+350')
        # Creating label
        self.label = Label(error_top)
        if error_message == 0:
            # Start too long
            self.label.configure(text='Start node too long', font=('Helvetica', 25, 'bold'))
        elif error_message == 1:
            # End too long
            self.label.configure(text='End node too long', font=('Helvetica', 25, 'bold'))
        elif error_message == 2:
            # Invalid start or end node
            self.label.configure(text='Node input needs to be\n'
                                      'between nodes A and {}'.format(upper_character), font=('Helvetica', 18, 'bold'))
        elif error_message == 3:
            # No start node
            self.label.configure(text='Please enter a start\nand end node', font=('Helvetica', 25, 'bold'))
        elif error_message == 4:
            # No start node
            self.label.configure(text='Please enter a start node', font=('Helvetica', 25, 'bold'))
        # Drawing label
        self.label.pack(pady=40)

    def run_algorithm(self):
        # Resetting outputs
        self.output_value.set('--')  # Path
        self.output_value_3.set('--')  # Traversal
        self.output_value_2.set('Length: 0')  # Path length
        self.number_nodes_explored.set('Nodes: 0')  # Nodes
        self.total_time.set('Time taken: --µs')  # Time
        # Closing existing instruction window
        if self.instruction_window_open:
            self.instruction_app.close_window()
        # Creating new window
        if self.manual_mode.get() == 1 and self.choice.get() != 3:  # A* not yet supported!
            self.instruction_top = Toplevel(self.master)
            self.instruction_app = instruction_window.InstructionWindow(self.instruction_top)
        # Running the relevant main function (depending on user choice)
        if self.choice.get() == 0:
            self.depth_first()  # Starts depth first function
        elif self.choice.get() == 1:
            self.breadth_first()  # Starts breadth first function
        elif self.choice.get() == 2:
            self.dijkstra()  # Starts dijkstra function
        elif self.choice.get() == 3:
            if self.manual_mode.get() == 1:  # Disable manual mode for A*
                self.manual_mode.set(0)
            self.a_star_algorithm()  # Starts A* function

    def next_step_manual(self):
        # Now 'next step' mode is true as init function has been run
        self.next_step = True
        # Runs init function
        if self.choice.get() == 0:  # Depth
            self.depth_first()
        elif self.choice.get() == 1:  # Breadth
            self.breadth_first()
        elif self.choice.get() == 2:  # Dijkstra
            self.dijkstra()
        elif self.choice.get() == 3:  # A*
            self.a_star_algorithm()

    def update_graph(self):
        # Setting colours for nodes that are in the path
        visited_node_colours = []
        for node in graph_file.Graph().g:
            if self.choice.get() == 0:
                if node in self.output.path:
                    # Visited nodes
                    visited_node_colours.append('green')
                else:
                    # Unvisited nodes
                    visited_node_colours.append('red')
            elif self.choice.get() == 1:
                # Set path that isn't part of the frontier to green
                if node in self.output.path and node not in self.output.frontier_nodes:
                    # Visited nodes
                    visited_node_colours.append('green')
                # Nodes in frontier
                elif node in self.output.frontier_nodes:
                    visited_node_colours.append('orange')
                else:
                    # Unvisited nodes
                    visited_node_colours.append('red')
            # if dijkstra then look at frontier and unexplored nodes
            elif self.choice.get() == 2:
                if node in self.output.path:
                    # Visited nodes
                    visited_node_colours.append('green')
                # Nodes in frontier
                elif node in self.output.traversal_path:
                    visited_node_colours.append('orange')
                else:
                    # Unvisited nodes
                    visited_node_colours.append('red')

        # UPDATING GRAPH ONCE ALGORITHM HAS BEEN RUN
        # Setting window position for graph
        manager = plt.get_current_fig_manager()
        manager.window.wm_geometry('700x700+810+50')
        manager.window.title('Path-Finder (Graph view)')
        # Using network x and maptlotlib draw function to show graph
        graph_object = graph_file.Graph()
        # Getting node positions
        pos = nx.circular_layout(graph_object.g)
        nx.draw(graph_object.g, pos, node_color=visited_node_colours, with_labels=True)
        # Displaying weighted edges
        labels = nx.get_edge_attributes(graph_object.g, 'weight')
        nx.draw_networkx_edge_labels(graph_object.g, pos, edge_labels=labels)
        plt.show()

    def depth_first(self):
        # IF AUTOMATIC MODE
        if self.manual_mode.get() == 0:
            # Taking current time for duration calculation
            self.start_time = time.time()
            # Running the depth first algorithm from file and passing it the node input (lowercase) from gui from entry
            self.output = depthfirst.DepthFirst(self, self.start_input.get().lower(), self.manual_mode)  # Instance
            self.output_value_2.set('Length: {}'.format(self.output.total_distance))  # Displaying total distance
            # Running the output function
            self.display_values()
        # IF MANUAL MODE
        else:
            # Enabling next step button
            self.next_step_button.config(relief=RAISED, bg='grey94')
            self.next_step_button.config(command=self.next_step_manual)
            # Closing old instruction window
            if not self.next_step:
                self.instruction_window_open = True
                # Running init from file
                self.output = depthfirst.DepthFirst(self, self.start_input.get().lower(), self.manual_mode)
                instruction_1, instruction_2, instruction_3, instruction_4 = self.output.get_step()
                # Displaying step
                self.instruction_app.update_instructions(instruction_1, instruction_2, instruction_3, instruction_4)
                # Display values
                self.display_values()
            else:
                # Now just updates traversal path (no need to re-run init function)
                self.path = self.output.manual_solve()
                self.total_distance = self.output.output()
                # Displaying next step
                instruction_1, instruction_2, instruction_3, instruction_4 = self.output.get_step()
                self.instruction_app.update_instructions(instruction_1, instruction_2, instruction_3, instruction_4)
                # Display values
                self.display_values()

    def breadth_first(self):
        # IF AUTOMATIC MODE
        if self.manual_mode.get() == 0:
            # Taking current time for duration calculation
            self.start_time = time.time()
            # Running file
            self.output = breadth_first.BreadthFirst(self, self.start_input.get().lower(), self.manual_mode)
            self.output_value_2.set('Length: {}'.format(self.output.total_distance))  # Displaying total distance
            self.display_values()
        # IF MANUAL MODE
        else:
            # Enabling next step button
            self.next_step_button.config(relief=RAISED, bg='grey94')
            self.next_step_button.config(command=self.next_step_manual)
            if not self.next_step:
                self.instruction_window_open = True
                # Running init from file
                self.output = breadth_first.BreadthFirst(self, self.start_input.get().lower(), self.manual_mode)
                instruction_1, instruction_2, instruction_3, instruction_4 = self.output.get_step()
                # Displaying step
                self.instruction_app.update_instructions(instruction_1, instruction_2, instruction_3, instruction_4)
                # Display values
                self.display_values()
            else:
                # Now just updates traversal path (no need to re-run init function)
                self.path = self.output.manual_solve()
                self.total_distance = self.output.output()
                instruction_1, instruction_2, instruction_3, instruction_4 = self.output.get_step()
                self.instruction_app.update_instructions(instruction_1, instruction_2, instruction_3, instruction_4)
                # Display values
                self.display_values()

    def dijkstra(self):
        # IF AUTOMATIC MODE
        if self.manual_mode.get() == 0:
            # Taking current time for duration calculation
            self.start_time = time.time()
            # Running file
            self.output = dijkstra_oop.Dijkstra(self, self.start_input.get().lower(), self.end_input.get().lower(),
                                                self.manual_mode)
            # Displaying the path length
            self.output_value_2.set('Length: {}'.format(self.output.total_length))
            self.display_values()
        # IF MANUAL MODE
        else:
            # Enabling next step button
            self.next_step_button.config(relief=RAISED, bg='grey94')
            self.next_step_button.config(command=self.next_step_manual)
            # Resetting step number
            if not self.next_step:
                # Displaying instructions
                self.instruction_window_open = True
                # Running init from file
                self.output = dijkstra_oop.Dijkstra(self, self.start_input.get().lower(), self.end_input.get().lower(),
                                                    self.manual_mode)
                # Displaying next step
                instruction_1, instruction_2, instruction_3, instruction_4 = self.output.get_step()
                self.instruction_app.update_instructions(instruction_1, instruction_2, instruction_3, instruction_4)
                # Outputting values
                self.display_values()
            else:
                # Now just updates traversal path (no need to re-run init function)
                self.traversal_path = self.output.manual_solve()
                # Displaying next step
                instruction_1, instruction_2, instruction_3, instruction_4 = self.output.get_step()
                self.instruction_app.update_instructions(instruction_1, instruction_2, instruction_3, instruction_4)
                # Outputting values
                self.display_values()

    def a_star_algorithm(self):
        # Taking current time for duration calculation
        self.start_time = time.time()
        # Running file
        self.output = a_algorithm.Check()  # Runs check function to make sure there is a start and end
        if self.output.path == 'Running':
            self.output = a_algorithm.Algorithm(self.heuristic_choice.get(), self.diagonal_enabled.get(),
                                                self.a_star_grid_top)
            # Displaying the path length
            if self.output.path != 'No solution':
                self.output_value_2.set('Length: {:.2f}'.format(self.output.current.f_cost))
            else:
                self.output_value_2.set('Length: --')
            # Display values
            self.display_values()
        else:
            self.display_error()

    def display_error(self):
        # Displaying error message
        self.output_value.set(' '.join(self.output.path))

    def display_values(self):
        # AUTOMATIC MODE
        if self.manual_mode.get() == 0:
            # Calculating time taken to complete traversal (µs)
            self.end_time = time.time()
            total_time_taken = (self.end_time - self.start_time)*100000000
            # Message displayed if time taken was less then the interval at which time is sampled
            if total_time_taken == 0:
                self.total_time.set('Time taken: 0µs (< measure freq)')
            else:
                self.total_time.set('Time taken: {:.3f}µs'.format(total_time_taken))

            # Displaying total nodes in path
            if not self.grid_view:
                # Length of path list output
                self.number_nodes_explored.set('Nodes: {}'.format(len(self.output.path)))
            else:
                # Length of the open and closed set combined
                self.number_nodes_explored.set('Nodes: {}/{}'.format(len(self.output.open_set + self.output.closed_set),
                                                                     (64 - self.output.wall_count)))

            # Displaying final path from file
            self.output_value.set(' '.join(self.output.path))
            # Traversal path for Dijkstra
            if self.choice.get() == 2:
                # Printing full traversal path
                self.output_value_3.set(' '.join(self.output.traversal_path))
            else:
                self.output_value_3.set('--')  # Resetting when not in use

            # Update grid or graph
            if not self.grid_view:
                # Updating the graph (runs draw function)
                plt.close('all')  # Closing all previously opened graphs
                self.update_graph()
            else:
                # Updating grid by running function
                self.grid_app.update_grid(self.display_costs.get())
        # MANUAL MODE
        else:
            # Traversal path for depth-first or breadth-first
            if self.choice.get() == 0 or self.choice.get() == 1:
                if self.next_step:
                    # Displaying path so far
                    self.output_value_3.set(' '.join(self.path))
                    # When end is reached
                    if len(self.path) == ord(self.character) - 96:
                        self.next_step = False
                        # OUTPUT VALUES
                        # Displaying final path
                        self.output_value.set(' '.join(self.path))
                        # Length of path list output
                        self.number_nodes_explored.set('Nodes: {}'.format(len(self.path)))
                        # Total distance
                        self.output_value_2.set('Length: {}'.format(self.output.total_distance))
                        # Reset frontier in breadth_first mode
                        if self.choice.get() == 1:
                            self.output.frontier_nodes = []
                        # Disabling the next step button
                        self.set_manual_button()
                else:
                    # Printing path so far
                    self.output_value_3.set('--')
            # Traversal path for Dijkstra
            elif self.choice.get() == 2:
                if self.next_step:
                    # Printing path so far
                    self.output_value_3.set(' '.join(self.traversal_path))
                    # When end is reached
                    if self.end_input.get() in self.traversal_path:
                        self.next_step = False  # Setting next step mode back to False as path has been completed
                        # OUTPUT VALUES
                        # Displaying final path from file
                        self.output_value.set(' '.join(self.output.path))
                        # Length of path list output
                        self.number_nodes_explored.set('Nodes: {}'.format(len(self.output.path)))
                        # Displaying the path length
                        self.output_value_2.set('Length: {}'.format(self.output.total_length))
                        # Disabling the next step button
                        self.set_manual_button()
                # A* algorithm
                else:
                    # Printing path so far
                    self.output_value_3.set('--')
            # Resetting when not in use
            else:
                self.output_value_3.set('--')

            # Update grid or graph
            if not self.grid_view:
                # Updating the graph (runs draw function)
                plt.close('all')  # Closing all previously opened graphs
                self.update_graph()
            else:
                # Updating grid by running function
                self.grid_app.update_grid(self.display_costs.get())


def main():
    root = Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()
