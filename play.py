from tkinter import *
from tkinter.font import names

root = Tk()
root.title('Floot')
root.geometry('800x300')

font=('Helvetica', 15)

def clear_window():
    for widget in root.slaves():
        widget.destroy()

class IntroPage:

    def __init__(self):
        # Create widgets
        self.entry_text = Label(root, text="How many players?", font=font)
        self.entry_field = Entry(root, text="How many players?", font=font)
        self.submit_button = Button(root, text='Next', command=self.submit_num_players, padx=50, font=font)

        # Display widgets
        self.entry_text.pack()
        self.entry_field.pack()
        self.submit_button.pack()

    def submit_num_players(self):
        try:
            num_players = int(self.entry_field.get())
        except:
            num_players = 0

        print(num_players)

        clear_window()
        NamesPage(num_players)

class NamesPage:

    def __init__(self, num_players):
        self.num  = num_players
        self.entry_list = []

        names_title = Label(root, text='Enter Player Names', font=font)
        names_title.pack()

        for i in range(num_players):
            self.entry_list.append(Entry(root, width=50))
            self.entry_list[-1].insert(END, f'Player {i+1}')
            self.entry_list[-1].pack(pady=5)

        self.ready_button = Button(root, text='Ready!', command=self.submit_names, padx=50, font=font)
        self.ready_button.pack(pady=10)

    def submit_names(self):
        player_names = [self.entry_list[i].get() for i in range(self.num)]
        print(player_names)
        clear_window()


IntroPage()
root.mainloop()
