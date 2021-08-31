from tkinter import *


class InstructionWindow:
    def __init__(self, master):
        master.title("Manual Instructions")
        master.geometry('700x240+810+790')
        self.window_open = True  # Window is now open
        self.master = master

        self.step_label = Label(self.master)
        self.step_number = 1  # Resetting step number
        self.instruction_label_1 = Label(self.master)
        self.instruction_label_2 = Label(self.master)
        self.instruction_label_3 = Label(self.master)
        self.instruction_label_4 = Label(self.master)

        self.draw_instruction()

    def draw_instruction(self):
        self.step_label.configure(text='STEP {}'.format(self.step_number), font=('Helvetica', 21, 'bold'))
        self.step_label.pack()
        self.instruction_label_1.configure(text='', font=('Helvetica', 16))
        self.instruction_label_1.pack()
        self.instruction_label_2.configure(text='', font=('Helvetica', 16))
        self.instruction_label_2.pack()
        self.instruction_label_3.configure(text='', font=('Helvetica', 16))
        self.instruction_label_3.pack()
        self.instruction_label_4.configure(text='', font=('Helvetica', 16))
        self.instruction_label_4.pack()

    def update_instructions(self, instruction_1, instruction_2, instruction_3, instruction_4):
        self.step_label.configure(text='STEP {}'.format(self.step_number))
        self.step_number += 1
        self.instruction_label_1.configure(text=instruction_1)
        self.instruction_label_2.configure(text=instruction_2)
        self.instruction_label_3.configure(text=instruction_3)
        self.instruction_label_4.configure(text=instruction_4)

    def close_window(self):
        self.master.destroy()
