import tkinter as tk
from tkinter import ttk


class DiceThrower:
    def __init__(self):
        # Importing data from text
        self.listclass = []
        with open('ClassList.txt') as f:
            for x in f.readlines():
                self.listclass.append(x.strip())
        self.Password = {}
        with open('Data_Login.txt') as f:
            for x in f.readlines():
                a = x.split(',')
                self.Password[a[0]] = a[1].strip()
        self.registration = {}
        for x in self.listclass:
            if x not in self.Password:
                self.registration[x] = 'unregistered'
            else:
                self.registration[x] = 'registered'

        # Starting Application and making it cover whole screen
        Screen = tk.Tk()
        Screen.title('Main Screen')
        Screen.state('zoomed')
        Screen.configure(background='grey')
        # Title to introduce the game
        Title = tk.Label(Screen, text='Welcome to Dicer Thrower', font=('Times New Roman', 50, 'bold'), fg='white')
        Title.configure(background='grey')
        Title.place(relx=0.3, rely=0.1)
        # Button to go to login page
        Start = tk.Button(Screen, text='Start', font=('Courier', 30, 'italic'), command=self.login)
        Start.configure(bg='white', fg='black', activebackground='black', activeforeground='white')
        Start.place(relx=0.43, rely=0.3, width=200)
        # Button to open the page
        Rules = tk.Button(Screen, text='Rules', font=('Courier', 30, 'italic'), command=self.game_rule)
        Rules.configure(bg='white', fg='black', activebackground='black', activeforeground='white')
        Rules.place(relx=0.43, rely=0.40, width=200)
        # Button to check all possible player and to see who has a password
        Player = tk.Button(Screen, text='Players', font=('Courier', 30, 'italic'), command=self.player_screen)
        Player.configure(bg='white', fg='black', activebackground='black', activeforeground='white')
        Player.place(relx=0.43, rely=0.50, width=200)
        # Button to quit Application
        Quit = tk.Button(Screen, text='Quit', font=('Courier', 30, 'italic'), command=Screen.destroy)
        Quit.place(relx=0.43, rely=0.60, width=200)

        Screen.mainloop()

        # Importing data from text files

    # Rules Screen
    def game_rule(self):
        # Create new Frame
        rules = tk.Toplevel()
        rules.title('Rules')
        rules.configure(background='black')
        # Focus attention to the frame so no spamming can occur
        rules.grab_set()
        rules.state('zoomed')

        # Where all the rules are inserted
        Title = tk.Label(rules, text='Rules', fg='white', font=('System', 60, 'bold'), bg='black')
        Title.place(relx=0.02, rely=0.02)

        First = tk.Label(rules, text="1. The points rolled on each player's dice are added to their score.", fg='white',
                         font=('System', 30), bg='black')
        First.place(relx=0.02, rely=0.1)

        Second = tk.Label(rules,
                          text="2. If the total is an even number, an additional 10 points are added to their score.",
                          fg='white',
                          font=('System', 30), bg='black')
        Second.place(relx=0.02, rely=0.15)

        Third = tk.Label(rules, text="3. If the total is an odd number, 5 points are subtracted from their score.",
                         fg='white',
                         font=('System', 30), bg='black')
        Third.place(relx=0.02, rely=0.20)

        Fourth = tk.Label(rules, text="4. The score of a player cannot go below 0 at any point.", fg='white',
                          font=('System', 30), bg='black')
        Fourth.place(relx=0.02, rely=0.25)

        Fifth = tk.Label(rules, text="5. The person with the highest score at the end of the 5 rounds wins.",
                         fg='white',
                         font=('System', 30), bg='black')
        Fifth.place(relx=0.02, rely=0.30)

        Sixth = tk.Label(rules,
                         text="6. If both players have the same score at the end of the 5 rounds, they each roll a die and whoever gets the highest score wins (this repeats until someone wins).",
                         fg='white',
                         font=('System', 30), bg='black', wraplength=1800, justify='left')
        Sixth.place(relx=0.02, rely=0.35)

        # Get rid of rules page
        Quit = tk.Button(rules, text='Go back', bg='black', fg='white', font=('System', 40, 'bold'), borderwidth=0,
                         activeforeground='white', activebackground='black', command=rules.destroy)
        Quit.place(relx=0.40, rely=0.8)

    def player_screen(self):
        # Creating Frame for simple player data (Name, registered)
        player = tk.Toplevel()
        player.state('zoomed')
        player.title('Players')
        player.configure(background='black')
        # Focus attention on Player Screen, so no spamming can occur
        player.grab_set()
        # Styling to make data easier to see
        style = ttk.Style()

        style.configure('Treeview.Heading', font=('Courier', 20, 'bold', 'italic'))
        style.configure('Treeview', font=('Courier', 15))

        # Button to destroy player page
        Quit = tk.Button(player, text='Go back', command=player.destroy)
        Quit.configure(font=('System', 50), borderwidth=0, background='black', foreground='white',
                       activeforeground='white', activebackground='black')
        Quit.place(relx=0.40, rely=0.8)

        # Creating table
        Data = ttk.Treeview(player, column=('#0', "#1"), height=15)
        # Giving headings to each column
        Data.heading('#0', text='Id')
        Data.heading('#1', text='Name')
        Data.heading('#2', text='Registered')
        # Position of the Table
        Data.place(relx=0.32, rely=0.3)

        # Inserting the data from text files into the table
        id = 1
        for x in self.registration:
            Data.insert('', id, text=id, values=(x, self.registration[x]))
            id += 1

    def login(self):
        # Log in Screen for authentication
        logging = tk.Toplevel()
        logging.configure(background='black')
        logging.state('zoomed')
        logging.title('Log in ')
        logging.grab_set()

        # Frame to encapsulate the log in section
        Framer = tk.Frame(logging)
        Framer.configure(background='black')
        Framer.place(relx=0.39, rely=0.1)
        # Player 1 login
        player1 = tk.Label(Framer, text='Player 1', font=('System', 20), bg='black', fg='white')
        player1.pack()
        user1 = tk.Label(Framer, text='Username', font=('System', 20), bg='black', fg='white')
        user1.pack(pady=(20, 0))
        player1_name = tk.Entry(Framer, font=("Times New Roman", 20))
        player1_name.pack(ipadx=50, ipady=20, pady=(10, 30))

        pass1 = tk.Label(Framer, text='Password', font=('System', 20), bg='black', fg='white')
        pass1.pack(pady=(0, 0))
        player1_pass = tk.Entry(Framer, font=("Times New Roman", 20), show='*')
        player1_pass.pack(ipadx=50, ipady=20, pady=(10, 50))

        # Player 2 login
        player2 = tk.Label(Framer, text='Player 2', font=('System', 20), bg='black', fg='white')
        player2.pack()
        player2_name = tk.Entry(Framer, font=("Times New Roman", 20), show="*")
        player2_name.pack(ipadx=50, ipady=20, pady=50)

        player2_pass = tk.Entry(Framer, font=("Times New Roman", 20))
        player2_pass.pack(ipadx=50, ipady=20)

Application = DiceThrower()
