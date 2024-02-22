from tkinter import Menu

class MenuBar:
    def __init__(self, parent):
        self.menu_bar = Menu(parent)

        # Define your menu items here
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=parent.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

    def new_file(self):
        # Add functionality for new file
        pass

    def open_file(self):
        # Add functionality for opening file
        pass

    def about(self):
        # Add functionality for about
        pass