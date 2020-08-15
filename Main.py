import tkinter as tk
from tkinter import ttk
import sqlite3


class DiceThrower:
    def __init__(self):
        # Setting up connection to local database
        self.c = sqlite3.connect('Database.db')
        self.cursor = self.c.cursor()
        # Importing data from text
        """self.listclass = []
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
"""
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
        Start = tk.Button(Screen, text='Start', font=('Courier', 30, 'italic'),borderwidth=0, command=self.login)
        Start.configure(bg='white', fg='black', activebackground='black', activeforeground='white')
        Start.place(relx=0.43, rely=0.3, width=200)
        # Button to open the page
        Rules = tk.Button(Screen, text='Rules', font=('Courier', 30, 'italic'), command=self.game_rule)
        Rules.configure(bg='white', fg='black', activebackground='black',borderwidth=0, activeforeground='white')
        Rules.place(relx=0.43, rely=0.40, width=200)
        # Button to check all possible player and to see who has a password
        Player = tk.Button(Screen, text='Players', font=('Courier', 30, 'italic'), command=self.player_screen)
        Player.configure(bg='white', fg='black', activebackground='black', borderwidth=0,activeforeground='white')
        Player.place(relx=0.43, rely=0.50, width=200)
        # Button to quit Application
        Quit = tk.Button(Screen, text='Quit', font=('Courier', 30, 'italic'),borderwidth=0, command=Screen.destroy)
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

        for x in self.cursor.execute("SELECT * FROM player"):

            Data.insert('', x[0], text=x[0], values=(x[1], x[2]))

    def login(self):
        # Log in Screen for authentication
        logging = tk.Toplevel()
        logging.configure(background='black')
        logging.state('zoomed')
        logging.title('Log in ')
        logging.grab_set()

        # Frame to encapsulate the first player logins
        Framer = tk.Frame(logging)
        Framer.configure(background='black')
        Framer.place(relx=0.10, rely=0.05)
        # Second Frame to encapsulate the second player logins
        Framer2 = tk.Frame(logging)
        Framer2.configure(background='black')
        Framer2.place(relx=0.70, rely=0.05)
        # Third Frame for Start and Quit button
        Framer3 = tk.Frame(logging)
        Framer3.configure(background='black')
        Framer3.place(relx=0.45, rely=0.6)
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
        player2 = tk.Label(Framer2, text='Player 2', font=('System', 20), bg='black', fg='white')
        player2.pack()
        user2 = tk.Label(Framer2, text='Username', font=('System', 20), bg='black', fg='white')
        user2.pack(pady=(20, 0))
        player2_name = tk.Entry(Framer2, font=("Times New Roman", 20), show="*")
        player2_name.pack(ipadx=50, ipady=20, pady=(10, 30))
        pass2 = tk.Label(Framer2, text='Password', font=('System', 20), bg='black', fg='white')
        pass2.pack(pady=(0, 0))
        player2_pass = tk.Entry(Framer2, font=("Times New Roman", 20))
        player2_pass.pack(ipadx=50, ipady=20)

        # Begin Button
        Button = tk.Button(Framer3, text='Start', font=('System', 30), command=self.start, borderwidth=0, fg='white',
                           bg='black',
                           activeforeground='white', activebackground='black')
        Button.pack(pady=(10, 20))
        #Sign in Button
        SignIn = tk.Button(Framer3, text="Sign in", font=('System', 30), command=self.signing, borderwidth=0, fg='white',
                           bg='black',
                           activeforeground='white', activebackground='black')

        SignIn.pack(pady=(10,20))
        # Quit Button
        Quit = tk.Button(Framer3, text='Quit', font=('System', 30), command=logging.destroy, borderwidth=0, fg='white',
                         bg='black', activeforeground='white', activebackground='black')
        Quit.pack()

    def start(self):
        print('Stupid')

    def signing(self):
        #Sign up frame and some configuration
        signup = tk.Toplevel()
        signup.geometry('800x500')
        signup.configure(background='black')
        signup.grab_set()
        signup.title('Signup')
        signup.resizable(False,False)


        Frame = tk.Frame(signup, bg='black')
        Frame.place(relx=0.3,rely=0.2)

        userlabel = tk.Label(Frame, text="Who are you? (Limit 30)", bg='black', fg='white', font=("System", 20))
        userlabel.pack()

        userentry = tk.Entry(Frame,font=('System', 25))
        userentry.pack(pady=20)

        passlabel = tk.Label(Frame, text="Write your password (Limit 30)", bg='black', fg='white', font=("System", 20))
        passlabel.pack()
        passentry = tk.Entry(Frame,font=('System', 25), show="*")
        passentry.pack(pady=(20,0))

        #Signup button
        commit = tk.Button(Frame, text="Sign up", borderwidth=0, fg='white',
                         bg='black', activeforeground='white', activebackground='black',font=('System', 30), command=lambda : self.check(userentry.get(), passentry.get()))
        commit.pack(pady=(20,0))
    def check(self,username,password):
        if username == '' or password == '':
            Error = tk.Toplevel()
            Error.grab_set()
            tk.Label(Error, text="USERNAME AND/OR PASSWORD CAN'T BE EMPTY", fg='white', bg='black', font=('Arial', 50)).pack(fill=tk.BOTH)
            Error.after(2000, lambda : Error.destroy())
        else:
            nameList = []
            for x in self.cursor.execute(f"SELECT * FROM player"):
                nameList.append(x[1])
            if username not in nameList:
                Error = tk.Toplevel()
                Error.grab_set()
                tk.Label(Error, text="USERNAME IS NOT IN CURRENT DATABASE", fg='white', bg='black',
                         font=('Arial', 50)).pack(fill=tk.BOTH)
                Error.after(2000, lambda: Error.destroy())
            else:
                if len(password) > 30:
                    Error = tk.Toplevel()
                    Error.grab_set()
                    tk.Label(Error, text="PASSWORD IS TOO LONG", fg='white', bg='black',
                             font=('Arial', 50)).pack(fill=tk.BOTH)
                    Error.after(2000, lambda: Error.destroy())
                else:

Application = DiceThrower()
