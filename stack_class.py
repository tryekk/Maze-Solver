class Stack:
    def __init__(self):
        self.stack_items = []  # Creating list to store items

    def push(self, item):
        self.stack_items.append(item)  # Function to append items

    def pop(self):
        return self.stack_items.pop()  # Function to remove items

    @property
    def is_empty(self):
        return self.stack_items == []  # Returns contents of stack to be checked if empty
