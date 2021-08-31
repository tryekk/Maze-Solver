from tkinter import *
import a_star_grid_store


class Grid:
    def __init__(self, master):
        # Drawing window and setting title

        master.wm_title("Maze Solver (Grid view)")
        master.geometry('700x700+810+50')
        self.master = master

        # Calling adjacency matrix to be drawn from file
        self.matrix = a_star_grid_store.Grid().matrix

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        # self.master.grid_propagate(False)

        # FRAMES
        # Creating main frame
        mainframe = Frame(self.master, borderwidth=2, relief='solid')
        for row in range(64):
            mainframe.rowconfigure(row, weight=1)
        for col in range(64):
            mainframe.columnconfigure(col, weight=1)
        mainframe.grid(column=0, row=0)

        # Creating frames for each node/cell on grid
        self.frame00 = Frame(mainframe)
        self.frame01 = Frame(mainframe)
        self.frame02 = Frame(mainframe)
        self.frame03 = Frame(mainframe)
        self.frame04 = Frame(mainframe)
        self.frame05 = Frame(mainframe)
        self.frame06 = Frame(mainframe)
        self.frame07 = Frame(mainframe)
        self.frame10 = Frame(mainframe)
        self.frame11 = Frame(mainframe)
        self.frame12 = Frame(mainframe)
        self.frame13 = Frame(mainframe)
        self.frame14 = Frame(mainframe)
        self.frame15 = Frame(mainframe)
        self.frame16 = Frame(mainframe)
        self.frame17 = Frame(mainframe)
        self.frame20 = Frame(mainframe)
        self.frame21 = Frame(mainframe)
        self.frame22 = Frame(mainframe)
        self.frame23 = Frame(mainframe)
        self.frame24 = Frame(mainframe)
        self.frame25 = Frame(mainframe)
        self.frame26 = Frame(mainframe)
        self.frame27 = Frame(mainframe)
        self.frame30 = Frame(mainframe)
        self.frame31 = Frame(mainframe)
        self.frame32 = Frame(mainframe)
        self.frame33 = Frame(mainframe)
        self.frame34 = Frame(mainframe)
        self.frame35 = Frame(mainframe)
        self.frame36 = Frame(mainframe)
        self.frame37 = Frame(mainframe)
        self.frame40 = Frame(mainframe)
        self.frame41 = Frame(mainframe)
        self.frame42 = Frame(mainframe)
        self.frame43 = Frame(mainframe)
        self.frame44 = Frame(mainframe)
        self.frame45 = Frame(mainframe)
        self.frame46 = Frame(mainframe)
        self.frame47 = Frame(mainframe)
        self.frame50 = Frame(mainframe)
        self.frame51 = Frame(mainframe)
        self.frame52 = Frame(mainframe)
        self.frame53 = Frame(mainframe)
        self.frame54 = Frame(mainframe)
        self.frame55 = Frame(mainframe)
        self.frame56 = Frame(mainframe)
        self.frame57 = Frame(mainframe)
        self.frame60 = Frame(mainframe)
        self.frame61 = Frame(mainframe)
        self.frame62 = Frame(mainframe)
        self.frame63 = Frame(mainframe)
        self.frame64 = Frame(mainframe)
        self.frame65 = Frame(mainframe)
        self.frame66 = Frame(mainframe)
        self.frame67 = Frame(mainframe)
        self.frame70 = Frame(mainframe)
        self.frame71 = Frame(mainframe)
        self.frame72 = Frame(mainframe)
        self.frame73 = Frame(mainframe)
        self.frame74 = Frame(mainframe)
        self.frame75 = Frame(mainframe)
        self.frame76 = Frame(mainframe)
        self.frame77 = Frame(mainframe)

        # Runs the function that builds the frames
        self.build_frames()

    def build_frames(self):
        # Setting constant size of cells
        PAD_X = 2
        PAD_Y = 20
        FONT = 'Consolas'
        FONT_COLOUR = 'grey94'
        FONT_SIZE = 11
        B_WIDTH = 1

        # Frame 00
        self.label00 = Label(self.frame00, text=self.matrix[0][0].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                             borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label00.bind("<Button-1>", self.change_value)
        self.label00.pack(fill=BOTH, expand=True)
        self.frame00.grid(row=0, column=0, sticky='nsew')

        # Frame 01
        self.label01 = Label(self.frame01, text=self.matrix[0][1].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label01.bind("<Button-1>", self.change_value_01)
        self.label01.pack(fill=BOTH, expand=True)
        self.frame01.grid(row=0, column=1, sticky='nsew')

        # Frame 02
        self.label02 = Label(self.frame02, text=self.matrix[0][2].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label02.bind("<Button-1>", self.change_value_02)
        self.label02.pack(fill=BOTH, expand=True)
        self.frame02.grid(row=0, column=2, sticky='nsew')

        # Frame 03
        self.label03 = Label(self.frame03, text=self.matrix[0][3].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label03.bind("<Button-1>", self.change_value_03)
        self.label03.pack(fill=BOTH, expand=True)
        self.frame03.grid(row=0, column=3, sticky='nsew')

        # Frame 04
        self.label04 = Label(self.frame04, text=self.matrix[0][4].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label04.bind("<Button-1>", self.change_value_04)
        self.label04.pack(fill=BOTH, expand=True)
        self.frame04.grid(row=0, column=4, sticky='nsew')

        # Frame 05
        self.label05 = Label(self.frame05, text=self.matrix[0][5].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label05.bind("<Button-1>", self.change_value_05)
        self.label05.pack(fill=BOTH, expand=True)
        self.frame05.grid(row=0, column=5, sticky='nsew')

        # Frame 06
        self.label06 = Label(self.frame06, text=self.matrix[0][6].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label06.bind("<Button-1>", self.change_value_06)
        self.label06.pack(fill=BOTH, expand=True)
        self.frame06.grid(row=0, column=6, sticky='nsew')

        # Frame 07
        self.label07 = Label(self.frame07, text=self.matrix[0][7].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label07.bind("<Button-1>", self.change_value_07)
        self.label07.pack(fill=BOTH, expand=True)
        self.frame07.grid(row=0, column=7, sticky='nsew')

        # Frame 10
        self.label10 = Label(self.frame10, text=self.matrix[1][0].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label10.bind("<Button-1>", self.change_value_10)
        self.label10.pack(fill=BOTH, expand=True)
        self.frame10.grid(row=1, column=0, sticky='nsew')

        # Frame 11
        self.label11 = Label(self.frame11, text=self.matrix[1][1].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label11.bind("<Button-1>", self.change_value_11)
        self.label11.pack(fill=BOTH, expand=True)
        self.frame11.grid(row=1, column=1, sticky='nsew')

        # Frame 12
        self.label12 = Label(self.frame12, text=self.matrix[1][2].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label12.bind("<Button-1>", self.change_value_12)
        self.label12.pack(fill=BOTH, expand=True)
        self.frame12.grid(row=1, column=2, sticky='nsew')

        # Frame 13
        self.label13 = Label(self.frame13, text=self.matrix[1][3].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label13.bind("<Button-1>", self.change_value_13)
        self.label13.pack(fill=BOTH, expand=True)
        self.frame13.grid(row=1, column=3, sticky='nsew')

        # Frame 14
        self.label14 = Label(self.frame14, text=self.matrix[1][4].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label14.bind("<Button-1>", self.change_value_14)
        self.label14.pack(fill=BOTH, expand=True)
        self.frame14.grid(row=1, column=4, sticky='nsew')

        # Frame 15
        self.label15 = Label(self.frame15, text=self.matrix[1][5].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label15.bind("<Button-1>", self.change_value_15)
        self.label15.pack(fill=BOTH, expand=True)
        self.frame15.grid(row=1, column=5, sticky='nsew')

        # Frame 16
        self.label16 = Label(self.frame16, text=self.matrix[1][6].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label16.bind("<Button-1>", self.change_value_16)
        self.label16.pack(fill=BOTH, expand=True)
        self.frame16.grid(row=1, column=6, sticky='nsew')

        # Frame 17
        self.label17 = Label(self.frame17, text=self.matrix[1][7].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label17.bind("<Button-1>", self.change_value_17)
        self.label17.pack(fill=BOTH, expand=True)
        self.frame17.grid(row=1, column=7, sticky='nsew')

        # Frame 20
        self.label20 = Label(self.frame20, text=self.matrix[2][0].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label20.bind("<Button-1>", self.change_value_20)
        self.label20.pack(fill=BOTH, expand=True)
        self.frame20.grid(row=2, column=0, sticky='nsew')

        # Frame 21
        self.label21 = Label(self.frame21, text=self.matrix[2][1].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label21.bind("<Button-1>", self.change_value_21)
        self.label21.pack(fill=BOTH, expand=True)
        self.frame21.grid(row=2, column=1, sticky='nsew')

        # Frame 22
        self.label22 = Label(self.frame22, text=self.matrix[2][2].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label22.bind("<Button-1>", self.change_value_22)
        self.label22.pack(fill=BOTH, expand=True)
        self.frame22.grid(row=2, column=2, sticky='nsew')

        # Frame 23
        self.label23 = Label(self.frame23, text=self.matrix[2][3].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label23.bind("<Button-1>", self.change_value_23)
        self.label23.pack(fill=BOTH, expand=True)
        self.frame23.grid(row=2, column=3, sticky='nsew')

        # Frame 24
        self.label24 = Label(self.frame24, text=self.matrix[2][4].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label24.bind("<Button-1>", self.change_value_24)
        self.label24.pack(fill=BOTH, expand=True)
        self.frame24.grid(row=2, column=4, sticky='nsew')

        # Frame 25
        self.label25 = Label(self.frame25, text=self.matrix[2][5].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label25.bind("<Button-1>", self.change_value_25)
        self.label25.pack(fill=BOTH, expand=True)
        self.frame25.grid(row=2, column=5, sticky='nsew')

        # Frame 26
        self.label26 = Label(self.frame26, text=self.matrix[2][6].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label26.bind("<Button-1>", self.change_value_26)
        self.label26.pack(fill=BOTH, expand=True)
        self.frame26.grid(row=2, column=6, sticky='nsew')

        # Frame 27
        self.label27 = Label(self.frame27, text=self.matrix[2][7].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label27.bind("<Button-1>", self.change_value_27)
        self.label27.pack(fill=BOTH, expand=True)
        self.frame27.grid(row=2, column=7, sticky='nsew')

        # Frame 30
        self.label30 = Label(self.frame30, text=self.matrix[3][0].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label30.bind("<Button-1>", self.change_value_30)
        self.label30.pack(fill=BOTH, expand=True)
        self.frame30.grid(row=3, column=0, sticky='nsew')

        # Frame 31
        self.label31 = Label(self.frame31, text=self.matrix[3][1].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label31.bind("<Button-1>", self.change_value_31)
        self.label31.pack(fill=BOTH, expand=True)
        self.frame31.grid(row=3, column=1, sticky='nsew')

        # Frame 32
        self.label32 = Label(self.frame32, text=self.matrix[3][2].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label32.bind("<Button-1>", self.change_value_32)
        self.label32.pack(fill=BOTH, expand=True)
        self.frame32.grid(row=3, column=2, sticky='nsew')

        # Frame 33
        self.label33 = Label(self.frame33, text=self.matrix[3][3].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label33.bind("<Button-1>", self.change_value_33)
        self.label33.pack(fill=BOTH, expand=True)
        self.frame33.grid(row=3, column=3, sticky='nsew')

        # Frame 34
        self.label34 = Label(self.frame34, text=self.matrix[3][4].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label34.bind("<Button-1>", self.change_value_34)
        self.label34.pack(fill=BOTH, expand=True)
        self.frame34.grid(row=3, column=4, sticky='nsew')

        # Frame 35
        self.label35 = Label(self.frame35, text=self.matrix[3][5].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label35.bind("<Button-1>", self.change_value_35)
        self.label35.pack(fill=BOTH, expand=True)
        self.frame35.grid(row=3, column=5, sticky='nsew')

        # Frame 36
        self.label36 = Label(self.frame36, text=self.matrix[3][6].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label36.bind("<Button-1>", self.change_value_36)
        self.label36.pack(fill=BOTH, expand=True)
        self.frame36.grid(row=3, column=6, sticky='nsew')

        # Frame 37
        self.label37 = Label(self.frame37, text=self.matrix[3][7].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                             borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label37.bind("<Button-1>", self.change_value_37)
        self.label37.pack(fill=BOTH, expand=True)
        self.frame37.grid(row=3, column=7, sticky='nsew')

        # Frame 40
        self.label40 = Label(self.frame40, text=self.matrix[4][0].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label40.bind("<Button-1>", self.change_value_40)
        self.label40.pack(fill=BOTH, expand=True)
        self.frame40.grid(row=4, column=0, sticky='nsew')

        # Frame 41
        self.label41 = Label(self.frame41, text=self.matrix[4][1].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label41.bind("<Button-1>", self.change_value_41)
        self.label41.pack(fill=BOTH, expand=True)
        self.frame41.grid(row=4, column=1, sticky='nsew')

        # Frame 42
        self.label42 = Label(self.frame42, text=self.matrix[4][2].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label42.bind("<Button-1>", self.change_value_42)
        self.label42.pack(fill=BOTH, expand=True)
        self.frame42.grid(row=4, column=2, sticky='nsew')

        # Frame 43
        self.label43 = Label(self.frame43, text=self.matrix[4][3].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label43.bind("<Button-1>", self.change_value_43)
        self.label43.pack(fill=BOTH, expand=True)
        self.frame43.grid(row=4, column=3, sticky='nsew')

        # Frame 44
        self.label44 = Label(self.frame44, text=self.matrix[4][4].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label44.bind("<Button-1>", self.change_value_44)
        self.label44.pack(fill=BOTH, expand=True)
        self.frame44.grid(row=4, column=4, sticky='nsew')

        # Frame 45
        self.label45 = Label(self.frame45, text=self.matrix[4][5].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label45.bind("<Button-1>", self.change_value_45)
        self.label45.pack(fill=BOTH, expand=True)
        self.frame45.grid(row=4, column=5, sticky='nsew')

        # Frame 46
        self.label46 = Label(self.frame46, text=self.matrix[4][6].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label46.bind("<Button-1>", self.change_value_46)
        self.label46.pack(fill=BOTH, expand=True)
        self.frame46.grid(row=4, column=6, sticky='nsew')

        # Frame 47
        self.label47 = Label(self.frame47, text=self.matrix[4][7].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label47.bind("<Button-1>", self.change_value_47)
        self.label47.pack(fill=BOTH, expand=True)
        self.frame47.grid(row=4, column=7, sticky='nsew')

        # Frame 50
        self.label50 = Label(self.frame50, text=self.matrix[5][0].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label50.bind("<Button-1>", self.change_value_50)
        self.label50.pack(fill=BOTH, expand=True)
        self.frame50.grid(row=5, column=0, sticky='nsew')

        # Frame 51
        self.label51 = Label(self.frame51, text=self.matrix[5][1].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label51.bind("<Button-1>", self.change_value_51)
        self.label51.pack(fill=BOTH, expand=True)
        self.frame51.grid(row=5, column=1, sticky='nsew')

        # Frame 52
        self.label52 = Label(self.frame52, text=self.matrix[5][2].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label52.bind("<Button-1>", self.change_value_52)
        self.label52.pack(fill=BOTH, expand=True)
        self.frame52.grid(row=5, column=2, sticky='nsew')

        # Frame 53
        self.label53 = Label(self.frame53, text=self.matrix[5][3].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label53.bind("<Button-1>", self.change_value_53)
        self.label53.pack(fill=BOTH, expand=True)
        self.frame53.grid(row=5, column=3, sticky='nsew')

        # Frame 54
        self.label54 = Label(self.frame54, text=self.matrix[5][4].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label54.bind("<Button-1>", self.change_value_54)
        self.label54.pack(fill=BOTH, expand=True)
        self.frame54.grid(row=5, column=4, sticky='nsew')

        # Frame 55
        self.label55 = Label(self.frame55, text=self.matrix[5][5].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label55.bind("<Button-1>", self.change_value_55)
        self.label55.pack(fill=BOTH, expand=True)
        self.frame55.grid(row=5, column=5, sticky='nsew')

        # Frame 56
        self.label56 = Label(self.frame56, text=self.matrix[5][6].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label56.bind("<Button-1>", self.change_value_56)
        self.label56.pack(fill=BOTH, expand=True)
        self.frame56.grid(row=5, column=6, sticky='nsew')

        # Frame 57
        self.label57 = Label(self.frame57, text=self.matrix[5][7].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label57.bind("<Button-1>", self.change_value_57)
        self.label57.pack(fill=BOTH, expand=True)
        self.frame57.grid(row=5, column=7, sticky='nsew')

        # Frame 60
        self.label60 = Label(self.frame60, text=self.matrix[6][0].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label60.bind("<Button-1>", self.change_value_60)
        self.label60.pack(fill=BOTH, expand=True)
        self.frame60.grid(row=6, column=0, sticky='nsew')

        # Frame 61
        self.label61 = Label(self.frame61, text=self.matrix[6][1].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label61.bind("<Button-1>", self.change_value_61)
        self.label61.pack(fill=BOTH, expand=True)
        self.frame61.grid(row=6, column=1, sticky='nsew')

        # Frame 62
        self.label62 = Label(self.frame62, text=self.matrix[6][2].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label62.bind("<Button-1>", self.change_value_62)
        self.label62.pack(fill=BOTH, expand=True)
        self.frame62.grid(row=6, column=2, sticky='nsew')

        # Frame 63
        self.label63 = Label(self.frame63, text=self.matrix[6][3].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label63.bind("<Button-1>", self.change_value_63)
        self.label63.pack(fill=BOTH, expand=True)
        self.frame63.grid(row=6, column=3, sticky='nsew')

        # Frame 64
        self.label64 = Label(self.frame64, text=self.matrix[6][4].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label64.bind("<Button-1>", self.change_value_64)
        self.label64.pack(fill=BOTH, expand=True)
        self.frame64.grid(row=6, column=4, sticky='nsew')

        # Frame 65
        self.label65 = Label(self.frame65, text=self.matrix[6][5].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label65.bind("<Button-1>", self.change_value_65)
        self.label65.pack(fill=BOTH, expand=True)
        self.frame65.grid(row=6, column=5, sticky='nsew')

        # Frame 66
        self.label66 = Label(self.frame66, text=self.matrix[6][6].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label66.bind("<Button-1>", self.change_value_66)
        self.label66.pack(fill=BOTH, expand=True)
        self.frame66.grid(row=6, column=6, sticky='nsew')

        # Frame 67
        self.label67 = Label(self.frame67, text=self.matrix[6][7].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label67.bind("<Button-1>", self.change_value_67)
        self.label67.pack(fill=BOTH, expand=True)
        self.frame67.grid(row=6, column=7, sticky='nsew')

        # Frame 70
        self.label70 = Label(self.frame70, text=self.matrix[7][0].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label70.bind("<Button-1>", self.change_value_70)
        self.label70.pack(fill=BOTH, expand=True)
        self.frame70.grid(row=7, column=0, sticky='nsew')

        # Frame 71
        self.label71 = Label(self.frame71, text=self.matrix[7][1].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label71.bind("<Button-1>", self.change_value_71)
        self.label71.pack(fill=BOTH, expand=True)
        self.frame71.grid(row=7, column=1, sticky='nsew')

        # Frame 72
        self.label72 = Label(self.frame72, text=self.matrix[7][2].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label72.bind("<Button-1>", self.change_value_72)
        self.label72.pack(fill=BOTH, expand=True)
        self.frame72.grid(row=7, column=2, sticky='nsew')

        # Frame 73
        self.label73 = Label(self.frame73, text=self.matrix[7][3].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label73.bind("<Button-1>", self.change_value_73)
        self.label73.pack(fill=BOTH, expand=True)
        self.frame73.grid(row=7, column=3, sticky='nsew')

        # Frame 74
        self.label74 = Label(self.frame74, text=self.matrix[7][4].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label74.bind("<Button-1>", self.change_value_74)
        self.label74.pack(fill=BOTH, expand=True)
        self.frame74.grid(row=7, column=4, sticky='nsew')

        # Frame 75
        self.label75 = Label(self.frame75, text=self.matrix[7][5].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label75.bind("<Button-1>", self.change_value_75)
        self.label75.pack(fill=BOTH, expand=True)
        self.frame75.grid(row=7, column=5, sticky='nsew')

        # Frame 76
        self.label76 = Label(self.frame76, text=self.matrix[7][6].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label76.bind("<Button-1>", self.change_value_76)
        self.label76.pack(fill=BOTH, expand=True)
        self.frame76.grid(row=7, column=6, sticky='nsew')

        # Frame 77
        self.label77 = Label(self.frame77, text=self.matrix[7][7].cost, fg=FONT_COLOUR, padx=PAD_X, pady=PAD_Y,
                                borderwidth=B_WIDTH, relief='solid', font=(FONT, FONT_SIZE, 'bold'))
        self.label77.bind("<Button-1>", self.change_value_77)
        self.label77.pack(fill=BOTH, expand=True)
        self.frame77.grid(row=7, column=7, sticky='nsew')

        # Update colours
        self.update_grid(0)

    def update_grid(self, display_costs):
        if display_costs == 0:
            # Global colour for path (can be changed here)
            self.NORMAL_COLOUR = 'grey94'
            self.WALL_COLOUR = 'grey60'
            self.START_COLOUR = 'green'
            START_FONT_COLOUR = 'green'
            self.END_COLOUR = 'red'
            END_FONT_COLOUR = 'red'
            PATH_COLOUR = '#FACA02'
            PATH_FONT_COLOUR = '#FACA02'
            OPEN_COLOUR = 'PaleTurquoise1'
            OPEN_FONT_COLOUR = 'PaleTurquoise1'
            FRONTIER_COLOUR = 'LightCyan2'
            FRONTIER_FONT_COLOUR = 'LightCyan2'
        else:
            # Global colour for path (can be changed here)
            self.NORMAL_COLOUR = 'grey94'
            self.WALL_COLOUR = 'grey60'
            self.START_COLOUR = 'green'
            START_FONT_COLOUR = 'black'  # 'green'
            self.END_COLOUR = 'red'
            END_FONT_COLOUR = 'black'  # 'red'
            PATH_COLOUR = '#FACA02'
            PATH_FONT_COLOUR = 'black'  # '#FACA02'
            OPEN_COLOUR = 'PaleTurquoise1'
            OPEN_FONT_COLOUR = 'black'  # 'PaleTurquoise1'
            FRONTIER_COLOUR = 'LightCyan2'
            FRONTIER_FONT_COLOUR = 'black'  # 'LightCyan2'

        # Updating colours for cells on grid

        # Node 00
        if self.matrix[0][0].value == 0:
            self.label00.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][0].value == 1:
            self.label00.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][0].value == 2:
            self.label00.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[0][0].cost)
            if self.matrix[0][0].cost == '11.1+11.1\n11.1':
                self.label00.configure(bg=self.START_COLOUR, fg=self.START_COLOUR, text=self.matrix[0][0].cost)
        elif self.matrix[0][0].value == 3:
            self.label00.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR)
            if self.matrix[0][0].cost == '11.1+11.1\n11.1':
                self.label00.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[0][0].value == 4:
            self.label00.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[0][0].cost)
        elif self.matrix[0][0].value == 5:
            self.label00.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[0][0].cost)
        elif self.matrix[0][0].value == 9:
            self.label00.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[0][0].cost)

        # Node 01
        if self.matrix[0][1].value == 0:
            self.label01.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][1].value == 1:
            self.label01.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][1].value == 2:
            self.label01.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[0][1].cost)
            if self.matrix[0][1].cost == '11.1+11.1\n11.1':
                self.label01.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][1].value == 3:
            self.label01.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[0][1].cost)
            if self.matrix[0][1].cost == '11.1+11.1\n11.1':
                self.label01.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[0][1].value == 4:
            self.label01.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[0][1].cost)
        elif self.matrix[0][1].value == 5:
            self.label01.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[0][1].cost)
        elif self.matrix[0][1].value == 9:
            self.label01.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[0][1].cost)

        # Node 02
        if self.matrix[0][2].value == 0:
            self.label02.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][2].value == 1:
            self.label02.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][2].value == 2:
            self.label02.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[0][2].cost)
            if self.matrix[0][2].cost == '11.1+11.1\n11.1':
                self.label02.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][2].value == 3:
            self.label02.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[0][2].cost)
            if self.matrix[0][2].cost == '11.1+11.1\n11.1':
                self.label02.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[0][2].value == 4:
            self.label02.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[0][2].cost)
        elif self.matrix[0][2].value == 5:
            self.label02.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[0][2].cost)
        elif self.matrix[0][2].value == 9:
            self.label02.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[0][2].cost)

        # Node 03
        if self.matrix[0][3].value == 0:
            self.label03.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][3].value == 1:
            self.label03.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][3].value == 2:
            self.label03.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[0][3].cost)
            if self.matrix[0][3].cost == '11.1+11.1\n11.1':
                self.label03.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][3].value == 3:
            self.label03.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[0][3].cost)
            if self.matrix[0][3].cost == '11.1+11.1\n11.1':
                self.label03.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[0][3].value == 4:
            self.label03.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[0][3].cost)
        elif self.matrix[0][3].value == 5:
            self.label03.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[0][3].cost)
        elif self.matrix[0][3].value == 9:
            self.label03.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[0][3].cost)

        # Node 04
        if self.matrix[0][4].value == 0:
            self.label04.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][4].value == 1:
            self.label04.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][4].value == 2:
            self.label04.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[0][4].cost)
            if self.matrix[0][4].cost == '11.1+11.1\n11.1':
                self.label04.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][4].value == 3:
            self.label04.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[0][4].cost)
            if self.matrix[0][4].cost == '11.1+11.1\n11.1':
                self.label04.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[0][4].value == 4:
            self.label04.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[0][4].cost)
        elif self.matrix[0][4].value == 5:
            self.label04.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[0][4].cost)
        elif self.matrix[0][4].value == 9:
            self.label04.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[0][4].cost)

        # Node 05
        if self.matrix[0][5].value == 0:
            self.label05.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][5].value == 1:
            self.label05.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][5].value == 2:
            self.label05.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[0][5].cost)
            if self.matrix[0][5].cost == '11.1+11.1\n11.1':
                self.label05.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][5].value == 3:
            self.label05.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[0][5].cost)
            if self.matrix[0][5].cost == '11.1+11.1\n11.1':
                self.label05.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[0][5].value == 4:
            self.label05.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[0][5].cost)
        elif self.matrix[0][5].value == 5:
            self.label05.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[0][5].cost)
        elif self.matrix[0][5].value == 9:
            self.label05.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[0][5].cost)

        # Node 06
        if self.matrix[0][6].value == 0:
            self.label06.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][6].value == 1:
            self.label06.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][6].value == 2:
            self.label06.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[0][6].cost)
            if self.matrix[0][6].cost == '11.1+11.1\n11.1':
                self.label06.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][6].value == 3:
            self.label06.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[0][6].cost)
            if self.matrix[0][6].cost == '11.1+11.1\n11.1':
                self.label06.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[0][6].value == 4:
            self.label06.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[0][6].cost)
        elif self.matrix[0][6].value == 5:
            self.label06.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[0][6].cost)
        elif self.matrix[0][6].value == 9:
            self.label06.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[0][6].cost)

        # Node 07
        if self.matrix[0][7].value == 0:
            self.label07.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][7].value == 1:
            self.label07.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][7].value == 2:
            self.label07.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[0][7].cost)
            if self.matrix[0][7].cost == '11.1+11.1\n11.1':
                self.label07.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][7].value == 3:
            self.label07.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[0][7].cost)
            if self.matrix[0][7].cost == '11.1+11.1\n11.1':
                self.label07.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[0][7].value == 4:
            self.label07.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[0][7].cost)
        elif self.matrix[0][7].value == 5:
            self.label07.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[0][7].cost)
        elif self.matrix[0][7].value == 9:
            self.label07.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[0][7].cost)

        # Node 10
        if self.matrix[1][0].value == 0:
            self.label10.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][0].value == 1:
            self.label10.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][0].value == 2:
            self.label10.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[1][0].cost)
            if self.matrix[1][0].cost == '11.1+11.1\n11.1':
                self.label10.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][0].value == 3:
            self.label10.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[1][0].cost)
            if self.matrix[1][0].cost == '11.1+11.1\n11.1':
                self.label10.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[1][0].value == 4:
            self.label10.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[1][0].cost)
        elif self.matrix[1][0].value == 5:
            self.label10.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[1][0].cost)
        elif self.matrix[1][0].value == 9:
            self.label10.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[1][0].cost)

        # Node 11
        if self.matrix[1][1].value == 0:
            self.label11.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][1].value == 1:
            self.label11.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][1].value == 2:
            self.label11.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[1][1].cost)
            if self.matrix[1][1].cost == '11.1+11.1\n11.1':
                self.label11.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][1].value == 3:
            self.label11.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[1][1].cost)
            if self.matrix[1][1].cost == '11.1+11.1\n11.1':
                self.label11.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[1][1].value == 4:
            self.label11.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[1][1].cost)
        elif self.matrix[1][1].value == 5:
            self.label11.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[1][1].cost)
        elif self.matrix[1][1].value == 9:
            self.label11.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[1][1].cost)

        # Node 12
        if self.matrix[1][2].value == 0:
            self.label12.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][2].value == 1:
            self.label12.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][2].value == 2:
            self.label12.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[1][2].cost)
            if self.matrix[1][2].cost == '11.1+11.1\n11.1':
                self.label12.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][2].value == 3:
            self.label12.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[1][2].cost)
            if self.matrix[1][2].cost == '11.1+11.1\n11.1':
                self.label12.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[1][2].value == 4:
            self.label12.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[1][2].cost)
        elif self.matrix[1][2].value == 5:
            self.label12.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[1][2].cost)
        elif self.matrix[1][2].value == 9:
            self.label12.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[1][2].cost)

        # Node 13
        if self.matrix[1][3].value == 0:
            self.label13.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][3].value == 1:
            self.label13.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][3].value == 2:
            self.label13.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[1][3].cost)
            if self.matrix[1][3].cost == '11.1+11.1\n11.1':
                self.label13.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][3].value == 3:
            self.label13.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[1][3].cost)
            if self.matrix[1][3].cost == '11.1+11.1\n11.1':
                self.label13.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[1][3].value == 4:
            self.label13.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[1][3].cost)
        elif self.matrix[1][3].value == 5:
            self.label13.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[1][3].cost)
        elif self.matrix[1][3].value == 9:
            self.label13.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[1][3].cost)

        # Node 14
        if self.matrix[1][4].value == 0:
            self.label14.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][4].value == 1:
            self.label14.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][4].value == 2:
            self.label14.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[1][4].cost)
            if self.matrix[1][4].cost == '11.1+11.1\n11.1':
                self.label14.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][4].value == 3:
            self.label14.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[1][4].cost)
            if self.matrix[1][4].cost == '11.1+11.1\n11.1':
                self.label14.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[1][4].value == 4:
            self.label14.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[1][4].cost)
        elif self.matrix[1][4].value == 5:
            self.label14.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[1][4].cost)
        elif self.matrix[1][4].value == 9:
            self.label14.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[1][4].cost)

        # Node 15
        if self.matrix[1][5].value == 0:
            self.label15.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][5].value == 1:
            self.label15.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][5].value == 2:
            self.label15.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[1][5].cost)
            if self.matrix[1][5].cost == '11.1+11.1\n11.1':
                self.label15.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][5].value == 3:
            self.label15.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[1][5].cost)
            if self.matrix[1][5].cost == '11.1+11.1\n11.1':
                self.label15.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[1][5].value == 4:
            self.label15.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[1][5].cost)
        elif self.matrix[1][5].value == 5:
            self.label15.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[1][5].cost)
        elif self.matrix[1][5].value == 9:
            self.label15.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[1][5].cost)

        # Node 16
        if self.matrix[1][6].value == 0:
            self.label16.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][6].value == 1:
            self.label16.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][6].value == 2:
            self.label16.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[1][6].cost)
            if self.matrix[1][6].cost == '11.1+11.1\n11.1':
                self.label16.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][6].value == 3:
            self.label16.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[1][6].cost)
            if self.matrix[1][6].cost == '11.1+11.1\n11.1':
                self.label16.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[1][6].value == 4:
            self.label16.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[1][6].cost)
        elif self.matrix[1][6].value == 5:
            self.label16.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[1][6].cost)
        elif self.matrix[1][6].value == 9:
            self.label16.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[1][6].cost)

        # Node 17
        if self.matrix[1][7].value == 0:
            self.label17.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][7].value == 1:
            self.label17.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][7].value == 2:
            self.label17.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[1][7].cost)
            if self.matrix[1][7].cost == '11.1+11.1\n11.1':
                self.label17.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][7].value == 3:
            self.label17.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[1][7].cost)
            if self.matrix[1][7].cost == '11.1+11.1\n11.1':
                self.label17.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[1][7].value == 4:
            self.label17.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[1][7].cost)
        elif self.matrix[1][7].value == 5:
            self.label17.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[1][7].cost)
        elif self.matrix[1][7].value == 9:
            self.label17.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[1][7].cost)

        # Node 20
        if self.matrix[2][0].value == 0:
            self.label20.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][0].value == 1:
            self.label20.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][0].value == 2:
            self.label20.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[2][0].cost)
            if self.matrix[2][0].cost == '11.1+11.1\n11.1':
                self.label20.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][0].value == 3:
            self.label20.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[2][0].cost)
            if self.matrix[2][0].cost == '11.1+11.1\n11.1':
                self.label20.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[2][0].value == 4:
            self.label20.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[2][0].cost)
        elif self.matrix[2][0].value == 5:
            self.label20.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[2][0].cost)
        elif self.matrix[2][0].value == 9:
            self.label20.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[2][0].cost)

        # Node 21
        if self.matrix[2][1].value == 0:
            self.label21.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][1].value == 1:
            self.label21.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][1].value == 2:
            self.label21.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[2][1].cost)
            if self.matrix[2][1].cost == '11.1+11.1\n11.1':
                self.label21.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][1].value == 3:
            self.label21.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[2][1].cost)
            if self.matrix[2][1].cost == '11.1+11.1\n11.1':
                self.label21.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[2][1].value == 4:
            self.label21.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[2][1].cost)
        elif self.matrix[2][1].value == 5:
            self.label21.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[2][1].cost)
        elif self.matrix[2][1].value == 9:
            self.label21.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[2][1].cost)

        # Node 22
        if self.matrix[2][2].value == 0:
            self.label22.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][2].value == 1:
            self.label22.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][2].value == 2:
            self.label22.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[2][2].cost)
            if self.matrix[2][2].cost == '11.1+11.1\n11.1':
                self.label22.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][2].value == 3:
            self.label22.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[2][2].cost)
            if self.matrix[2][2].cost == '11.1+11.1\n11.1':
                self.label22.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[2][2].value == 4:
            self.label22.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[2][2].cost)
        elif self.matrix[2][2].value == 5:
            self.label22.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[2][2].cost)
        elif self.matrix[2][2].value == 9:
            self.label22.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[2][2].cost)

        # Node 23
        if self.matrix[2][3].value == 0:
            self.label23.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][3].value == 1:
            self.label23.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][3].value == 2:
            self.label23.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[2][3].cost)
            if self.matrix[2][3].cost == '11.1+11.1\n11.1':
                self.label23.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][3].value == 3:
            self.label23.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[2][3].cost)
            if self.matrix[2][3].cost == '11.1+11.1\n11.1':
                self.label23.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[2][3].value == 4:
            self.label23.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[2][3].cost)
        elif self.matrix[2][3].value == 5:
            self.label23.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[2][3].cost)
        elif self.matrix[2][3].value == 9:
            self.label23.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[2][3].cost)

        # Node 24
        if self.matrix[2][4].value == 0:
            self.label24.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][4].value == 1:
            self.label24.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][4].value == 2:
            self.label24.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[2][4].cost)
            if self.matrix[2][4].cost == '11.1+11.1\n11.1':
                self.label24.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][4].value == 3:
            self.label24.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[2][4].cost)
            if self.matrix[2][4].cost == '11.1+11.1\n11.1':
                self.label24.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[2][4].value == 4:
            self.label24.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[2][4].cost)
        elif self.matrix[2][4].value == 5:
            self.label24.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[2][4].cost)
        elif self.matrix[2][4].value == 9:
            self.label24.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[2][4].cost)

        # Node 25
        if self.matrix[2][5].value == 0:
            self.label25.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][5].value == 1:
            self.label25.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][5].value == 2:
            self.label25.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[2][5].cost)
            if self.matrix[2][5].cost == '11.1+11.1\n11.1':
                self.label25.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][5].value == 3:
            self.label25.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[2][5].cost)
            if self.matrix[2][5].cost == '11.1+11.1\n11.1':
                self.label25.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[2][5].value == 4:
            self.label25.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[2][5].cost)
        elif self.matrix[2][5].value == 5:
            self.label25.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[2][5].cost)
        elif self.matrix[2][5].value == 9:
            self.label25.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[2][5].cost)

        # Node 26
        if self.matrix[2][6].value == 0:
            self.label26.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][6].value == 1:
            self.label26.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][6].value == 2:
            self.label26.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[2][6].cost)
            if self.matrix[2][6].cost == '11.1+11.1\n11.1':
                self.label26.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][6].value == 3:
            self.label26.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[2][6].cost)
            if self.matrix[2][6].cost == '11.1+11.1\n11.1':
                self.label26.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[2][6].value == 4:
            self.label26.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[2][6].cost)
        elif self.matrix[2][6].value == 5:
            self.label26.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[2][6].cost)
        elif self.matrix[2][6].value == 9:
            self.label26.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[2][6].cost)

        # Node 27
        if self.matrix[2][7].value == 0:
            self.label27.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][7].value == 1:
            self.label27.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][7].value == 2:
            self.label27.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[2][7].cost)
            if self.matrix[2][7].cost == '11.1+11.1\n11.1':
                self.label27.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][7].value == 3:
            self.label27.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[2][7].cost)
            if self.matrix[2][7].cost == '11.1+11.1\n11.1':
                self.label27.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[2][7].value == 4:
            self.label27.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[2][7].cost)
        elif self.matrix[2][7].value == 5:
            self.label27.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[2][7].cost)
        elif self.matrix[2][7].value == 9:
            self.label27.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[2][7].cost)

        # Node 30
        if self.matrix[3][0].value == 0:
            self.label30.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][0].value == 1:
            self.label30.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][0].value == 2:
            self.label30.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[3][0].cost)
            if self.matrix[3][0].cost == '11.1+11.1\n11.1':
                self.label30.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][0].value == 3:
            self.label30.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[3][0].cost)
            if self.matrix[3][0].cost == '11.1+11.1\n11.1':
                self.label30.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[3][0].value == 4:
            self.label30.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[3][0].cost)
        elif self.matrix[3][0].value == 5:
            self.label30.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[3][0].cost)
        elif self.matrix[3][0].value == 9:
            self.label30.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[3][0].cost)

        # Node 31
        if self.matrix[3][1].value == 0:
            self.label31.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][1].value == 1:
            self.label31.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][1].value == 2:
            self.label31.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[3][1].cost)
            if self.matrix[3][1].cost == '11.1+11.1\n11.1':
                self.label31.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][1].value == 3:
            self.label31.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[3][1].cost)
            if self.matrix[3][1].cost == '11.1+11.1\n11.1':
                self.label31.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[3][1].value == 4:
            self.label31.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[3][1].cost)
        elif self.matrix[3][1].value == 5:
            self.label31.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[3][1].cost)
        elif self.matrix[3][1].value == 9:
            self.label31.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[3][1].cost)

        # Node 32
        if self.matrix[3][2].value == 0:
            self.label32.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][2].value == 1:
            self.label32.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][2].value == 2:
            self.label32.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[3][2].cost)
            if self.matrix[3][2].cost == '11.1+11.1\n11.1':
                self.label32.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][2].value == 3:
            self.label32.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[3][2].cost)
            if self.matrix[3][2].cost == '11.1+11.1\n11.1':
                self.label32.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[3][2].value == 4:
            self.label32.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[3][2].cost)
        elif self.matrix[3][2].value == 5:
            self.label32.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[3][2].cost)
        elif self.matrix[3][2].value == 9:
            self.label32.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[3][2].cost)

        # Node 33
        if self.matrix[3][3].value == 0:
            self.label33.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][3].value == 1:
            self.label33.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][3].value == 2:
            self.label33.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[3][3].cost)
            if self.matrix[3][3].cost == '11.1+11.1\n11.1':
                self.label33.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][3].value == 3:
            self.label33.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[3][3].cost)
            if self.matrix[3][3].cost == '11.1+11.1\n11.1':
                self.label33.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[3][3].value == 4:
            self.label33.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[3][3].cost)
        elif self.matrix[3][3].value == 5:
            self.label33.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[3][3].cost)
        elif self.matrix[3][3].value == 9:
            self.label33.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[3][3].cost)

        # Node 34
        if self.matrix[3][4].value == 0:
            self.label34.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][4].value == 1:
            self.label34.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][4].value == 2:
            self.label34.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[3][4].cost)
            if self.matrix[3][4].cost == '11.1+11.1\n11.1':
                self.label34.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][4].value == 3:
            self.label34.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[3][4].cost)
            if self.matrix[3][4].cost == '11.1+11.1\n11.1':
                self.label34.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[3][4].value == 4:
            self.label34.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[3][4].cost)
        elif self.matrix[3][4].value == 5:
            self.label34.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[3][4].cost)
        elif self.matrix[3][4].value == 9:
            self.label34.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[3][4].cost)

        # Node 35
        if self.matrix[3][5].value == 0:
            self.label35.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][5].value == 1:
            self.label35.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][5].value == 2:
            self.label35.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[3][5].cost)
            if self.matrix[3][5].cost == '11.1+11.1\n11.1':
                self.label35.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][5].value == 3:
            self.label35.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[3][5].cost)
            if self.matrix[3][5].cost == '11.1+11.1\n11.1':
                self.label35.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[3][5].value == 4:
            self.label35.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[3][5].cost)
        elif self.matrix[3][5].value == 5:
            self.label35.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[3][5].cost)
        elif self.matrix[3][5].value == 9:
            self.label35.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[3][5].cost)

        # Node 36
        if self.matrix[3][6].value == 0:
            self.label36.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][6].value == 1:
            self.label36.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][6].value == 2:
            self.label36.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[3][6].cost)
            if self.matrix[3][6].cost == '11.1+11.1\n11.1':
                self.label36.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][6].value == 3:
            self.label36.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[3][6].cost)
            if self.matrix[3][6].cost == '11.1+11.1\n11.1':
                self.label36.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[3][6].value == 4:
            self.label36.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[3][6].cost)
        elif self.matrix[3][6].value == 5:
            self.label36.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[3][6].cost)
        elif self.matrix[3][6].value == 9:
            self.label36.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[3][6].cost)

        # Node 37
        if self.matrix[3][7].value == 0:
            self.label37.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][7].value == 1:
            self.label37.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][7].value == 2:
            self.label37.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[3][7].cost)
            if self.matrix[3][7].cost == '11.1+11.1\n11.1':
                self.label37.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][7].value == 3:
            self.label37.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[3][7].cost)
            if self.matrix[3][7].cost == '11.1+11.1\n11.1':
                self.label37.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[3][7].value == 4:
            self.label37.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[3][7].cost)
        elif self.matrix[3][7].value == 5:
            self.label37.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[3][7].cost)
        elif self.matrix[3][7].value == 9:
            self.label37.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[3][7].cost)

        # Node 40
        if self.matrix[4][0].value == 0:
            self.label40.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][0].value == 1:
            self.label40.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][0].value == 2:
            self.label40.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[4][0].cost)
            if self.matrix[4][0].cost == '11.1+11.1\n11.1':
                self.label40.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][0].value == 3:
            self.label40.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[4][0].cost)
            if self.matrix[4][0].cost == '11.1+11.1\n11.1':
                self.label40.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[4][0].value == 4:
            self.label40.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[4][0].cost)
        elif self.matrix[4][0].value == 5:
            self.label40.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[4][0].cost)
        elif self.matrix[4][0].value == 9:
            self.label40.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[4][0].cost)

        # Node 41
        if self.matrix[4][1].value == 0:
            self.label41.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][1].value == 1:
            self.label41.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][1].value == 2:
            self.label41.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[4][1].cost)
            if self.matrix[4][1].cost == '11.1+11.1\n11.1':
                self.label41.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][1].value == 3:
            self.label41.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[4][1].cost)
            if self.matrix[4][1].cost == '11.1+11.1\n11.1':
                self.label41.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[4][1].value == 4:
            self.label41.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[4][1].cost)
        elif self.matrix[4][1].value == 5:
            self.label41.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[4][1].cost)
        elif self.matrix[4][1].value == 9:
            self.label41.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[4][1].cost)

        # Node 42
        if self.matrix[4][2].value == 0:
            self.label42.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][2].value == 1:
            self.label42.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][2].value == 2:
            self.label42.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[4][2].cost)
            if self.matrix[4][2].cost == '11.1+11.1\n11.1':
                self.label42.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][2].value == 3:
            self.label42.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[4][2].cost)
            if self.matrix[4][2].cost == '11.1+11.1\n11.1':
                self.label42.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[4][2].value == 4:
            self.label42.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[4][2].cost)
        elif self.matrix[4][2].value == 5:
            self.label42.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[4][2].cost)
        elif self.matrix[4][2].value == 9:
            self.label42.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[4][2].cost)

        # Node 43
        if self.matrix[4][3].value == 0:
            self.label43.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][3].value == 1:
            self.label43.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][3].value == 2:
            self.label43.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[4][3].cost)
            if self.matrix[4][3].cost == '11.1+11.1\n11.1':
                self.label43.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][3].value == 3:
            self.label43.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[4][3].cost)
            if self.matrix[4][3].cost == '11.1+11.1\n11.1':
                self.label43.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[4][3].value == 4:
            self.label43.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[4][3].cost)
        elif self.matrix[4][3].value == 5:
            self.label43.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[4][3].cost)
        elif self.matrix[4][3].value == 9:
            self.label43.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[4][3].cost)

        # Node 44
        if self.matrix[4][4].value == 0:
            self.label44.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][4].value == 1:
            self.label44.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][4].value == 2:
            self.label44.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[4][4].cost)
            if self.matrix[4][4].cost == '11.1+11.1\n11.1':
                self.label44.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][4].value == 3:
            self.label44.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[4][4].cost)
            if self.matrix[4][4].cost == '11.1+11.1\n11.1':
                self.label44.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[4][4].value == 4:
            self.label44.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[4][4].cost)
        elif self.matrix[4][4].value == 5:
            self.label44.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[4][4].cost)
        elif self.matrix[4][4].value == 9:
            self.label44.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[4][4].cost)

        # Node 45
        if self.matrix[4][5].value == 0:
            self.label45.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][5].value == 1:
            self.label45.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][5].value == 2:
            self.label45.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[4][5].cost)
            if self.matrix[4][5].cost == '11.1+11.1\n11.1':
                self.label45.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][5].value == 3:
            self.label45.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[4][5].cost)
            if self.matrix[4][5].cost == '11.1+11.1\n11.1':
                self.label45.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[4][5].value == 4:
            self.label45.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[4][5].cost)
        elif self.matrix[4][5].value == 5:
            self.label45.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[4][5].cost)
        elif self.matrix[4][5].value == 9:
            self.label45.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[4][5].cost)

        # Node 46
        if self.matrix[4][6].value == 0:
            self.label46.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][6].value == 1:
            self.label46.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][6].value == 2:
            self.label46.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[4][6].cost)
            if self.matrix[4][6].cost == '11.1+11.1\n11.1':
                self.label46.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][6].value == 3:
            self.label46.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[4][6].cost)
            if self.matrix[4][6].cost == '11.1+11.1\n11.1':
                self.label46.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[4][6].value == 4:
            self.label46.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[4][6].cost)
        elif self.matrix[4][6].value == 5:
            self.label46.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[4][6].cost)
        elif self.matrix[4][6].value == 9:
            self.label46.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[4][6].cost)

        # Node 47
        if self.matrix[4][7].value == 0:
            self.label47.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][7].value == 1:
            self.label47.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][7].value == 2:
            self.label47.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[4][7].cost)
            if self.matrix[4][7].cost == '11.1+11.1\n11.1':
                self.label47.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][7].value == 3:
            self.label47.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[4][7].cost)
            if self.matrix[4][7].cost == '11.1+11.1\n11.1':
                self.label47.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[4][7].value == 4:
            self.label47.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[4][7].cost)
        elif self.matrix[4][7].value == 5:
            self.label47.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[4][7].cost)
        elif self.matrix[4][7].value == 9:
            self.label47.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[4][7].cost)

        # Node 50
        if self.matrix[5][0].value == 0:
            self.label50.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][0].value == 1:
            self.label50.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][0].value == 2:
            self.label50.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[5][0].cost)
            if self.matrix[5][0].cost == '11.1+11.1\n11.1':
                self.label50.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][0].value == 3:
            self.label50.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[5][0].cost)
            if self.matrix[5][0].cost == '11.1+11.1\n11.1':
                self.label50.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[5][0].value == 4:
            self.label50.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[5][0].cost)
        elif self.matrix[5][0].value == 5:
            self.label50.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[5][0].cost)
        elif self.matrix[5][0].value == 9:
            self.label50.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[5][0].cost)

        # Node 51
        if self.matrix[5][1].value == 0:
            self.label51.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][1].value == 1:
            self.label51.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][1].value == 2:
            self.label51.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[5][1].cost)
            if self.matrix[5][1].cost == '11.1+11.1\n11.1':
                self.label51.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][1].value == 3:
            self.label51.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[5][1].cost)
            if self.matrix[5][1].cost == '11.1+11.1\n11.1':
                self.label51.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[5][1].value == 4:
            self.label51.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[5][1].cost)
        elif self.matrix[5][1].value == 5:
            self.label51.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[5][1].cost)
        elif self.matrix[5][1].value == 9:
            self.label51.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[5][1].cost)

        # Node 52
        if self.matrix[5][2].value == 0:
            self.label52.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][2].value == 1:
            self.label52.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][2].value == 2:
            self.label52.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[5][2].cost)
            if self.matrix[5][2].cost == '11.1+11.1\n11.1':
                self.label52.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][2].value == 3:
            self.label52.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[5][2].cost)
            if self.matrix[5][2].cost == '11.1+11.1\n11.1':
                self.label52.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[5][2].value == 4:
            self.label52.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[5][2].cost)
        elif self.matrix[5][2].value == 5:
            self.label52.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[5][2].cost)
        elif self.matrix[5][2].value == 9:
            self.label52.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[5][2].cost)

        # Node 53
        if self.matrix[5][3].value == 0:
            self.label53.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][3].value == 1:
            self.label53.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][3].value == 2:
            self.label53.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[5][3].cost)
            if self.matrix[5][3].cost == '11.1+11.1\n11.1':
                self.label53.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][3].value == 3:
            self.label53.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[5][3].cost)
            if self.matrix[5][3].cost == '11.1+11.1\n11.1':
                self.label53.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[5][3].value == 4:
            self.label53.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[5][3].cost)
        elif self.matrix[5][3].value == 5:
            self.label53.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[5][3].cost)
        elif self.matrix[5][3].value == 9:
            self.label53.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[5][3].cost)

        # Node 54
        if self.matrix[5][4].value == 0:
            self.label54.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][4].value == 1:
            self.label54.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][4].value == 2:
            self.label54.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[5][4].cost)
            if self.matrix[5][4].cost == '11.1+11.1\n11.1':
                self.label54.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][4].value == 3:
            self.label54.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[5][4].cost)
            if self.matrix[5][4].cost == '11.1+11.1\n11.1':
                self.label54.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[5][4].value == 4:
            self.label54.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[5][4].cost)
        elif self.matrix[5][4].value == 5:
            self.label54.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[5][4].cost)
        elif self.matrix[5][4].value == 9:
            self.label54.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[5][4].cost)

        # Node 55
        if self.matrix[5][5].value == 0:
            self.label55.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][5].value == 1:
            self.label55.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][5].value == 2:
            self.label55.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[5][5].cost)
            if self.matrix[5][5].cost == '11.1+11.1\n11.1':
                self.label55.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][5].value == 3:
            self.label55.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[5][5].cost)
            if self.matrix[5][5].cost == '11.1+11.1\n11.1':
                self.label55.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[5][5].value == 4:
            self.label55.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[5][5].cost)
        elif self.matrix[5][5].value == 5:
            self.label55.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[5][5].cost)
        elif self.matrix[5][5].value == 9:
            self.label55.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[5][5].cost)

        # Node 56
        if self.matrix[5][6].value == 0:
            self.label56.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][6].value == 1:
            self.label56.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][6].value == 2:
            self.label56.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[5][6].cost)
            if self.matrix[5][6].cost == '11.1+11.1\n11.1':
                self.label56.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][6].value == 3:
            self.label56.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[5][6].cost)
            if self.matrix[5][6].cost == '11.1+11.1\n11.1':
                self.label56.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[5][6].value == 4:
            self.label56.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[5][6].cost)
        elif self.matrix[5][6].value == 5:
            self.label56.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[5][6].cost)
        elif self.matrix[5][6].value == 9:
            self.label56.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[5][6].cost)

        # Node 57
        if self.matrix[5][7].value == 0:
            self.label57.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][7].value == 1:
            self.label57.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][7].value == 2:
            self.label57.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[5][7].cost)
            if self.matrix[5][7].cost == '11.1+11.1\n11.1':
                self.label57.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][7].value == 3:
            self.label57.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[5][7].cost)
            if self.matrix[5][7].cost == '11.1+11.1\n11.1':
                self.label57.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[5][7].value == 4:
            self.label57.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[5][7].cost)
        elif self.matrix[5][7].value == 5:
            self.label57.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[5][7].cost)
        elif self.matrix[5][7].value == 9:
            self.label57.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[5][7].cost)

        # Node 60
        if self.matrix[6][0].value == 0:
            self.label60.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][0].value == 1:
            self.label60.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][0].value == 2:
            self.label60.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[6][0].cost)
            if self.matrix[6][0].cost == '11.1+11.1\n11.1':
                self.label60.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][0].value == 3:
            self.label60.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[6][0].cost)
            if self.matrix[6][0].cost == '11.1+11.1\n11.1':
                self.label60.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[6][0].value == 4:
            self.label60.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[6][0].cost)
        elif self.matrix[6][0].value == 5:
            self.label60.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[6][0].cost)
        elif self.matrix[6][0].value == 9:
            self.label60.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[6][0].cost)

        # Node 61
        if self.matrix[6][1].value == 0:
            self.label61.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][1].value == 1:
            self.label61.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][1].value == 2:
            self.label61.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[6][1].cost)
            if self.matrix[6][1].cost == '11.1+11.1\n11.1':
                self.label61.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][1].value == 3:
            self.label61.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[6][1].cost)
            if self.matrix[6][1].cost == '11.1+11.1\n11.1':
                self.label61.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[6][1].value == 4:
            self.label61.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[6][1].cost)
        elif self.matrix[6][1].value == 5:
            self.label61.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[6][1].cost)
        elif self.matrix[6][1].value == 9:
            self.label61.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[6][1].cost)

        # Node 62
        if self.matrix[6][2].value == 0:
            self.label62.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][2].value == 1:
            self.label62.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][2].value == 2:
            self.label62.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[6][2].cost)
            if self.matrix[6][2].cost == '11.1+11.1\n11.1':
                self.label62.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][2].value == 3:
            self.label62.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[6][2].cost)
            if self.matrix[6][2].cost == '11.1+11.1\n11.1':
                self.label62.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[6][2].value == 4:
            self.label62.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[6][2].cost)
        elif self.matrix[6][2].value == 5:
            self.label62.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[6][2].cost)
        elif self.matrix[6][2].value == 9:
            self.label62.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[6][2].cost)

        # Node 63
        if self.matrix[6][3].value == 0:
            self.label63.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][3].value == 1:
            self.label63.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][3].value == 2:
            self.label63.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[6][3].cost)
            if self.matrix[6][3].cost == '11.1+11.1\n11.1':
                self.label63.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][3].value == 3:
            self.label63.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[6][3].cost)
            if self.matrix[6][3].cost == '11.1+11.1\n11.1':
                self.label63.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[6][3].value == 4:
            self.label63.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[6][3].cost)
        elif self.matrix[6][3].value == 5:
            self.label63.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[6][3].cost)
        elif self.matrix[6][3].value == 9:
            self.label63.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[6][3].cost)

        # Node 64
        if self.matrix[6][4].value == 0:
            self.label64.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][4].value == 1:
            self.label64.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][4].value == 2:
            self.label64.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[6][4].cost)
            if self.matrix[6][4].cost == '11.1+11.1\n11.1':
                self.label64.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][4].value == 3:
            self.label64.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[6][4].cost)
            if self.matrix[6][4].cost == '11.1+11.1\n11.1':
                self.label64.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[6][4].value == 4:
            self.label64.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[6][4].cost)
        elif self.matrix[6][4].value == 5:
            self.label64.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[6][4].cost)
        elif self.matrix[6][4].value == 9:
            self.label64.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[6][4].cost)

        # Node 65
        if self.matrix[6][5].value == 0:
            self.label65.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][5].value == 1:
            self.label65.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][5].value == 2:
            self.label65.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[6][5].cost)
            if self.matrix[6][5].cost == '11.1+11.1\n11.1':
                self.label65.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][5].value == 3:
            self.label65.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[6][5].cost)
            if self.matrix[6][5].cost == '11.1+11.1\n11.1':
                self.label65.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[6][5].value == 4:
            self.label65.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[6][5].cost)
        elif self.matrix[6][5].value == 5:
            self.label65.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[6][5].cost)
        elif self.matrix[6][5].value == 9:
            self.label65.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[6][5].cost)

        # Node 66
        if self.matrix[6][6].value == 0:
            self.label66.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][6].value == 1:
            self.label66.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][6].value == 2:
            self.label66.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[6][6].cost)
            if self.matrix[6][6].cost == '11.1+11.1\n11.1':
                self.label66.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][6].value == 3:
            self.label66.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[6][6].cost)
            if self.matrix[6][6].cost == '11.1+11.1\n11.1':
                self.label66.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[6][6].value == 4:
            self.label66.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[6][6].cost)
        elif self.matrix[6][6].value == 5:
            self.label66.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[6][6].cost)
        elif self.matrix[6][6].value == 9:
            self.label66.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[6][6].cost)

        # Node 67
        if self.matrix[6][7].value == 0:
            self.label67.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][7].value == 1:
            self.label67.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][7].value == 2:
            self.label67.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[6][7].cost)
            if self.matrix[6][7].cost == '11.1+11.1\n11.1':
                self.label67.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][7].value == 3:
            self.label67.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[6][7].cost)
            if self.matrix[6][7].cost == '11.1+11.1\n11.1':
                self.label67.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[6][7].value == 4:
            self.label67.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[6][7].cost)
        elif self.matrix[6][7].value == 5:
            self.label67.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[6][7].cost)
        elif self.matrix[6][7].value == 9:
            self.label67.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[6][7].cost)

        # Node 70
        if self.matrix[7][0].value == 0:
            self.label70.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][0].value == 1:
            self.label70.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][0].value == 2:
            self.label70.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[7][0].cost)
            if self.matrix[7][0].cost == '11.1+11.1\n11.1':
                self.label70.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][0].value == 3:
            self.label70.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[7][0].cost)
            if self.matrix[7][0].cost == '11.1+11.1\n11.1':
                self.label70.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[7][0].value == 4:
            self.label70.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[7][0].cost)
        elif self.matrix[7][0].value == 5:
            self.label70.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[7][0].cost)
        elif self.matrix[7][0].value == 9:
            self.label70.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[7][0].cost)

        # Node 71
        if self.matrix[7][1].value == 0:
            self.label71.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][1].value == 1:
            self.label71.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][1].value == 2:
            self.label71.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[7][1].cost)
            if self.matrix[7][1].cost == '11.1+11.1\n11.1':
                self.label71.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][1].value == 3:
            self.label71.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[7][1].cost)
            if self.matrix[7][1].cost == '11.1+11.1\n11.1':
                self.label71.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[7][1].value == 4:
            self.label71.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[7][1].cost)
        elif self.matrix[7][1].value == 5:
            self.label71.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[7][1].cost)
        elif self.matrix[7][1].value == 9:
            self.label71.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[7][1].cost)

        # Node 72
        if self.matrix[7][2].value == 0:
            self.label72.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][2].value == 1:
            self.label72.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][2].value == 2:
            self.label72.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[7][2].cost)
            if self.matrix[7][2].cost == '11.1+11.1\n11.1':
                self.label72.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][2].value == 3:
            self.label72.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[7][2].cost)
            if self.matrix[7][2].cost == '11.1+11.1\n11.1':
                self.label72.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[7][2].value == 4:
            self.label72.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[7][2].cost)
        elif self.matrix[7][2].value == 5:
            self.label72.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[7][2].cost)
        elif self.matrix[7][2].value == 9:
            self.label72.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[7][2].cost)

        # Node 73
        if self.matrix[7][3].value == 0:
            self.label73.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][3].value == 1:
            self.label73.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][3].value == 2:
            self.label73.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[7][3].cost)
            if self.matrix[7][3].cost == '11.1+11.1\n11.1':
                self.label73.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][3].value == 3:
            self.label73.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[7][3].cost)
            if self.matrix[7][3].cost == '11.1+11.1\n11.1':
                self.label73.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[7][3].value == 4:
            self.label73.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[7][3].cost)
        elif self.matrix[7][3].value == 5:
            self.label73.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[7][3].cost)
        elif self.matrix[7][3].value == 9:
            self.label73.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[7][3].cost)

        # Node 74
        if self.matrix[7][4].value == 0:
            self.label74.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][4].value == 1:
            self.label74.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][4].value == 2:
            self.label74.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[7][4].cost)
            if self.matrix[7][4].cost == '11.1+11.1\n11.1':
                self.label74.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][4].value == 3:
            self.label74.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[7][4].cost)
            if self.matrix[7][4].cost == '11.1+11.1\n11.1':
                self.label74.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[7][4].value == 4:
            self.label74.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[7][4].cost)
        elif self.matrix[7][4].value == 5:
            self.label74.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[7][4].cost)
        elif self.matrix[7][4].value == 9:
            self.label74.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[7][4].cost)

        # Node 75
        if self.matrix[7][5].value == 0:
            self.label75.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][5].value == 1:
            self.label75.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][5].value == 2:
            self.label75.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[7][5].cost)
            if self.matrix[7][5].cost == '11.1+11.1\n11.1':
                self.label75.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][5].value == 3:
            self.label75.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[7][5].cost)
            if self.matrix[7][5].cost == '11.1+11.1\n11.1':
                self.label75.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[7][5].value == 4:
            self.label75.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[7][5].cost)
        elif self.matrix[7][5].value == 5:
            self.label75.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[7][5].cost)
        elif self.matrix[7][5].value == 9:
            self.label75.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[7][5].cost)

        # Node 76
        if self.matrix[7][6].value == 0:
            self.label76.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][6].value == 1:
            self.label76.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][6].value == 2:
            self.label76.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[7][6].cost)
            if self.matrix[7][6].cost == '11.1+11.1\n11.1':
                self.label76.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][6].value == 3:
            self.label76.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[7][6].cost)
            if self.matrix[7][6].cost == '11.1+11.1\n11.1':
                self.label76.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[7][6].value == 4:
            self.label76.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[7][6].cost)
        elif self.matrix[7][6].value == 5:
            self.label76.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[7][6].cost)
        elif self.matrix[7][6].value == 9:
            self.label76.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[7][6].cost)

        # Node 77
        if self.matrix[7][7].value == 0:
            self.label77.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][7].value == 1:
            self.label77.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][7].value == 2:
            self.label77.configure(bg=self.START_COLOUR, fg=START_FONT_COLOUR, text=self.matrix[7][7].cost)
            if self.matrix[7][7].cost == '11.1+11.1\n11.1':
                self.label77.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][7].value == 3:
            self.label77.configure(bg=self.END_COLOUR, fg=END_FONT_COLOUR, text=self.matrix[7][7].cost)
            if self.matrix[7][7].cost == '11.1+11.1\n11.1':
                self.label77.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
        elif self.matrix[7][7].value == 4:
            self.label77.configure(bg=OPEN_COLOUR, fg=OPEN_FONT_COLOUR, text=self.matrix[7][7].cost)
        elif self.matrix[7][7].value == 5:
            self.label77.configure(bg=PATH_COLOUR, fg=PATH_FONT_COLOUR, text=self.matrix[7][7].cost)
        elif self.matrix[7][7].value == 9:
            self.label77.configure(bg=FRONTIER_COLOUR, fg=FRONTIER_FONT_COLOUR, text=self.matrix[7][7].cost)

    def change_value(self, event):
        self.matrix[0][0].value = (self.matrix[0][0].value + 1) % 4
        # self.label00.config(text=self.matrix[0][0].value)
        if self.matrix[0][0].value == 0:
            self.label00.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][0].value == 1:
            self.label00.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][0].value == 2:
            self.label00.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][0].value == 3:
            self.label00.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_01(self, event):
        self.matrix[0][1].value = (self.matrix[0][1].value + 1) % 4
        # # self.label01.config(text=self.matrix[0][1].value)
        if self.matrix[0][1].value == 0:
            self.label01.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][1].value == 1:
            self.label01.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][1].value == 2:
            self.label01.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][1].value == 3:
            self.label01.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_02(self, event):
        self.matrix[0][2].value = (self.matrix[0][2].value + 1) % 4
        # # self.label02.config(text=self.matrix[0][2].value)
        if self.matrix[0][2].value == 0:
            self.label02.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][2].value == 1:
            self.label02.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][2].value == 2:
            self.label02.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][2].value == 3:
            self.label02.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_03(self, event):
        self.matrix[0][3].value = (self.matrix[0][3].value + 1) % 4
        # self.label03.config(text=self.matrix[0][3].value)
        if self.matrix[0][3].value == 0:
            self.label03.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][3].value == 1:
            self.label03.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][3].value == 2:
            self.label03.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][3].value == 3:
            self.label03.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_04(self, event):
        self.matrix[0][4].value = (self.matrix[0][4].value + 1) % 4
        # self.label04.config(text=self.matrix[0][4].value)
        if self.matrix[0][4].value == 0:
            self.label04.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][4].value == 1:
            self.label04.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][4].value == 2:
            self.label04.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][4].value == 3:
            self.label04.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_05(self, event):
        self.matrix[0][5].value = (self.matrix[0][5].value + 1) % 4
        # self.label05.config(text=self.matrix[0][5].value)
        if self.matrix[0][5].value == 0:
            self.label05.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][5].value == 1:
            self.label05.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][5].value == 2:
            self.label05.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][5].value == 3:
            self.label05.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_06(self, event):
        self.matrix[0][6].value = (self.matrix[0][6].value + 1) % 4
        # self.label06.config(text=self.matrix[0][6].value)
        if self.matrix[0][6].value == 0:
            self.label06.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][6].value == 1:
            self.label06.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][6].value == 2:
            self.label06.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][6].value == 3:
            self.label06.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_07(self, event):
        self.matrix[0][7].value = (self.matrix[0][7].value + 1) % 4
        # self.label07.config(text=self.matrix[0][7].value)
        if self.matrix[0][7].value == 0:
            self.label07.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[0][7].value == 1:
            self.label07.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[0][7].value == 2:
            self.label07.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[0][7].value == 3:
            self.label07.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_10(self, event):
        self.matrix[1][0].value = (self.matrix[1][0].value + 1) % 4
        # self.label10.config(text=self.matrix[1][0].value)
        if self.matrix[1][0].value == 0:
            self.label10.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][0].value == 1:
            self.label10.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][0].value == 2:
            self.label10.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][0].value == 3:
            self.label10.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_11(self, event):
        self.matrix[1][1].value = (self.matrix[1][1].value + 1) % 4
        # self.label11.config(text=self.matrix[1][1].value)
        if self.matrix[1][1].value == 0:
            self.label11.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][1].value == 1:
            self.label11.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][1].value == 2:
            self.label11.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][1].value == 3:
            self.label11.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_12(self, event):
        self.matrix[1][2].value = (self.matrix[1][2].value + 1) % 4
        # self.label12.config(text=self.matrix[1][2].value)
        if self.matrix[1][2].value == 0:
            self.label12.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][2].value == 1:
            self.label12.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][2].value == 2:
            self.label12.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][2].value == 3:
            self.label12.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_13(self, event):
        self.matrix[1][3].value = (self.matrix[1][3].value + 1) % 4
        # self.label13.config(text=self.matrix[1][3].value)
        if self.matrix[1][3].value == 0:
            self.label13.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][3].value == 1:
            self.label13.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][3].value == 2:
            self.label13.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][3].value == 3:
            self.label13.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_14(self, event):
        self.matrix[1][4].value = (self.matrix[1][4].value + 1) % 4
        # self.label14.config(text=self.matrix[1][4].value)
        if self.matrix[1][4].value == 0:
            self.label14.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][4].value == 1:
            self.label14.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][4].value == 2:
            self.label14.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][4].value == 3:
            self.label14.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_15(self, event):
        self.matrix[1][5].value = (self.matrix[1][5].value + 1) % 4
        # self.label15.config(text=self.matrix[1][5].value)
        if self.matrix[1][5].value == 0:
            self.label15.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][5].value == 1:
            self.label15.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][5].value == 2:
            self.label15.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][5].value == 3:
            self.label15.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_16(self, event):
        self.matrix[1][6].value = (self.matrix[1][6].value + 1) % 4
        # self.label16.config(text=self.matrix[1][6].value)
        if self.matrix[1][6].value == 0:
            self.label16.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][6].value == 1:
            self.label16.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][6].value == 2:
            self.label16.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][6].value == 3:
            self.label16.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_17(self, event):
        self.matrix[1][7].value = (self.matrix[1][7].value + 1) % 4
        # self.label17.config(text=self.matrix[1][7].value)
        if self.matrix[1][7].value == 0:
            self.label17.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[1][7].value == 1:
            self.label17.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[1][7].value == 2:
            self.label17.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[1][7].value == 3:
            self.label17.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_20(self, event):
        self.matrix[2][0].value = (self.matrix[2][0].value + 1) % 4
        # self.label20.config(text=self.matrix[2][0].value)
        if self.matrix[2][0].value == 0:
            self.label20.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][0].value == 1:
            self.label20.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][0].value == 2:
            self.label20.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][0].value == 3:
            self.label20.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_21(self, event):
        self.matrix[2][1].value = (self.matrix[2][1].value + 1) % 4
        # self.label21.config(text=self.matrix[2][1].value)
        if self.matrix[2][1].value == 0:
            self.label21.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][1].value == 1:
            self.label21.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][1].value == 2:
            self.label21.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][1].value == 3:
            self.label21.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_22(self, event):
        self.matrix[2][2].value = (self.matrix[2][2].value + 1) % 4
        # self.label22.config(text=self.matrix[2][2].value)
        if self.matrix[2][2].value == 0:
            self.label22.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][2].value == 1:
            self.label22.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][2].value == 2:
            self.label22.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][2].value == 3:
            self.label22.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_23(self, event):
        self.matrix[2][3].value = (self.matrix[2][3].value + 1) % 4
        # self.label23.config(text=self.matrix[2][3].value)
        if self.matrix[2][3].value == 0:
            self.label23.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][3].value == 1:
            self.label23.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][3].value == 2:
            self.label23.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][3].value == 3:
            self.label23.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_24(self, event):
        self.matrix[2][4].value = (self.matrix[2][4].value + 1) % 4
        # self.label24.config(text=self.matrix[2][4].value)
        if self.matrix[2][4].value == 0:
            self.label24.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][4].value == 1:
            self.label24.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][4].value == 2:
            self.label24.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][4].value == 3:
            self.label24.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_25(self, event):
        self.matrix[2][5].value = (self.matrix[2][5].value + 1) % 4
        # self.label25.config(text=self.matrix[2][5].value)
        if self.matrix[2][5].value == 0:
            self.label25.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][5].value == 1:
            self.label25.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][5].value == 2:
            self.label25.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][5].value == 3:
            self.label25.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_26(self, event):
        self.matrix[2][6].value = (self.matrix[2][6].value + 1) % 4
        # self.label26.config(text=self.matrix[2][6].value)
        if self.matrix[2][6].value == 0:
            self.label26.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][6].value == 1:
            self.label26.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][6].value == 2:
            self.label26.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][6].value == 3:
            self.label26.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_27(self, event):
        self.matrix[2][7].value = (self.matrix[2][7].value + 1) % 4
        # self.label27.config(text=self.matrix[2][7].value)
        if self.matrix[2][7].value == 0:
            self.label27.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[2][7].value == 1:
            self.label27.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[2][7].value == 2:
            self.label27.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[2][7].value == 3:
            self.label27.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_30(self, event):
        self.matrix[3][0].value = (self.matrix[3][0].value + 1) % 4
        # self.label30.config(text=self.matrix[3][0].value)
        if self.matrix[3][0].value == 0:
            self.label30.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][0].value == 1:
            self.label30.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][0].value == 2:
            self.label30.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][0].value == 3:
            self.label30.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_31(self, event):
        self.matrix[3][1].value = (self.matrix[3][1].value + 1) % 4
        # self.label31.config(text=self.matrix[3][1].value)
        if self.matrix[3][1].value == 0:
            self.label31.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][1].value == 1:
            self.label31.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][1].value == 2:
            self.label31.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][1].value == 3:
            self.label31.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_32(self, event):
        self.matrix[3][2].value = (self.matrix[3][2].value + 1) % 4
        # self.label32.config(text=self.matrix[3][2].value)
        if self.matrix[3][2].value == 0:
            self.label32.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][2].value == 1:
            self.label32.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][2].value == 2:
            self.label32.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][2].value == 3:
            self.label32.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_33(self, event):
        self.matrix[3][3].value = (self.matrix[3][3].value + 1) % 4
        # self.label33.config(text=self.matrix[3][3].value)
        if self.matrix[3][3].value == 0:
            self.label33.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][3].value == 1:
            self.label33.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][3].value == 2:
            self.label33.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][3].value == 3:
            self.label33.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_34(self, event):
        self.matrix[3][4].value = (self.matrix[3][4].value + 1) % 4
        # self.label34.config(text=self.matrix[3][4].value)
        if self.matrix[3][4].value == 0:
            self.label34.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][4].value == 1:
            self.label34.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][4].value == 2:
            self.label34.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][4].value == 3:
            self.label34.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_35(self, event):
        self.matrix[3][5].value = (self.matrix[3][5].value + 1) % 4
        # self.label35.config(text=self.matrix[3][5].value)
        if self.matrix[3][5].value == 0:
            self.label35.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][5].value == 1:
            self.label35.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][5].value == 2:
            self.label35.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][5].value == 3:
            self.label35.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_36(self, event):
        self.matrix[3][6].value = (self.matrix[3][6].value + 1) % 4
        # self.label36.config(text=self.matrix[3][6].value)
        if self.matrix[3][6].value == 0:
            self.label36.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][6].value == 1:
            self.label36.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][6].value == 2:
            self.label36.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][6].value == 3:
            self.label36.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_37(self, event):
        self.matrix[3][7].value = (self.matrix[3][7].value + 1) % 4
        # self.label37.config(text=self.matrix[3][7].value)
        if self.matrix[3][7].value == 0:
            self.label37.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[3][7].value == 1:
            self.label37.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[3][7].value == 2:
            self.label37.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[3][7].value == 3:
            self.label37.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_40(self, event):
        self.matrix[4][0].value = (self.matrix[4][0].value + 1) % 4
        # self.label40.config(text=self.matrix[4][0].value)
        if self.matrix[4][0].value == 0:
            self.label40.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][0].value == 1:
            self.label40.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][0].value == 2:
            self.label40.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][0].value == 3:
            self.label40.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_41(self, event):
        self.matrix[4][1].value = (self.matrix[4][1].value + 1) % 4
        # self.label41.config(text=self.matrix[4][1].value)
        if self.matrix[4][1].value == 0:
            self.label41.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][1].value == 1:
            self.label41.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][1].value == 2:
            self.label41.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][1].value == 3:
            self.label41.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_42(self, event):
        self.matrix[4][2].value = (self.matrix[4][2].value + 1) % 4
        # self.label42.config(text=self.matrix[4][2].value)
        if self.matrix[4][2].value == 0:
            self.label42.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][2].value == 1:
            self.label42.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][2].value == 2:
            self.label42.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][2].value == 3:
            self.label42.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_43(self, event):
        self.matrix[4][3].value = (self.matrix[4][3].value + 1) % 4
        # self.label43.config(text=self.matrix[4][3].value)
        if self.matrix[4][3].value == 0:
            self.label43.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][3].value == 1:
            self.label43.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][3].value == 2:
            self.label43.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][3].value == 3:
            self.label43.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_44(self, event):
        self.matrix[4][4].value = (self.matrix[4][4].value + 1) % 4
        # self.label44.config(text=self.matrix[4][4].value)
        if self.matrix[4][4].value == 0:
            self.label44.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][4].value == 1:
            self.label44.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][4].value == 2:
            self.label44.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][4].value == 3:
            self.label44.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_45(self, event):
        self.matrix[4][5].value = (self.matrix[4][5].value + 1) % 4
        # self.label45.config(text=self.matrix[4][5].value)
        if self.matrix[4][5].value == 0:
            self.label45.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][5].value == 1:
            self.label45.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][5].value == 2:
            self.label45.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][5].value == 3:
            self.label45.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_46(self, event):
        self.matrix[4][6].value = (self.matrix[4][6].value + 1) % 4
        # self.label46.config(text=self.matrix[4][6].value)
        if self.matrix[4][6].value == 0:
            self.label46.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][6].value == 1:
            self.label46.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][6].value == 2:
            self.label46.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][6].value == 3:
            self.label46.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_47(self, event):
        self.matrix[4][7].value = (self.matrix[4][7].value + 1) % 4
        # self.label47.config(text=self.matrix[4][7].value)
        if self.matrix[4][7].value == 0:
            self.label47.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[4][7].value == 1:
            self.label47.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[4][7].value == 2:
            self.label47.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[4][7].value == 3:
            self.label47.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_50(self, event):
        self.matrix[5][0].value = (self.matrix[5][0].value + 1) % 4
        # self.label50.config(text=self.matrix[5][0].value)
        if self.matrix[5][0].value == 0:
            self.label50.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][0].value == 1:
            self.label50.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][0].value == 2:
            self.label50.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][0].value == 3:
            self.label50.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_51(self, event):
        self.matrix[5][1].value = (self.matrix[5][1].value + 1) % 4
        # self.label51.config(text=self.matrix[5][1].value)
        if self.matrix[5][1].value == 0:
            self.label51.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][1].value == 1:
            self.label51.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][1].value == 2:
            self.label51.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][1].value == 3:
            self.label51.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_52(self, event):
        self.matrix[5][2].value = (self.matrix[5][2].value + 1) % 4
        # self.label52.config(text=self.matrix[5][2].value)
        if self.matrix[5][2].value == 0:
            self.label52.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][2].value == 1:
            self.label52.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][2].value == 2:
            self.label52.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][2].value == 3:
            self.label52.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_53(self, event):
        self.matrix[5][3].value = (self.matrix[5][3].value + 1) % 4
        # self.label53.config(text=self.matrix[5][3].value)
        if self.matrix[5][3].value == 0:
            self.label53.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][3].value == 1:
            self.label53.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][3].value == 2:
            self.label53.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][3].value == 3:
            self.label53.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_54(self, event):
        self.matrix[5][4].value = (self.matrix[5][4].value + 1) % 4
        # self.label54.config(text=self.matrix[5][4].value)
        if self.matrix[5][4].value == 0:
            self.label54.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][4].value == 1:
            self.label54.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][4].value == 2:
            self.label54.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][4].value == 3:
            self.label54.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_55(self, event):
        self.matrix[5][5].value = (self.matrix[5][5].value + 1) % 4
        # self.label55.config(text=self.matrix[5][5].value)
        if self.matrix[5][5].value == 0:
            self.label55.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][5].value == 1:
            self.label55.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][5].value == 2:
            self.label55.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][5].value == 3:
            self.label55.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_56(self, event):
        self.matrix[5][6].value = (self.matrix[5][6].value + 1) % 4
        # self.label56.config(text=self.matrix[5][6].value)
        if self.matrix[5][6].value == 0:
            self.label56.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][6].value == 1:
            self.label56.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][6].value == 2:
            self.label56.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][6].value == 3:
            self.label56.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_57(self, event):
        self.matrix[5][7].value = (self.matrix[5][7].value + 1) % 4
        # self.label57.config(text=self.matrix[5][7].value)
        if self.matrix[5][7].value == 0:
            self.label57.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[5][7].value == 1:
            self.label57.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[5][7].value == 2:
            self.label57.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[5][7].value == 3:
            self.label57.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_60(self, event):
        self.matrix[6][0].value = (self.matrix[6][0].value + 1) % 4
        # self.label60.config(text=self.matrix[6][0].value)
        if self.matrix[6][0].value == 0:
            self.label60.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][0].value == 1:
            self.label60.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][0].value == 2:
            self.label60.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][0].value == 3:
            self.label60.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_61(self, event):
        self.matrix[6][1].value = (self.matrix[6][1].value + 1) % 4
        # self.label61.config(text=self.matrix[6][1].value)
        if self.matrix[6][1].value == 0:
            self.label61.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][1].value == 1:
            self.label61.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][1].value == 2:
            self.label61.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][1].value == 3:
            self.label61.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_62(self, event):
        self.matrix[6][2].value = (self.matrix[6][2].value + 1) % 4
        # self.label62.config(text=self.matrix[6][2].value)
        if self.matrix[6][2].value == 0:
            self.label62.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][2].value == 1:
            self.label62.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][2].value == 2:
            self.label62.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][2].value == 3:
            self.label62.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_63(self, event):
        self.matrix[6][3].value = (self.matrix[6][3].value + 1) % 4
        # self.label63.config(text=self.matrix[6][3].value)
        if self.matrix[6][3].value == 0:
            self.label63.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][3].value == 1:
            self.label63.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][3].value == 2:
            self.label63.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][3].value == 3:
            self.label63.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_64(self, event):
        self.matrix[6][4].value = (self.matrix[6][4].value + 1) % 4
        # self.label64.config(text=self.matrix[6][4].value)
        if self.matrix[6][4].value == 0:
            self.label64.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][4].value == 1:
            self.label64.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][4].value == 2:
            self.label64.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][4].value == 3:
            self.label64.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_65(self, event):
        self.matrix[6][5].value = (self.matrix[6][5].value + 1) % 4
        # self.label65.config(text=self.matrix[6][5].value)
        if self.matrix[6][5].value == 0:
            self.label65.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][5].value == 1:
            self.label65.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][5].value == 2:
            self.label65.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][5].value == 3:
            self.label65.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_66(self, event):
        self.matrix[6][6].value = (self.matrix[6][6].value + 1) % 4
        # self.label66.config(text=self.matrix[6][6].value)
        if self.matrix[6][6].value == 0:
            self.label66.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][6].value == 1:
            self.label66.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][6].value == 2:
            self.label66.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][6].value == 3:
            self.label66.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_67(self, event):
        self.matrix[6][7].value = (self.matrix[6][7].value + 1) % 4
        # self.label67.config(text=self.matrix[6][7].value)
        if self.matrix[6][7].value == 0:
            self.label67.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[6][7].value == 1:
            self.label67.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[6][7].value == 2:
            self.label67.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[6][7].value == 3:
            self.label67.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_70(self, event):
        self.matrix[7][0].value = (self.matrix[7][0].value + 1) % 4
        # self.label70.config(text=self.matrix[7][0].value)
        if self.matrix[7][0].value == 0:
            self.label70.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][0].value == 1:
            self.label70.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][0].value == 2:
            self.label70.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][0].value == 3:
            self.label70.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_71(self, event):
        self.matrix[7][1].value = (self.matrix[7][1].value + 1) % 4
        # self.label71.config(text=self.matrix[7][1].value)
        if self.matrix[7][1].value == 0:
            self.label71.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][1].value == 1:
            self.label71.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][1].value == 2:
            self.label71.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][1].value == 3:
            self.label71.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_72(self, event):
        self.matrix[7][2].value = (self.matrix[7][2].value + 1) % 4
        # self.label72.config(text=self.matrix[7][2].value)
        if self.matrix[7][2].value == 0:
            self.label72.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][2].value == 1:
            self.label72.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][2].value == 2:
            self.label72.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][2].value == 3:
            self.label72.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_73(self, event):
        self.matrix[7][3].value = (self.matrix[7][3].value + 1) % 4
        # self.label73.config(text=self.matrix[7][3].value)
        if self.matrix[7][3].value == 0:
            self.label73.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][3].value == 1:
            self.label73.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][3].value == 2:
            self.label73.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][3].value == 3:
            self.label73.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_74(self, event):
        self.matrix[7][4].value = (self.matrix[7][4].value + 1) % 4
        # self.label74.config(text=self.matrix[7][4].value)
        if self.matrix[7][4].value == 0:
            self.label74.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][4].value == 1:
            self.label74.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][4].value == 2:
            self.label74.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][4].value == 3:
            self.label74.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_75(self, event):
        self.matrix[7][5].value = (self.matrix[7][5].value + 1) % 4
        # self.label75.config(text=self.matrix[7][5].value)
        if self.matrix[7][5].value == 0:
            self.label75.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][5].value == 1:
            self.label75.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][5].value == 2:
            self.label75.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][5].value == 3:
            self.label75.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_76(self, event):
        self.matrix[7][6].value = (self.matrix[7][6].value + 1) % 4
        # self.label76.config(text=self.matrix[7][6].value)
        if self.matrix[7][6].value == 0:
            self.label76.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][6].value == 1:
            self.label76.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][6].value == 2:
            self.label76.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][6].value == 3:
            self.label76.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)

    def change_value_77(self, event):
        self.matrix[7][7].value = (self.matrix[7][7].value + 1) % 4
        # self.label77.config(text=self.matrix[7][7].value)
        if self.matrix[7][7].value == 0:
            self.label77.configure(bg=self.NORMAL_COLOUR, fg=self.NORMAL_COLOUR)
        elif self.matrix[7][7].value == 1:
            self.label77.configure(bg=self.WALL_COLOUR, fg=self.WALL_COLOUR)
        elif self.matrix[7][7].value == 2:
            self.label77.configure(bg=self.START_COLOUR, fg=self.START_COLOUR)
        elif self.matrix[7][7].value == 3:
            self.label77.configure(bg=self.END_COLOUR, fg=self.END_COLOUR)
