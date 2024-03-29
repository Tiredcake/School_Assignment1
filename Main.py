import tkinter as tk
from tkinter import ttk
import sqlite3
import random as rand
from PIL import ImageTk, Image
from numpy import random
import tkinter.font as TkFont


class DiceThrower:
    def __init__(self):
        # Setting up connection to local database
        self.c = sqlite3.connect('Database.db')
        self.cursor = self.c.cursor()
        self.leaderboard = sqlite3.connect('Leaderboard.db')
        self.leadercursor = self.leaderboard.cursor()
        # Ready the list of name that can be used in the game
        self.nameList = []
        for x in self.cursor.execute(f"SELECT * FROM player"):
            self.nameList.append(x[1])

        # Starting Application and making it cover whole screen
        Screen = tk.Tk()
        Screen.attributes('-fullscreen', True)
        Screen.title('Main Screen')
        Screen.state('zoomed')
        Screen.configure(background='grey')
        # Title to introduce the game
        Title = tk.Label(Screen, text='Welcome to Dicer Thrower', font=('Times New Roman', 50, 'bold'), fg='white')
        Title.configure(background='grey')
        Title.place(relx=0.3, rely=0.1)
        # Button to go to login page
        Start = tk.Button(Screen, text='Start', font=('Courier', 30, 'italic'), borderwidth=0, command=self.login)
        Start.configure(bg='white', fg='black', activebackground='black', activeforeground='white')
        Start.place(relx=0.43, rely=0.3, width=280)
        # Button to open the page
        Rules = tk.Button(Screen, text='Rules', font=('Courier', 30, 'italic'), command=self.game_rule)
        Rules.configure(bg='white', fg='black', activebackground='black', borderwidth=0, activeforeground='white')
        Rules.place(relx=0.43, rely=0.40, width=280)
        # Button to check all possible player and to see who has a password
        Player = tk.Button(Screen, text='Players', font=('Courier', 30, 'italic'), command=self.player_screen)
        Player.configure(bg='white', fg='black', activebackground='black', borderwidth=0, activeforeground='white')
        Player.place(relx=0.43, rely=0.50, width=280)
        # Button to open leaderboard
        Leaderboard = tk.Button(Screen, text='Leaderboard', font=('Courier', 30, 'italic'), command=self.board)
        Leaderboard.place(relx=0.43, rely=0.60, width=280)
        # Button to quit Application
        Quit = tk.Button(Screen, text='Quit', font=('Courier', 30, 'italic'), borderwidth=0, command=Screen.destroy)
        Quit.place(relx=0.43, rely=0.70, width=280)

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

        rules.attributes('-fullscreen', True)

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
        player.attributes('-fullscreen', True)
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
        self.logging = tk.Toplevel()
        self.logging.configure(background='black')
        self.logging.state('zoomed')
        self.logging.attributes('-fullscreen', True)
        self.logging.title('Log in ')
        self.logging.grab_set()

        bigfont = TkFont.Font(family='System', size=10)
        self.logging.option_add("*TCombobox*Listbox*Font", bigfont)
        # Frame to encapsulate the first player logins
        Framer = tk.Frame(self.logging)
        Framer.configure(background='black')
        Framer.place(relx=0.10, rely=0.05)
        # Second Frame to encapsulate the second player logins
        Framer2 = tk.Frame(self.logging)
        Framer2.configure(background='black')
        Framer2.place(relx=0.70, rely=0.05)
        # Third Frame for Start and Quit button
        Framer3 = tk.Frame(self.logging)
        Framer3.configure(background='black')
        Framer3.place(relx=0.45, rely=0.6)
        # Player 1 login
        player1 = tk.Label(Framer, text='Player 1', font=('System', 20), bg='black', fg='white')
        player1.pack()
        user1 = tk.Label(Framer, text='Username', font=('System', 20), bg='black', fg='white')
        user1.pack(pady=(20, 0))
        player1_name = ttk.Combobox(Framer, font=("Times New Roman", 20), values=self.nameList)
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
        player2_name = ttk.Combobox(Framer2, font=("Times New Roman", 20), values=self.nameList)
        player2_name.pack(ipadx=50, ipady=20, pady=(10, 30))
        pass2 = tk.Label(Framer2, text='Password', font=('System', 20), bg='black', fg='white')
        pass2.pack(pady=(0, 0))
        player2_pass = tk.Entry(Framer2, font=("Times New Roman", 20), show="*")
        player2_pass.pack(ipadx=50, ipady=20)

        # Begin Button
        Button = tk.Button(Framer3, text='Start', font=('System', 30), borderwidth=0, fg='white',
                           bg='black', command=lambda: self.authentication(player1_name.get(), player1_pass.get(),
                                                                           player2_name.get(), player2_pass.get()),
                           activeforeground='white', activebackground='black')
        Button.pack(pady=(10, 20))
        # Sign in Button
        SignIn = tk.Button(Framer3, text="Sign in", font=('System', 30), command=self.signing, borderwidth=0,
                           fg='white',
                           bg='black',
                           activeforeground='white', activebackground='black')

        SignIn.pack(pady=(10, 20))
        # Quit Button
        Quit = tk.Button(Framer3, text='Quit', font=('System', 30), command=self.logging.destroy, borderwidth=0,
                         fg='white',
                         bg='black', activeforeground='white', activebackground='black')
        Quit.pack()

    def signing(self):
        # Sign up frame and some configuration
        self.signup = tk.Toplevel()
        self.signup.geometry('800x500')
        self.signup.configure(background='black')
        self.signup.grab_set()
        self.signup.title('Signup')
        self.signup.resizable(False, False)

        Frame = tk.Frame(self.signup, bg='black')
        Frame.place(relx=0.3, rely=0.2)

        userlabel = tk.Label(Frame, text="Who are you?", bg='black', fg='white', font=("System", 20))
        userlabel.pack()

        userentry = tk.Entry(Frame, font=('System', 25))
        userentry.pack(pady=20)

        passlabel = tk.Label(Frame, text="Write your password (Limit 30)", bg='black', fg='white', font=("System", 20))
        passlabel.pack()
        passentry = tk.Entry(Frame, font=('System', 25), show="*")
        passentry.pack(pady=(20, 0))

        # Signup button
        commit = tk.Button(Frame, text="Sign up", borderwidth=0, fg='white',
                           bg='black', activeforeground='white', activebackground='black', font=('System', 30),
                           command=lambda: self.check(userentry.get(), passentry.get()))
        commit.pack(pady=(20, 0))
        # Quit Button
        Quit = tk.Button(Frame, text="Quit", borderwidth=0, fg='white',
                         bg='black', activeforeground='white', activebackground='black', font=('System', 30),
                         command=self.signup.destroy)
        Quit.pack()

    def check(self, username, password):
        if username == '' or password == '':
            Error = tk.Toplevel()
            Error.grab_set()
            tk.Label(Error, text="USERNAME AND/OR PASSWORD CAN'T BE EMPTY", fg='white', bg='black',
                     font=('Arial', 50)).pack(fill=tk.BOTH)
            Error.after(2000, lambda: Error.destroy())
        else:

            if username not in self.nameList:
                Error = tk.Toplevel()
                Error.grab_set()
                tk.Label(Error, text="USERNAME IS NOT IN CURRENT DATABASE", fg='white', bg='black',
                         font=('Arial', 50)).pack(fill=tk.BOTH)
                Error.after(2000, lambda: Error.destroy())
            else:
                if len(password) > 30 or ' ' in password:
                    Error = tk.Toplevel()
                    Error.grab_set()
                    tk.Label(Error, text="PASSWORD IS TOO LONG/NO EMPTY SPACE IN PASSWORD", fg='white', bg='black',
                             font=('Arial', 30)).pack(fill=tk.BOTH)
                    Error.after(2000, lambda: Error.destroy())
                else:
                    self.cursor.execute(f"SELECT * FROM player WHERE name = '{username}'")
                    temp = self.cursor.fetchone()
                    if temp[3] != '':
                        Important = tk.Toplevel()
                        Important.grab_set()
                        tk.Label(Important, text="You already have a password! Do you want to continue?", fg='white',
                                 bg='black',
                                 font=('Arial', 50)).pack(fill=tk.BOTH)
                        Buttons_frame = tk.Frame(Important)
                        Buttons_frame.pack(fill=tk.BOTH)
                        tk.Button(Buttons_frame, text="Continue", fg='white', bg='black', font=('Arial', 50),
                                  command=lambda: [self.insert_data(username, password), Important.destroy(),
                                                   self.signup.destroy()]).pack(fill=tk.BOTH, side=tk.LEFT,
                                                                                expand=True)
                        tk.Button(Buttons_frame, text="No", fg='white', bg='black', font=('Arial', 50),
                                  command=Important.destroy).pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
                    else:
                        self.insert_data(username, password)
                        self.signup.destroy()

    def insert_data(self, user, passw):
        self.cursor.execute(f"UPDATE player SET password='{passw}', registered='Y' WHERE name='{user}'")
        self.c.commit()
        Pop = tk.Toplevel()
        Pop.grab_set()
        Pop.configure(background='black')
        Pop.resizable(False, False)
        Pop.geometry('1040x100')

        tk.Label(Pop, text="Your password has been set", fg='white', bg='black', font=('System', 40)).pack(fill=tk.BOTH)
        Pop.after(2000, lambda: Pop.destroy())

    def authentication(self, u1, p1, u2, p2):
        if u1 not in self.nameList or u2 not in self.nameList:
            Error = tk.Toplevel()
            Error.grab_set()
            tk.Label(Error, text="Your Log In are Faulty! Correct it!", fg='white', bg='black',
                     font=('Arial', 30)).pack(fill=tk.BOTH)
            Error.after(2000, lambda: Error.destroy())
        elif u1 == u2:
            Error = tk.Toplevel()
            Error.grab_set()
            tk.Label(Error, text="Don't try to be smart about this", fg='red', bg='black',
                     font=('Arial', 30)).pack(fill=tk.BOTH)
            Error.after(2000, lambda: Error.destroy())
        elif u1 in self.nameList and u2 in self.nameList:
            u1_pass = self.cursor.execute(f"SELECT * FROM player WHERE name='{u1}'").fetchone()[3]
            u2_pass = self.cursor.execute(f"SELECT * FROM player WHERE name='{u2}'").fetchone()[3]
            if u1_pass == "" and u2_pass == "":
                Error = tk.Toplevel()
                Error.grab_set()
                tk.Label(Error, text=f"{u1} and {u2} does not have a password!", fg='white', bg='black',
                         font=('Arial', 30)).pack(fill=tk.BOTH)
                Error.after(2000, lambda: Error.destroy())
            elif u1_pass == "":
                Error = tk.Toplevel()
                Error.grab_set()
                tk.Label(Error, text=f"{u1} does not have a password!", fg='white', bg='black',
                         font=('Arial', 30)).pack(fill=tk.BOTH)
                Error.after(2000, lambda: Error.destroy())
            elif u2_pass == "":
                Error = tk.Toplevel()
                Error.grab_set()
                tk.Label(Error, text=f"{u2} does not have a password!", fg='white', bg='black',
                         font=('Arial', 30)).pack(fill=tk.BOTH)
                Error.after(2000, lambda: Error.destroy())
            elif u1_pass == p1 and u2_pass == p2:
                Error = tk.Toplevel()
                self.logging.destroy()
                self.game(u1, u2)

                Error.after(2000, lambda: Error.destroy())
            else:
                Error = tk.Toplevel()
                Error.grab_set()
                tk.Label(Error, text="Someone's Password is incorrect! Remember it!", fg='white', bg='black',
                         font=('Arial', 30)).pack(fill=tk.BOTH)
                Error.after(2000, lambda: Error.destroy())

    def game(self, p1, p2):
        self.game_screen = tk.Toplevel()
        self.game_screen.configure(background='black')
        self.game_screen.grab_set()
        title = ["Why must I suffer?", "Has the Gambling God foresaken us?",
                 "Must we continue this gambling advertising?", "Does the application knows of its actions?",
                 "When will someone find this?"]
        self.game_screen.title(title[rand.randrange(0, len(title))])
        self.game_screen.attributes('-fullscreen', True)

        Player1 = tk.Label(self.game_screen, text=p1, bg='black', fg='white', font=('System', 30))
        Player1.place(relx=0.2, rely=0.1)
        Player2 = tk.Label(self.game_screen, text=p2, bg='black', fg='white', font=('System', 30))
        Player2.place(relx=0.6, rely=0.1)

        """
        image = tk.Label(self.game_screen, image=img[0])
        image.photo = img[0]
        image.pack()"""
        self.Score = {p1: [1, 0], p2: [1, 0]}
        Begin = tk.Button(self.game_screen, text=f"Click to begin {p1}'s game", borderwidth=0, bg='black', fg='white',
                          font=('System', 20), activebackground='black', activeforeground='white',
                          command=lambda: [self.dicey(p1, 0.2, 0.3, self.Score[p1][0]), self.end(p1, p2)])
        Begin.place(relx=0.15, rely=0.68)

        Begin2 = tk.Button(self.game_screen, text=f"Click to begin {p2}'s game", borderwidth=0, bg='black', fg='white',
                           font=('System', 20), activebackground='black', activeforeground='white',
                           command=lambda: [self.dicey(p2, 0.6, 0.3, self.Score[p2][0]), self.end(p1, p2)])
        Begin2.place(relx=0.55, rely=0.68)
        self.End = {p1: 0, p2: 0}

    def dicey(self, player, x, y, count):
        if count > 5:
            tk.Label(self.game_screen, text=f"{player} have reached limit", bg='black', fg='white',
                     font=('System', 20)).place(relx=x, rely=y + 0.2)
        elif player == 'Patrick Nguyen':
            img = [ImageTk.PhotoImage(Image.open("1.png")), ImageTk.PhotoImage(Image.open("2.png")),
                   ImageTk.PhotoImage(Image.open("3.png")), ImageTk.PhotoImage(Image.open("4.png"))]
            number = rand.randrange(0, len(img))
            roll = (str(random.choice([1, 2, 3, 4, 5, 6], p=[0.05, 0.05, 0.05, 0.05, 0.05, 0.75])),
                    str(random.choice([1, 2, 3, 4, 5, 6], p=[0.05, 0.05, 0.05, 0.05, 0.05, 0.75])))
            for i in roll:
                self.Score[player][1] += int(i)
            Total = tk.Label(self.game_screen, text=f"Total: {self.Score[player][1]}", bg='black', fg='white',
                             font=('System', 20))
            Total.place(relx=x, rely=y + 0.3)
            Rolls = tk.Label(self.game_screen, text=','.join(roll), bg='black', fg='white', font=('System', 30))
            Rolls.place(relx=x, rely=y - 0.1)
            image = tk.Label(self.game_screen, image=img[number])
            image.photo = img[number]
            image.place(relx=x, rely=y)

            Round = tk.Label(self.game_screen, text=f"Round {self.Score[player][0]}", bg='black', fg='white',
                             font=('System', 20))
            Round.place(relx=x, rely=y + 0.2)
            if self.Score[player][0] == 5:
                self.End[player] = 1
            self.Score[player][0] += 1

        else:
            img = [ImageTk.PhotoImage(Image.open("1.png")), ImageTk.PhotoImage(Image.open("2.png")),
                   ImageTk.PhotoImage(Image.open("3.png")), ImageTk.PhotoImage(Image.open("4.png"))]
            number = rand.randrange(0, len(img))
            roll = (str(rand.randrange(1, 6)), str(rand.randrange(1, 6)))
            for i in roll:
                self.Score[player][1] += int(i)
            Total = tk.Label(self.game_screen, text=f"Total: {self.Score[player][1]}", bg='black', fg='white',
                             font=('System', 20))
            Total.place(relx=x, rely=y + 0.3)
            Rolls = tk.Label(self.game_screen, text=','.join(roll), bg='black', fg='white', font=('System', 30))
            Rolls.place(relx=x, rely=y - 0.1)
            image = tk.Label(self.game_screen, image=img[number])
            image.photo = img[number]
            image.place(relx=x, rely=y)

            Round = tk.Label(self.game_screen, text=f"Round {self.Score[player][0]}", bg='black', fg='white',
                             font=('System', 20))
            Round.place(relx=x, rely=y + 0.2)
            if self.Score[player][0] == 5:
                self.End[player] = 1
            self.Score[player][0] += 1

    def end(self, p1, p2):
        a = self.End.get(p1)
        b = self.End.get(p2)

        if a == 1 and b == 1:
            if self.Score[p1][1] > self.Score[p2][1]:
                Winner = tk.Toplevel()
                Winner.resizable(False, False)
                Winner.configure(background='black')

                Winner.grab_set()

                Announcement = tk.Label(Winner, text=f"{p1} Won! {p2} Lost~~~", bg='black', fg='white',
                                        font=('System', 20))
                Announcement.pack(fill=tk.BOTH)
                play = tk.Button(Winner, text='Play again', bg='black', fg='white',
                                 font=('System', 20),
                                 command=lambda: [Winner.destroy(), self.emergency(p1,p2)])
                play.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
                Quit = tk.Button(Winner, text="Quit", bg='black', fg='white',
                                 font=('System', 20), command=lambda: [Winner.destroy(), self.game_screen.destroy()])
                Quit.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
                self.commit_winner(p1)
            elif self.Score[p1][1] < self.Score[p2][1]:
                Winner = tk.Toplevel()
                Winner.resizable(False, False)
                Winner.configure(background='black')

                Winner.grab_set()

                Announcement = tk.Label(Winner, text=f"{p2} Won! {p1} Lost~~~", bg='black', fg='white',
                                        font=('System', 20))
                Announcement.pack(fill=tk.BOTH)
                play = tk.Button(Winner, text='Play again', bg='black', fg='white',
                                 font=('System', 20),
                                 command=lambda: [Winner.destroy(), self.emergency(p1,p2)])
                play.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
                Quit = tk.Button(Winner, text="Quit", bg='black', fg='white',
                                 font=('System', 20), command=lambda: [Winner.destroy(), self.game_screen.destroy()])
                Quit.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
                self.commit_winner(p2)
            elif self.Score[p1][1] == self.Score[p2][1]:
                Winner = tk.Toplevel()
                Winner.resizable(False, False)
                Winner.configure(background='black')

                Winner.grab_set()

                Announcement = tk.Label(Winner, text=f"Both are losers!", bg='black', fg='white',
                                        font=('System', 20))
                Announcement.pack(fill=tk.BOTH)
                play = tk.Button(Winner, text='Play again', bg='black', fg='white',
                                 font=('System', 20),
                                 command=lambda: [Winner.destroy(), self.emergency()])
                play.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
                Quit = tk.Button(Winner, text="Quit", bg='black', fg='white',
                                 font=('System', 20), command=lambda: [Winner.destroy(), self.game_screen.destroy(p1,p2)])
                Quit.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    def commit_winner(self, player):
        self.leadercursor.execute(f"INSERT INTO leaderboard VALUES ('{player}', {self.Score[player][1]})")
        self.leaderboard.commit()

    def board(self):
        ranking = self.leadercursor.execute("SELECT * FROM leaderboard ORDER BY score DESC LIMIT 5 ").fetchall()

        # Creating Frame for simple player data (Name, registered)
        player = tk.Toplevel()
        player.attributes('-fullscreen', True)
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
        Data = ttk.Treeview(player, column=('#0', "#1"), height=5)
        # Giving headings to each column
        Data.heading('#0', text='Rank')
        Data.heading('#1', text='Name')
        Data.heading('#2', text='Score')
        # Position of the Table
        Data.place(relx=0.32, rely=0.3)
        Rank = 1
        for x in ranking:
            Data.insert('', str(Rank), text=str(Rank), values=(x[0], x[1]))
            Rank += 1

    def emergency(self,p1,p2):
        Assurance = tk.Toplevel()
        Assurance.grab_set()
        Assurance.resizable(False,False)
        Assurance.configure(background='black')
        Question = tk.Label(Assurance, text="Does both player want to continue playing?", font=("System", 30), bg='black', fg='white')
        Question.pack()
        Yes = tk.Button(Assurance, text="YES", font=("System", 30), borderwidth=0, background='black', foreground='white',
                       activeforeground='white', activebackground='black', command=lambda:[Assurance.destroy(), self.game_screen.destroy(), self.game(p1,p2)])
        Yes.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        No = tk.Button(Assurance, text="NO", font=("System", 30), borderwidth=0, background='black', foreground='white',
                       activeforeground='white', activebackground='black', command=lambda:[Assurance.destroy(), self.game_screen.destroy()])
        No.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
Application = DiceThrower()
