import sqlite3
import tkinter as tk
from tkinter import ttk


class SportsDatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Database Management")
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use the clam theme for a modern look
        self.root.geometry("1400x800")  # Set window size
        self.login_frame()

    def set_style(self, widget, background, foreground, font_size=10):
        self.style.configure(widget, background=background, foreground=foreground, font=("Helvetica", font_size, "bold"))

    def login_frame(self):
        login_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        login_frame.pack_propagate(False)
        login_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 12)  # Label style
        self.set_style("TEntry", "white", "#3498db")  # Entry style
        self.set_style("TButton", "#2ecc71", "white", 12)  # Button style

        ttk.Label(login_frame, text="Login/Sign-up").pack(pady=10)

        ttk.Label(login_frame, text="Username").pack()
        username_entry = ttk.Entry(login_frame)
        username_entry.pack()

        ttk.Label(login_frame, text="Password").pack()
        password_entry = ttk.Entry(login_frame, show="*")
        password_entry.pack()

        login_button = ttk.Button(login_frame, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get()))
        login_button.pack(pady=10)

        signup_button = ttk.Button(login_frame, text="Sign Up", command=self.signup)
        signup_button.pack(pady=10)
    
    def login(self, username, password):
        # Add code to validate user credentials
        # For simplicity, using predefined admin credentials
        if username == "admin" and password == "adminpassword":
            self.admin_home_page()
        else:
            self.user_home_page()

    def signup(self):
        # Add code for user registration
        # You can implement a new window or a dialog for user registration
        # For simplicity, let's assume the user is already registered
        self.user_home_page()

    def user_home_page(self):
        self.clear_screen()

        home_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        home_frame.pack_propagate(False)
        home_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(home_frame, text="Welcome to Local Championship").pack(pady=10)

        self.set_style("TButton", "#2ecc71", "white", 12)  # Larger button style
        alpha_button = ttk.Button(home_frame, text="Team Ranking", command=self.user_page_alpha)
        alpha_button.pack(pady=10)

        beta_button = ttk.Button(home_frame, text="Player Ranking", command=self.user_page_beta)
        beta_button.pack(pady=10)

        # New buttons for group stage and knockout stage
        group_stage_button = ttk.Button(home_frame, text="Group Stage", command=self.user_page_group_stage)
        group_stage_button.pack(pady=10)

        knockout_stage_button = ttk.Button(home_frame, text="Knockout Stage", command=self.user_page_knockout_stage)
        knockout_stage_button.pack(pady=10)

        cursor.execute("SELECT TeamID, TeamName\
                        FROM Team")

        data = cursor.fetchall()

        ttk.Label(home_frame, text="TEAMS").pack()

        # Create a scrollable frame
        scrollable_frame = tk.Frame(home_frame)
        scrollable_frame.pack(side=tk.TOP, padx=10)

        canvas = tk.Canvas(scrollable_frame, width=250)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Add column names
        column_names = ["Team ID", "Team", "View Players"]
        for col, name in enumerate(column_names):
            label = tk.Label(inner_frame, text=name, font=("Helvetica", 10, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for row_idx, row in enumerate(data, start=1):
            team_id = row[0]
            label = tk.Label(inner_frame, text=team_id)
            label.grid(row=row_idx, column=0, padx=30, pady=5, sticky="w")

            team_name = row[1]
            label = tk.Label(inner_frame, text=row[1])
            label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")

            button = tk.Button(inner_frame, text="Players", command=lambda tid=team_id,tname=team_name: self.user_show_players(
                                                                                                                tid, tname))
            button.grid(row=row_idx, column=2, padx=30, pady=5, sticky="w")

        # Bind the canvas to the mousewheel for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind("<Configure>", lambda event: self.update_scrollregion(event, canvas))

        canvas.focus_set()

    def user_show_players(self, team_id, team_name):
        # Add code to show details of the selected player based on the player_id
        self.clear_screen()

        players_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        players_frame.pack_propagate(False)
        players_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(players_frame, text=f"Players of team {team_name}").pack(pady=10)

        cursor.execute(f"SELECT * \
                        FROM \
                            Player p \
                        WHERE \
                            p.TeamID = {team_id}"
                       )
        
        data = cursor.fetchall()

        entity_fields = self.get_entity_fields("Player")

        # Create a scrollable frame
        scrollable_frame = tk.Frame(players_frame)
        scrollable_frame.pack(side=tk.TOP, padx=10)

        canvas = tk.Canvas(scrollable_frame, width=930)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Add column names
        for col, name in enumerate(entity_fields):
            label = tk.Label(inner_frame, text=name, font=("Helvetica", 10, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for row_idx, row in enumerate(data, start=1):
            label = tk.Label(inner_frame, text=row[0])
            label.grid(row=row_idx, column=0, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[1])
            label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")
            
            label = tk.Label(inner_frame, text=row[2])
            label.grid(row=row_idx, column=2, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[3])
            label.grid(row=row_idx, column=3, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[4])
            label.grid(row=row_idx, column=4, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[5])
            label.grid(row=row_idx, column=5, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[6])
            label.grid(row=row_idx, column=6, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[7])
            label.grid(row=row_idx, column=7, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[8])
            label.grid(row=row_idx, column=8, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[9])
            label.grid(row=row_idx, column=9, padx=10, pady=5, sticky="w")

        # Bind the canvas to the mousewheel for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind("<Configure>", lambda event: self.update_scrollregion(event, canvas))

        canvas.focus_set()

        back_button = tk.Button(players_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

    def admin_home_page(self):
        self.clear_screen()

        home_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        home_frame.pack_propagate(False)
        home_frame.pack(padx=20, pady=20)

        ttk.Label(home_frame, text="Welcome to Local Championship Database Management").pack(pady=10)

        self.set_style("TButton", "#2ecc71", "white", 12)  # Larger button style
        alpha_button = ttk.Button(home_frame, text="Team Ranking", command=self.admin_page_alpha)
        alpha_button.pack(pady=10)

        beta_button = ttk.Button(home_frame, text="Player Ranking", command=self.admin_page_beta)
        beta_button.pack(pady=10)

        group_stage_button = ttk.Button(home_frame, text="Group Stage", command=self.admin_page_group_stage)
        group_stage_button.pack(pady=10)

        knockout_stage_button = ttk.Button(home_frame, text="Knockout Stage", command=self.admin_page_knockout_stage)
        knockout_stage_button.pack(pady=10)
        
        cursor.execute("SELECT TeamID, TeamName\
                        FROM Team")

        data = cursor.fetchall()

        ttk.Label(home_frame, text="TEAMS").pack()

        # Create a scrollable frame
        scrollable_frame = tk.Frame(home_frame)
        scrollable_frame.pack(side=tk.TOP, padx=10)

        canvas = tk.Canvas(scrollable_frame, width=250)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Add column names
        column_names = ["Team ID", "Team", "View Players"]
        for col, name in enumerate(column_names):
            label = tk.Label(inner_frame, text=name, font=("Helvetica", 10, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for row_idx, row in enumerate(data, start=1):
            team_id = row[0]
            label = tk.Label(inner_frame, text=team_id)
            label.grid(row=row_idx, column=0, padx=30, pady=5, sticky="w")

            team_name = row[1]
            label = tk.Label(inner_frame, text=row[1])
            label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")

            button = tk.Button(inner_frame, text="Players", command=lambda tid=team_id,tname=team_name: self.admin_show_players(
                                                                                                                tid, tname))
            button.grid(row=row_idx, column=2, padx=30, pady=5, sticky="w")

        # Bind the canvas to the mousewheel for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind("<Configure>", lambda event: self.update_scrollregion(event, canvas))

        canvas.focus_set()

        view_button = ttk.Button(home_frame, text="View data from DB", command=self.view_data)
        view_button.pack(pady=10)

        insert_button = ttk.Button(home_frame, text="Insert data to DB", command=self.insert_data)
        insert_button.pack(pady=10)

    def admin_show_players(self, team_id, team_name):
        # Add code to show details of the selected player based on the player_id
        self.clear_screen()

        players_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        players_frame.pack_propagate(False)
        players_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(players_frame, text=f"Players of team {team_name}").pack(pady=10)

        cursor.execute(f"SELECT * \
                        FROM \
                            Player p \
                        WHERE \
                            p.TeamID = {team_id}"
                       )
        
        data = cursor.fetchall()

        entity_fields = self.get_entity_fields("Player")

        # Create a scrollable frame
        scrollable_frame = tk.Frame(players_frame)
        scrollable_frame.pack(side=tk.TOP, padx=10)

        canvas = tk.Canvas(scrollable_frame, width=930)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Add column names
        for col, name in enumerate(entity_fields):
            label = tk.Label(inner_frame, text=name, font=("Helvetica", 10, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for row_idx, row in enumerate(data, start=1):
            label = tk.Label(inner_frame, text=row[0])
            label.grid(row=row_idx, column=0, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[1])
            label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")
            
            label = tk.Label(inner_frame, text=row[2])
            label.grid(row=row_idx, column=2, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[3])
            label.grid(row=row_idx, column=3, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[4])
            label.grid(row=row_idx, column=4, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[5])
            label.grid(row=row_idx, column=5, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[6])
            label.grid(row=row_idx, column=6, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[7])
            label.grid(row=row_idx, column=7, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[8])
            label.grid(row=row_idx, column=8, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[9])
            label.grid(row=row_idx, column=9, padx=10, pady=5, sticky="w")

        # Bind the canvas to the mousewheel for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind("<Configure>", lambda event: self.update_scrollregion(event, canvas))

        canvas.focus_set()

        back_button = tk.Button(players_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def user_page_alpha(self):
        self.clear_screen()

        page_alpha_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        page_alpha_frame.pack_propagate(False)
        page_alpha_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(page_alpha_frame, text="Team Ranking based on Goals Scored").pack(pady=10)
        # Add code to fetch and display team ranking based on goals scored from the database
        cursor.execute("SELECT \
                            t.TeamID, \
                            t.TeamName, \
                            SUM(ps.GoalsScored) AS TotalGoalsScored \
                        FROM \
                            Team t \
                        JOIN \
                            Player p \
                        ON \
                            t.TeamID = p.TeamID \
                        JOIN \
                            PlayerStats ps \
                        ON \
                            p.PlayerID = ps.PlayerID \
                        GROUP BY \
                            t.TeamID, t.TeamName \
                        ORDER BY \
                            TotalGoalsScored DESC" \
                       )
        
        data = cursor.fetchall()
        # Create a Treeview widget
        tree = ttk.Treeview(page_alpha_frame, columns=["TeamID","Team Name","Goals Scored"], show="headings")

        # Set up columns
        for field in ["TeamID","Team Name","Goals Scored"]:
            tree.heading(field, text=field)
            tree.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Insert data rows
        for row in data:
            tree.insert("", "end", values=row)

        # Add the Treeview to the frame
        tree.pack(side=tk.TOP, fill=tk.BOTH)

        back_button = tk.Button(page_alpha_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

    def user_page_beta(self):
        self.clear_screen()

        page_beta_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        page_beta_frame.pack_propagate(False)
        page_beta_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(page_beta_frame, text="Player Ranking based on Goals Scored").pack(pady=10)
        # Add code to fetch and display player ranking based on goals scored from the database
        cursor.execute("SELECT \
                            p.PlayerID, \
                            p.FirstName, \
                            p.LastName, \
                            t.TeamName, \
                            pss.GOALS \
                        FROM \
                            Player as p \
                        JOIN \
                            Team as t ON p.TeamID = t.TeamID \
                        JOIN \
                            ( \
                            SELECT SUM(ps.GoalsScored) as GOALS, ps.PlayerID \
                            FROM PlayerStats as ps \
                            GROUP BY ps.playerID \
                            ) as pss on pss.PlayerID = p.PlayerID \
                        ORDER BY \
                            pss.GOALS DESC")

        data = cursor.fetchall()
        # Create a scrollable frame
        scrollable_frame = tk.Frame(page_beta_frame)
        scrollable_frame.pack(side=tk.TOP, padx=10)

        canvas = tk.Canvas(scrollable_frame, width=400)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Add column names
        column_names = ["Name", "Team", "Goals Scored", "View Stats"]
        for col, name in enumerate(column_names):
            label = tk.Label(inner_frame, text=name, font=("Helvetica", 10, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for row_idx, row in enumerate(data, start=1):
            player_id = row[0]
            player_info = f"{row[1]} {row[2]}"
            label = tk.Label(inner_frame, text=player_info)
            label.grid(row=row_idx, column=0, padx=10, pady=5, sticky="w")

            team_label = tk.Label(inner_frame, text=row[3])
            team_label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")

            goals_label = tk.Label(inner_frame, text=row[4])
            goals_label.grid(row=row_idx, column=2, padx=10, pady=5, sticky="w")

            button = tk.Button(inner_frame, text="View Stats", command=lambda pid=player_id,pinfo=player_info: 
                                                                                                self.user_show_player_details(pid, 
                                                                                                                              pinfo))
            button.grid(row=row_idx, column=3, padx=10, pady=5, sticky="w")

        back_button = tk.Button(page_beta_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

        # Bind the canvas to the mousewheel for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind("<Configure>", lambda event: self.update_scrollregion(event, canvas))

        canvas.focus_set()


    def user_show_player_details(self, player_id, player_info):
        # Add code to show details of the selected player based on the player_id
        self.clear_screen()

        player_stats_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        player_stats_frame.pack_propagate(False)
        player_stats_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(player_stats_frame, text=f"Stats of player {player_info}").pack(pady=10)

        # Add code to fetch and display team ranking based on goals scored from the database
        cursor.execute(f"SELECT * \
                        FROM \
                            PlayerStats p \
                        WHERE \
                            p.PlayerID = {player_id}"
                       )
        
        data = cursor.fetchall()
        # Create a Treeview widget
        entity_fields = self.get_entity_fields("PlayerStats")
        tree = ttk.Treeview(player_stats_frame, columns=entity_fields, show="headings")

        # Set up columns
        for field in entity_fields:
            tree.heading(field, text=field)
            tree.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Insert data rows
        for row in data:
            tree.insert("", "end", values=row)

        # Add the Treeview to the frame
        tree.pack(side=tk.TOP, fill=tk.BOTH)

        back_button = tk.Button(player_stats_frame, text="Back", command=self.user_page_beta)
        back_button.pack(pady=10)

    def user_page_group_stage(self):
        self.clear_screen()

        group_stage_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        group_stage_frame.pack_propagate(False)
        group_stage_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        self.set_style("TButton", "#2ecc71", "white", 12)  # Larger button style
        ttk.Label(group_stage_frame, text="Group Stage Information").pack(pady=10)

        wins = []
        for i in range(1,25):
            cursor.execute(f"SELECT \
                                ts.TeamID, SUM(ts.GoalsScored) \
                            FROM \
                                (SELECT \
                                    p.FirstName, t.TeamID, ps.GoalsScored \
                                FROM \
                                    Team as t \
                                JOIN \
                                    Plays as pl \
                                ON \
                                    pl.MatchID = '{i}' \
                                AND \
                                    pl.HomeTeamID = t.TeamID \
                                JOIN \
                                    Player as p \
                                ON \
                                    p.TeamID = t.TeamID \
                                JOIN \
                                    PlayerStats as ps \
                                ON \
                                    ps.PlayerID = p.PlayerID \
                                AND \
                                    ps.MatchID = '{i}') as ts \
                            GROUP BY \
                                ts.TeamID"
                            )
            homeTeamGoals = cursor.fetchall()

            cursor.execute(f"SELECT \
                                ts.TeamID, SUM(ts.GoalsScored) \
                            FROM \
                                (SELECT \
                                    p.FirstName, t.TeamID, ps.GoalsScored \
                                FROM \
                                    Team as t \
                                JOIN \
                                    Plays as pl \
                                ON \
                                    pl.MatchID = '{i}' \
                                AND \
                                    pl.GuestTeamID = t.TeamID \
                                JOIN \
                                    Player as p \
                                ON \
                                    p.TeamID = t.TeamID \
                                JOIN \
                                    PlayerStats as ps \
                                ON \
                                    ps.PlayerID = p.PlayerID \
                                AND \
                                    ps.MatchID = '{i}') as ts \
                            GROUP BY \
                                ts.TeamID"
                            )
            guestTeamGoals = cursor.fetchall()
            if(homeTeamGoals[0][1] > guestTeamGoals[0][1]): wins.append((homeTeamGoals[0][0],i))
            elif(homeTeamGoals[0][1] < guestTeamGoals[0][1]): wins.append((guestTeamGoals[0][0],i))
            else: wins.append((0,0,i))

        cursor.execute("SELECT \
                            t.TeamName \
                        FROM \
                            Team as t \
                        ORDER BY \
                            t.TeamID")
        teamNames = cursor.fetchall()
        ranking = []
        for j in range(1,9):
            ranking.append([j,teamNames[j-1][0],0])
            for i in range(1,25):
                if(wins[i-1][0] == j): ranking[j-1][2] = ranking[j-1][2]+1
        
        groupa = []
        groupb = []
        for i in range(0,8):
            if (ranking[i][0] < 5): groupa.append(ranking[i]) 
            elif (ranking[i][0] >= 5): groupb.append(ranking[i])
        
        groupa.sort(key=lambda x: x[2], reverse=True)
        groupb.sort(key=lambda x: x[2], reverse=True)
        
        # First Treeview
        tree1_frame = tk.Frame(group_stage_frame)
        tree1_frame.pack(side=tk.TOP, padx=10)

        ttk.Label(tree1_frame, text="Group A").pack()
        tree1 = ttk.Treeview(group_stage_frame, columns=["TeamID", "Team Name", "Wins"], show="headings")

        # Set up columns
        for field in ["TeamID", "Team Name", "Wins"]:
            tree1.heading(field, text=field)
            tree1.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed 

        for row in groupa:
            tree1.insert("", "end", values=row)

        # Add the first Treeview to the frame
        tree1.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        # Second Treeview
        tree2_frame = tk.Frame(group_stage_frame)
        tree2_frame.pack(side=tk.TOP, padx=10)

        ttk.Label(tree2_frame, text="Group B").pack()
        tree2 = ttk.Treeview(group_stage_frame, columns=["TeamID", "Team Name", "Wins"], show="headings")

        # Set up columns
        for field in ["TeamID", "Team Name", "Wins"]:
            tree2.heading(field, text=field)
            tree2.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed
        
        for row in groupb:
            tree2.insert("", "end", values=row)

        # Add the second Treeview to the frame
        tree2.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        match_button = tk.Button(group_stage_frame, text="Matches", command=self.user_group_matches_page)
        match_button.pack(pady=10)

        back_button = tk.Button(group_stage_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

    def user_group_matches_page(self):
        self.clear_screen()

        match_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        match_frame.pack_propagate(False)
        match_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(match_frame, text="Welcome to Local Championship").pack(pady=10)

        cursor.execute("SELECT MatchID, Date, Time, CourtID, Phase, t.TeamName as HomeTeam, ts.TeamName as GuestTeam \
                       FROM \
                       (SELECT * \
                       FROM \
                       (SELECT *\
                        FROM Match \
                        WHERE Phase='Group A') as m \
                        JOIN Plays as p \
                        ON p.MatchID = m.MatchID) as pl\
                       JOIN Team as t \
                       ON t.TeamID = pl.HomeTeamID \
                       JOIN Team as ts \
                       ON ts.TeamID = pl.GuestTeamID")

        data1 = cursor.fetchall()

        cursor.execute("SELECT MatchID, Date, Time, CourtID, Phase, t.TeamName as HomeTeam, ts.TeamName as GuestTeam \
                       FROM \
                       (SELECT * \
                       FROM \
                       (SELECT *\
                        FROM Match \
                        WHERE Phase='Group B') as m \
                        JOIN Plays as p \
                        ON p.MatchID = m.MatchID) as pl\
                       JOIN Team as t \
                       ON t.TeamID = pl.HomeTeamID \
                       JOIN Team as ts \
                       ON ts.TeamID = pl.GuestTeamID")

        data2 = cursor.fetchall()

        ttk.Label(match_frame, text="Matches of Groups").pack()

        # Create a scrollable frame
        scrollable_frame = tk.Frame(match_frame)
        scrollable_frame.pack(side=tk.TOP, padx=10)

        canvas = tk.Canvas(scrollable_frame, width=700)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Add column names
        entity_fields = self.get_entity_fields('Match')
        entity_fields.append("Home Team")
        entity_fields.append("Guest Team")
        for col, name in enumerate(entity_fields):
            label = tk.Label(inner_frame, text=name, font=("Helvetica", 10, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for row_idx, row in enumerate(data1, start=1):
            match_id = row[0]
            label = tk.Label(inner_frame, text=match_id)
            label.grid(row=row_idx, column=0, padx=30, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[1])
            label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[2])
            label.grid(row=row_idx, column=2, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[3])
            label.grid(row=row_idx, column=3, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[4])
            label.grid(row=row_idx, column=4, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[5])
            label.grid(row=row_idx, column=5, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[6])
            label.grid(row=row_idx, column=6, padx=10, pady=5, sticky="w")

            button = tk.Button(inner_frame, text="Players", command=lambda mid=match_id: self.user_show_players_in_match(mid))
            button.grid(row=row_idx, column=7, padx=30, pady=5, sticky="w")

        for row_idx, row in enumerate(data2, start=len(data1) + 1):
            match_id = row[0]
            label = tk.Label(inner_frame, text=match_id)
            label.grid(row=row_idx, column=0, padx=30, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[1])
            label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[2])
            label.grid(row=row_idx, column=2, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[3])
            label.grid(row=row_idx, column=3, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[4])
            label.grid(row=row_idx, column=4, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[5])
            label.grid(row=row_idx, column=5, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[6])
            label.grid(row=row_idx, column=6, padx=10, pady=5, sticky="w")

            button = tk.Button(inner_frame, text="Players", command=lambda mid=match_id: self.user_show_players_in_match(mid))
            button.grid(row=row_idx, column=7, padx=30, pady=5, sticky="w")

        # Bind the canvas to the mousewheel for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind("<Configure>", lambda event: self.update_scrollregion(event, canvas))

        canvas.focus_set()

        back_button = tk.Button(match_frame, text="Back", command=self.user_page_group_stage)
        back_button.pack(pady=10)

    def user_show_players_in_match(self, match_id):
        self.clear_screen()

        match_players_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        match_players_frame.pack_propagate(False)
        match_players_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        self.set_style("TButton", "#2ecc71", "white", 12)  # Larger button style
        ttk.Label(match_players_frame, text=f"Match {match_id}").pack(pady=10)

        # First Treeview
        tree1_frame = tk.Frame(match_players_frame)  # Set the height here
        tree1_frame.pack(side=tk.TOP, padx=10)

        ttk.Label(tree1_frame, text="Home Team").pack()
        tree1 = ttk.Treeview(match_players_frame, height=11, columns=["First Name", "Last Name", "Position"], show="headings")

        # Set up columns
        for field in ["First Name", "Last Name", "Position"]:
            tree1.heading(field, text=field)
            tree1.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Fetch and insert data for the first tree
        cursor.execute(f"SELECT \
                            p2.FirstName, \
                            p2.LastName, \
                            p2.Position \
                        FROM \
                            (SELECT \
                                p.PlayerID, \
                                p.FirstName, \
                                p.LastName, \
                                p.TeamID, \
                                p.Position \
                            FROM \
                                Player as p \
                            JOIN \
                                PlayerStats as ps \
                            ON \
                                ps.MatchID = {match_id} \
                            AND \
                                ps.PlayerID = p.PlayerID \
                            ) as p2 \
                        JOIN \
                            Team as t \
                        ON \
                            t.TeamID = p2.TeamID \
                        JOIN \
                            Plays as pl \
                        ON \
                            pl.HomeTeamID = t.TeamID \
                        AND \
                            pl.MatchID = {match_id} \
                        ORDER BY \
                            p2.LastName,p2.FirstName"
                       )
        data1 = cursor.fetchall()
        for row in data1:
            tree1.insert("", "end", values=row)

        # Add the first Treeview to the frame
        tree1.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        # Second Treeview
        tree2_frame = tk.Frame(match_players_frame)
        tree2_frame.pack(side=tk.TOP, padx=10)

        ttk.Label(tree2_frame, text="Guest Team").pack()
        tree2 = ttk.Treeview(match_players_frame, height=11, columns=["First Name", "Last Name", "Position"], show="headings")

        # Set up columns
        for field in ["First Name", "Last Name", "Position"]:
            tree2.heading(field, text=field)
            tree2.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Fetch and insert data for the second tree
        # Add your second SQL query to fetch different data if needed
        cursor.execute(f"SELECT \
                            p2.FirstName, \
                            p2.LastName, \
                            p2.Position \
                        FROM \
                            (SELECT \
                                p.PlayerID, \
                                p.FirstName, \
                                p.LastName, \
                                p.TeamID, \
                                p.Position \
                            FROM \
                                Player as p \
                            JOIN \
                                PlayerStats as ps \
                            ON \
                                ps.MatchID = {match_id} \
                            AND \
                                ps.PlayerID = p.PlayerID \
                            ) as p2 \
                        JOIN \
                            Team as t \
                        ON \
                            t.TeamID = p2.TeamID \
                        JOIN \
                            Plays as pl \
                        ON \
                            pl.GuestTeamID = t.TeamID \
                        AND \
                            pl.MatchID = {match_id} \
                        ORDER BY \
                            p2.LastName,p2.FirstName"
                       )
        data2 = cursor.fetchall()
        for row in data2:
            tree2.insert("", "end", values=row)

        # Add the second Treeview to the frame
        tree2.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        back_button = tk.Button(match_players_frame, text="Back", command=self.user_group_matches_page)
        back_button.pack(pady=10)

    def user_page_knockout_stage(self):
        self.clear_screen()

        knockout_stage_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        knockout_stage_frame.pack_propagate(False)
        knockout_stage_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(knockout_stage_frame, text="Knockout Stage Information").pack(pady=10)

        wins = []
        for i in range(1,25):
            cursor.execute(f"SELECT \
                                ts.TeamID, SUM(ts.GoalsScored) \
                            FROM \
                                (SELECT \
                                    p.FirstName, t.TeamID, ps.GoalsScored \
                                FROM \
                                    Team as t \
                                JOIN \
                                    Plays as pl \
                                ON \
                                    pl.MatchID = '{i}' \
                                AND \
                                    pl.HomeTeamID = t.TeamID \
                                JOIN \
                                    Player as p \
                                ON \
                                    p.TeamID = t.TeamID \
                                JOIN \
                                    PlayerStats as ps \
                                ON \
                                    ps.PlayerID = p.PlayerID \
                                AND \
                                    ps.MatchID = '{i}') as ts \
                            GROUP BY \
                                ts.TeamID"
                            )
            homeTeamGoals = cursor.fetchall()

            cursor.execute(f"SELECT \
                                ts.TeamID, SUM(ts.GoalsScored) \
                            FROM \
                                (SELECT \
                                    p.FirstName, t.TeamID, ps.GoalsScored \
                                FROM \
                                    Team as t \
                                JOIN \
                                    Plays as pl \
                                ON \
                                    pl.MatchID = '{i}' \
                                AND \
                                    pl.GuestTeamID = t.TeamID \
                                JOIN \
                                    Player as p \
                                ON \
                                    p.TeamID = t.TeamID \
                                JOIN \
                                    PlayerStats as ps \
                                ON \
                                    ps.PlayerID = p.PlayerID \
                                AND \
                                    ps.MatchID = '{i}') as ts \
                            GROUP BY \
                                ts.TeamID"
                            )
            guestTeamGoals = cursor.fetchall()
            if(homeTeamGoals[0][1] > guestTeamGoals[0][1]): wins.append((homeTeamGoals[0][0],i))
            elif(homeTeamGoals[0][1] < guestTeamGoals[0][1]): wins.append((guestTeamGoals[0][0],i))
            else: wins.append((0,0,i))

        cursor.execute("SELECT \
                            t.TeamName \
                        FROM \
                            Team as t \
                        ORDER BY \
                            t.TeamID")
        teamNames = cursor.fetchall()
        ranking = []
        for j in range(1,9):
            ranking.append([j,teamNames[j-1][0],0])
            for i in range(1,25):
                if(wins[i-1][0] == j): ranking[j-1][2] = ranking[j-1][2]+1
        
        groupa = []
        groupb = []
        for i in range(0,8):
            if (ranking[i][0] < 5): groupa.append(ranking[i]) 
            elif (ranking[i][0] >= 5): groupb.append(ranking[i])
        
        groupa.sort(key=lambda x: x[2], reverse=True)
        groupb.sort(key=lambda x: x[2], reverse=True)

        knockoutsTeams = []
        knockoutsTeams.append(groupa[0][1])
        knockoutsTeams.append(groupb[1][1])
        knockoutsTeams.append(groupb[0][1])
        knockoutsTeams.append(groupa[1][1])

        # Display the bracket
        bracket_canvas = tk.Canvas(knockout_stage_frame, width=800, height=400, bg="white")
        bracket_canvas.pack(pady=10)

        # Draw the bracket lines
        bracket_canvas.create_line(150, 75, 350, 75, fill="black", width=2)  # Horizontal line (1a)
        bracket_canvas.create_line(150, 150, 350, 150, fill="black", width=2)  # Horizontal line (2a)
        bracket_canvas.create_line(150, 225, 350, 225, fill="black", width=2)  # Horizontal line (3a)
        bracket_canvas.create_line(150, 300, 350, 300, fill="black", width=2)  # Horizontal line (4a)

        # Draw the connecting lines for each round
        bracket_canvas.create_line(350, 75, 350, 150, fill="black", width=2)
        bracket_canvas.create_line(350, 225, 350, 300, fill="black", width=2)

        bracket_canvas.create_line(350, 112.5, 550, 112.5, fill="black", width=2) # Horizontal (1b)
        bracket_canvas.create_line(350, 262.5, 550, 262.5, fill="black", width=2) # Horizontal (2b)

        bracket_canvas.create_line(550, 112.5, 550, 262.5, fill="black", width=2)

        bracket_canvas.create_line(550, 187.5, 750, 187.5, fill="black", width=2) # Horizontal (1c)

        # Draw the team names
        for i, team in enumerate(knockoutsTeams):
            bracket_canvas.create_text(100, 75 + i * 75, text=str(i+1)+') '+team, font=("Helvetica", 12), anchor="e")

        # Draw the team names
        for i, team in enumerate(knockoutsTeams):
            bracket_canvas.create_text(250, 65 + i * 75, text=team, font=("Helvetica", 12), anchor="e")

        bracket_canvas.create_text(480, 102.5, text="Winner (1-2)", font=("Helvetica", 12), anchor="e")
        bracket_canvas.create_text(480, 252.5, text="Winner (3-4)", font=("Helvetica", 12), anchor="e")

        bracket_canvas.create_text(700, 177.5, text="Finals Winner", font=("Helvetica", 12), anchor="e")

        back_button = tk.Button(knockout_stage_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

    def admin_page_alpha(self):
        self.clear_screen()

        page_alpha_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        page_alpha_frame.pack_propagate(False)
        page_alpha_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(page_alpha_frame, text="Team Ranking based on Goals Scored").pack(pady=10)
        # Add code to fetch and display team ranking based on goals scored from the database

        cursor.execute("SELECT \
                            t.TeamID, \
                            t.TeamName, \
                            SUM(ps.GoalsScored) AS TotalGoalsScored \
                        FROM \
                            Team t \
                        JOIN \
                            Player p \
                        ON \
                            t.TeamID = p.TeamID \
                        JOIN \
                            PlayerStats ps \
                        ON \
                            p.PlayerID = ps.PlayerID \
                        GROUP BY \
                            t.TeamID, t.TeamName \
                        ORDER BY \
                            TotalGoalsScored DESC" \
                       )
        
        data = cursor.fetchall()
        # Create a Treeview widget
        tree = ttk.Treeview(page_alpha_frame, columns=["TeamID","Team Name","Goals Scored"], show="headings")

        # Set up columns
        for field in ["TeamID","Team Name","Goals Scored"]:
            tree.heading(field, text=field)
            tree.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Insert data rows
        for row in data:
            tree.insert("", "end", values=row)

        # Add the Treeview to the frame
        tree.pack(side=tk.TOP, fill=tk.BOTH)

        back_button = tk.Button(page_alpha_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def admin_page_beta(self):
        self.clear_screen()

        page_beta_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        page_beta_frame.pack_propagate(False)
        page_beta_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(page_beta_frame, text="Player Ranking based on Goals Scored").pack(pady=10)
        # Add code to fetch and display player ranking based on goals scored from the database
        cursor.execute("SELECT \
                            p.PlayerID, \
                            p.FirstName, \
                            p.LastName, \
                            t.TeamName, \
                            pss.GOALS \
                        FROM \
                            Player as p \
                        JOIN \
                            Team as t ON p.TeamID = t.TeamID \
                        JOIN \
                            ( \
                            SELECT SUM(ps.GoalsScored) as GOALS, ps.PlayerID \
                            FROM PlayerStats as ps \
                            GROUP BY ps.playerID \
                            ) as pss on pss.PlayerID = p.PlayerID \
                        ORDER BY \
                            pss.GOALS DESC;")

        data = cursor.fetchall()
        
        # Create a scrollable frame
        scrollable_frame = tk.Frame(page_beta_frame)
        scrollable_frame.pack(side=tk.TOP, padx=10)

        canvas = tk.Canvas(scrollable_frame, width=400)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Add column names
        column_names = ["Name", "Team", "Goals Scored", "View Stats"]
        for col, name in enumerate(column_names):
            label = tk.Label(inner_frame, text=name, font=("Helvetica", 10, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for row_idx, row in enumerate(data, start=1):
            player_id = row[0]
            player_info = f"{row[1]} {row[2]}"
            label = tk.Label(inner_frame, text=player_info)
            label.grid(row=row_idx, column=0, padx=10, pady=5, sticky="w")

            team_label = tk.Label(inner_frame, text=row[3])
            team_label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")

            goals_label = tk.Label(inner_frame, text=row[4])
            goals_label.grid(row=row_idx, column=2, padx=10, pady=5, sticky="w")

            button = tk.Button(inner_frame, text="View Stats", command=lambda pid=player_id, pinfo=player_info: 
                                                                                                self.admin_show_player_details(pid, 
                                                                                                                               pinfo))
            button.grid(row=row_idx, column=3, padx=10, pady=5, sticky="w")

        back_button = tk.Button(page_beta_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

        # Bind the canvas to the mousewheel for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind("<Configure>", lambda event: self.update_scrollregion(event, canvas))

        canvas.focus_set()

    def update_scrollregion(self, event, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_mousewheel(self, event, canvas):
        # Enable scrolling with the mouse wheel
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def admin_show_player_details(self, player_id, player_info):
        # Add code to show details of the selected player based on the player_id
        self.clear_screen()

        player_stats_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        player_stats_frame.pack_propagate(False)
        player_stats_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(player_stats_frame, text=f"Stats of player {player_info}").pack(pady=10)

        # Add code to fetch and display team ranking based on goals scored from the database
        cursor.execute(f"SELECT * \
                        FROM \
                            PlayerStats p \
                        WHERE \
                            p.PlayerID = {player_id}"
                       )
        
        data = cursor.fetchall()
        # Create a Treeview widget
        entity_fields = self.get_entity_fields("PlayerStats")
        tree = ttk.Treeview(player_stats_frame, columns=entity_fields, show="headings")

        # Set up columns
        for field in entity_fields:
            tree.heading(field, text=field)
            tree.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Insert data rows
        for row in data:
            tree.insert("", "end", values=row)

        # Add the Treeview to the frame
        tree.pack(side=tk.TOP, fill=tk.BOTH)

        back_button = tk.Button(player_stats_frame, text="Back", command=self.admin_page_beta)
        back_button.pack(pady=10)

    def admin_page_group_stage(self):
        self.clear_screen()

        group_stage_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        group_stage_frame.pack_propagate(False)
        group_stage_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(group_stage_frame, text="Group Stage Information").pack(pady=10)

        wins = []
        for i in range(1,25):
            cursor.execute(f"SELECT \
                                ts.TeamID, SUM(ts.GoalsScored) \
                            FROM \
                                (SELECT \
                                    p.FirstName, t.TeamID, ps.GoalsScored \
                                FROM \
                                    Team as t \
                                JOIN \
                                    Plays as pl \
                                ON \
                                    pl.MatchID = '{i}' \
                                AND \
                                    pl.HomeTeamID = t.TeamID \
                                JOIN \
                                    Player as p \
                                ON \
                                    p.TeamID = t.TeamID \
                                JOIN \
                                    CompetesIn as c \
                                ON \
                                    c.PlayerID = p.PlayerID \
                                AND \
                                    c.MatchID = '{i}' \
                                JOIN \
                                    PlayerStats as ps \
                                ON \
                                    ps.PlayerID = p.PlayerID \
                                AND \
                                    ps.MatchID = '{i}') as ts \
                            GROUP BY \
                                ts.TeamID"
                            )
            homeTeamGoals = cursor.fetchall()

            cursor.execute(f"SELECT \
                                ts.TeamID, SUM(ts.GoalsScored) \
                            FROM \
                                (SELECT \
                                    p.FirstName, t.TeamID, ps.GoalsScored \
                                FROM \
                                    Team as t \
                                JOIN \
                                    Plays as pl \
                                ON \
                                    pl.MatchID = '{i}' \
                                AND \
                                    pl.GuestTeamID = t.TeamID \
                                JOIN \
                                    Player as p \
                                ON \
                                    p.TeamID = t.TeamID \
                                JOIN \
                                    CompetesIn as c \
                                ON \
                                    c.PlayerID = p.PlayerID \
                                AND \
                                    c.MatchID = '{i}' \
                                JOIN \
                                    PlayerStats as ps \
                                ON \
                                    ps.PlayerID = p.PlayerID \
                                AND \
                                    ps.MatchID = '{i}') as ts \
                            GROUP BY \
                                ts.TeamID"
                            )
            guestTeamGoals = cursor.fetchall()
            if(homeTeamGoals[0][1] > guestTeamGoals[0][1]): wins.append((homeTeamGoals[0][0],i))
            elif(homeTeamGoals[0][1] < guestTeamGoals[0][1]): wins.append((guestTeamGoals[0][0],i))
            else: wins.append((0,0,i))

        cursor.execute("SELECT \
                            t.TeamName \
                        FROM \
                            Team as t \
                        ORDER BY \
                            t.TeamID")
        teamNames = cursor.fetchall()
        ranking = []
        for j in range(1,9):
            ranking.append([j,teamNames[j-1][0],0])
            for i in range(1,25):
                if(wins[i-1][0] == j): ranking[j-1][2] = ranking[j-1][2]+1
        
        groupa = []
        groupb = []
        for i in range(0,8):
            if (ranking[i][0] < 5): groupa.append(ranking[i]) 
            elif (ranking[i][0] >= 5): groupb.append(ranking[i])
        
        groupa.sort(key=lambda x: x[2], reverse=True)
        groupb.sort(key=lambda x: x[2], reverse=True)
        
        # First Treeview
        tree1_frame = tk.Frame(group_stage_frame)
        tree1_frame.pack(side=tk.TOP, padx=10)

        ttk.Label(tree1_frame, text="Group A").pack()
        tree1 = ttk.Treeview(group_stage_frame, columns=["TeamID", "Team Name", "Wins"], show="headings")

        # Set up columns
        for field in ["TeamID", "Team Name", "Wins"]:
            tree1.heading(field, text=field)
            tree1.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed 

        for row in groupa:
            tree1.insert("", "end", values=row)

        # Add the first Treeview to the frame
        tree1.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        # Second Treeview
        tree2_frame = tk.Frame(group_stage_frame)
        tree2_frame.pack(side=tk.TOP, padx=10)

        ttk.Label(tree2_frame, text="Group B").pack()
        tree2 = ttk.Treeview(group_stage_frame, columns=["TeamID", "Team Name", "Wins"], show="headings")

        # Set up columns
        for field in ["TeamID", "Team Name", "Wins"]:
            tree2.heading(field, text=field)
            tree2.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed
        
        for row in groupb:
            tree2.insert("", "end", values=row)

        # Add the second Treeview to the frame
        tree2.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        match_button = tk.Button(group_stage_frame, text="Matches", command=self.admin_group_matches_page)
        match_button.pack(pady=10)

        back_button = tk.Button(group_stage_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def admin_group_matches_page(self):
        self.clear_screen()

        match_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        match_frame.pack_propagate(False)
        match_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(match_frame, text="Welcome to Local Championship").pack(pady=10)

        cursor.execute("SELECT MatchID, Date, Time, CourtID, Phase, t.TeamName as HomeTeam, ts.TeamName as GuestTeam \
                       FROM \
                       (SELECT * \
                       FROM \
                       (SELECT *\
                        FROM Match \
                        WHERE Phase='Group A') as m \
                        JOIN Plays as p \
                        ON p.MatchID = m.MatchID) as pl\
                       JOIN Team as t \
                       ON t.TeamID = pl.HomeTeamID \
                       JOIN Team as ts \
                       ON ts.TeamID = pl.GuestTeamID")

        data1 = cursor.fetchall()

        cursor.execute("SELECT MatchID, Date, Time, CourtID, Phase, t.TeamName as HomeTeam, ts.TeamName as GuestTeam \
                       FROM \
                       (SELECT * \
                       FROM \
                       (SELECT *\
                        FROM Match \
                        WHERE Phase='Group B') as m \
                        JOIN Plays as p \
                        ON p.MatchID = m.MatchID) as pl\
                       JOIN Team as t \
                       ON t.TeamID = pl.HomeTeamID \
                       JOIN Team as ts \
                       ON ts.TeamID = pl.GuestTeamID")

        data2 = cursor.fetchall()

        ttk.Label(match_frame, text="Matches of Groups").pack()

        # Create a scrollable frame
        scrollable_frame = tk.Frame(match_frame)
        scrollable_frame.pack(side=tk.TOP, padx=10)

        canvas = tk.Canvas(scrollable_frame, width=700)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Add column names
        entity_fields = self.get_entity_fields('Match')
        entity_fields.append("Home Team")
        entity_fields.append("Guest Team")
        for col, name in enumerate(entity_fields):
            label = tk.Label(inner_frame, text=name, font=("Helvetica", 10, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        for row_idx, row in enumerate(data1, start=1):
            match_id = row[0]
            label = tk.Label(inner_frame, text=match_id)
            label.grid(row=row_idx, column=0, padx=30, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[1])
            label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[2])
            label.grid(row=row_idx, column=2, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[3])
            label.grid(row=row_idx, column=3, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[4])
            label.grid(row=row_idx, column=4, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[5])
            label.grid(row=row_idx, column=5, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[6])
            label.grid(row=row_idx, column=6, padx=10, pady=5, sticky="w")

            button = tk.Button(inner_frame, text="Players", command=lambda mid=match_id: self.admin_show_players_in_match(mid))
            button.grid(row=row_idx, column=7, padx=30, pady=5, sticky="w")

        for row_idx, row in enumerate(data2, start=len(data1) + 1):
            match_id = row[0]
            label = tk.Label(inner_frame, text=match_id)
            label.grid(row=row_idx, column=0, padx=30, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[1])
            label.grid(row=row_idx, column=1, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[2])
            label.grid(row=row_idx, column=2, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[3])
            label.grid(row=row_idx, column=3, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[4])
            label.grid(row=row_idx, column=4, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[5])
            label.grid(row=row_idx, column=5, padx=10, pady=5, sticky="w")

            label = tk.Label(inner_frame, text=row[6])
            label.grid(row=row_idx, column=6, padx=10, pady=5, sticky="w")

            button = tk.Button(inner_frame, text="Players", command=lambda mid=match_id: self.admin_show_players_in_match(mid))
            button.grid(row=row_idx, column=7, padx=30, pady=5, sticky="w")

        # Bind the canvas to the mousewheel for scrolling
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind("<Configure>", lambda event: self.update_scrollregion(event, canvas))

        canvas.focus_set()

        back_button = tk.Button(match_frame, text="Back", command=self.admin_page_group_stage)
        back_button.pack(pady=10)

    def admin_show_players_in_match(self, match_id):
        self.clear_screen()

        match_players_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        match_players_frame.pack_propagate(False)
        match_players_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        self.set_style("TButton", "#2ecc71", "white", 12)  # Larger button style
        ttk.Label(match_players_frame, text=f"Match {match_id}").pack(pady=10)

        # First Treeview
        tree1_frame = tk.Frame(match_players_frame)  # Set the height here
        tree1_frame.pack(side=tk.TOP, padx=10)

        ttk.Label(tree1_frame, text="Home Team").pack()
        tree1 = ttk.Treeview(match_players_frame, height=11, columns=["First Name", "Last Name", "Position"], show="headings")

        # Set up columns
        for field in ["First Name", "Last Name", "Position"]:
            tree1.heading(field, text=field)
            tree1.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Fetch and insert data for the first tree
        cursor.execute(f"SELECT \
                            p2.FirstName, \
                            p2.LastName, \
                            p2.Position \
                        FROM \
                            (SELECT \
                                p.PlayerID, \
                                p.FirstName, \
                                p.LastName, \
                                p.TeamID, \
                                p.Position \
                            FROM \
                                Player as p \
                            JOIN \
                                PlayerStats as ps \
                            ON \
                                ps.MatchID = {match_id} \
                            AND \
                                ps.PlayerID = p.PlayerID \
                            ) as p2 \
                        JOIN \
                            Team as t \
                        ON \
                            t.TeamID = p2.TeamID \
                        JOIN \
                            Plays as pl \
                        ON \
                            pl.HomeTeamID = t.TeamID \
                        AND \
                            pl.MatchID = {match_id} \
                        ORDER BY \
                            p2.LastName,p2.FirstName"
                       )
        data1 = cursor.fetchall()
        for row in data1:
            tree1.insert("", "end", values=row)

        # Add the first Treeview to the frame
        tree1.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        # Second Treeview
        tree2_frame = tk.Frame(match_players_frame)
        tree2_frame.pack(side=tk.TOP, padx=10)

        ttk.Label(tree2_frame, text="Guest Team").pack()
        tree2 = ttk.Treeview(match_players_frame, height=11, columns=["First Name", "Last Name", "Position"], show="headings")

        # Set up columns
        for field in ["First Name", "Last Name", "Position"]:
            tree2.heading(field, text=field)
            tree2.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Fetch and insert data for the second tree
        # Add your second SQL query to fetch different data if needed
        cursor.execute(f"SELECT \
                            p2.FirstName, \
                            p2.LastName, \
                            p2.Position \
                        FROM \
                            (SELECT \
                                p.PlayerID, \
                                p.FirstName, \
                                p.LastName, \
                                p.TeamID, \
                                p.Position \
                            FROM \
                                Player as p \
                            JOIN \
                                PlayerStats as ps \
                            ON \
                                ps.MatchID = {match_id} \
                            AND \
                                ps.PlayerID = p.PlayerID \
                            ) as p2 \
                        JOIN \
                            Team as t \
                        ON \
                            t.TeamID = p2.TeamID \
                        JOIN \
                            Plays as pl \
                        ON \
                            pl.GuestTeamID = t.TeamID \
                        AND \
                            pl.MatchID = {match_id} \
                        ORDER BY \
                            p2.LastName,p2.FirstName"
                       )
        data2 = cursor.fetchall()
        for row in data2:
            tree2.insert("", "end", values=row)

        # Add the second Treeview to the frame
        tree2.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        back_button = tk.Button(match_players_frame, text="Back", command=self.admin_group_matches_page)
        back_button.pack(pady=10)

    def admin_page_knockout_stage(self):
        self.clear_screen()

        knockout_stage_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        knockout_stage_frame.pack_propagate(False)
        knockout_stage_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(knockout_stage_frame, text="Knockout Stage Information").pack(pady=10)

        wins = []
        for i in range(1,25):
            cursor.execute(f"SELECT \
                                ts.TeamID, SUM(ts.GoalsScored) \
                            FROM \
                                (SELECT \
                                    p.FirstName, t.TeamID, ps.GoalsScored \
                                FROM \
                                    Team as t \
                                JOIN \
                                    Plays as pl \
                                ON \
                                    pl.MatchID = '{i}' \
                                AND \
                                    pl.HomeTeamID = t.TeamID \
                                JOIN \
                                    Player as p \
                                ON \
                                    p.TeamID = t.TeamID \
                                JOIN \
                                    CompetesIn as c \
                                ON \
                                    c.PlayerID = p.PlayerID \
                                AND \
                                    c.MatchID = '{i}' \
                                JOIN \
                                    PlayerStats as ps \
                                ON \
                                    ps.PlayerID = p.PlayerID \
                                AND \
                                    ps.MatchID = '{i}') as ts \
                            GROUP BY \
                                ts.TeamID"
                            )
            homeTeamGoals = cursor.fetchall()

            cursor.execute(f"SELECT \
                                ts.TeamID, SUM(ts.GoalsScored) \
                            FROM \
                                (SELECT \
                                    p.FirstName, t.TeamID, ps.GoalsScored \
                                FROM \
                                    Team as t \
                                JOIN \
                                    Plays as pl \
                                ON \
                                    pl.MatchID = '{i}' \
                                AND \
                                    pl.GuestTeamID = t.TeamID \
                                JOIN \
                                    Player as p \
                                ON \
                                    p.TeamID = t.TeamID \
                                JOIN \
                                    CompetesIn as c \
                                ON \
                                    c.PlayerID = p.PlayerID \
                                AND \
                                    c.MatchID = '{i}' \
                                JOIN \
                                    PlayerStats as ps \
                                ON \
                                    ps.PlayerID = p.PlayerID \
                                AND \
                                    ps.MatchID = '{i}') as ts \
                            GROUP BY \
                                ts.TeamID"
                            )
            guestTeamGoals = cursor.fetchall()
            if(homeTeamGoals[0][1] > guestTeamGoals[0][1]): wins.append((homeTeamGoals[0][0],i))
            elif(homeTeamGoals[0][1] < guestTeamGoals[0][1]): wins.append((guestTeamGoals[0][0],i))
            else: wins.append((0,0,i))

        cursor.execute("SELECT \
                            t.TeamName \
                        FROM \
                            Team as t \
                        ORDER BY \
                            t.TeamID")
        teamNames = cursor.fetchall()
        ranking = []
        for j in range(1,9):
            ranking.append([j,teamNames[j-1][0],0])
            for i in range(1,25):
                if(wins[i-1][0] == j): ranking[j-1][2] = ranking[j-1][2]+1
        
        groupa = []
        groupb = []
        for i in range(0,8):
            if (ranking[i][0] < 5): groupa.append(ranking[i]) 
            elif (ranking[i][0] >= 5): groupb.append(ranking[i])
        
        groupa.sort(key=lambda x: x[2], reverse=True)
        groupb.sort(key=lambda x: x[2], reverse=True)

        knockoutsTeams = []
        knockoutsTeams.append(groupa[0][1])
        knockoutsTeams.append(groupb[1][1])
        knockoutsTeams.append(groupb[0][1])
        knockoutsTeams.append(groupa[1][1])
        
        # Display the bracket
        bracket_canvas = tk.Canvas(knockout_stage_frame, width=800, height=400, bg="white")
        bracket_canvas.pack(pady=10)

        # Draw the bracket lines
        bracket_canvas.create_line(150, 75, 350, 75, fill="black", width=2)  # Horizontal line (1a)
        bracket_canvas.create_line(150, 150, 350, 150, fill="black", width=2)  # Horizontal line (2a)
        bracket_canvas.create_line(150, 225, 350, 225, fill="black", width=2)  # Horizontal line (3a)
        bracket_canvas.create_line(150, 300, 350, 300, fill="black", width=2)  # Horizontal line (4a)

        # Draw the connecting lines for each round
        bracket_canvas.create_line(350, 75, 350, 150, fill="black", width=2)
        bracket_canvas.create_line(350, 225, 350, 300, fill="black", width=2)

        bracket_canvas.create_line(350, 112.5, 550, 112.5, fill="black", width=2) # Horizontal (1b)
        bracket_canvas.create_line(350, 262.5, 550, 262.5, fill="black", width=2) # Horizontal (2b)

        bracket_canvas.create_line(550, 112.5, 550, 262.5, fill="black", width=2)

        bracket_canvas.create_line(550, 187.5, 750, 187.5, fill="black", width=2) # Horizontal (1c)

        # Draw the team names
        for i, team in enumerate(knockoutsTeams):
            bracket_canvas.create_text(100, 75 + i * 75, text=str(i+1)+') '+team, font=("Helvetica", 12), anchor="e")

        # Draw the team names
        for i, team in enumerate(knockoutsTeams):
            bracket_canvas.create_text(250, 65 + i * 75, text=team, font=("Helvetica", 12), anchor="e")

        bracket_canvas.create_text(480, 102.5, text="Winner (1-2)", font=("Helvetica", 12), anchor="e")
        bracket_canvas.create_text(480, 252.5, text="Winner (3-4)", font=("Helvetica", 12), anchor="e")

        bracket_canvas.create_text(700, 177.5, text="Finals Winner", font=("Helvetica", 12), anchor="e")

        back_button = tk.Button(knockout_stage_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def view_data(self):
        self.clear_screen()

        view_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        view_frame.pack_propagate(False)
        view_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(view_frame, text="Local Championship's Data").pack(pady=10)
        # Add code to fetch and display data from the database by entity

        entities = ["Court", "Championship", "Team", "Referee", "Match", "Plays", "Includes", "Referees", "Player", "PlayerStats", "Position"]

        entity_var = tk.StringVar()
        entity_dropdown = ttk.Combobox(view_frame, textvariable=entity_var, values=entities)
        entity_dropdown.pack(pady=10)

        insert_button = tk.Button(view_frame, text="View", command=lambda: self.view_entity_data(view_frame, entity_var.get()))
        insert_button.pack(pady=10)

        back_button = tk.Button(view_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def insert_data(self):
        self.clear_screen()

        insert_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        insert_frame.pack_propagate(False)
        insert_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(insert_frame, text="Insert Data into Local Championship Database").pack(pady=10)

        entities = ["Court", "Championship", "Team", "Referee", "Match", "Plays", "Includes", "Referees", "Player", "PlayerStats", "Position"]

        entity_var = tk.StringVar()
        entity_dropdown = ttk.Combobox(insert_frame, textvariable=entity_var, values=entities)
        entity_dropdown.pack(pady=10)

        insert_button = tk.Button(insert_frame, text="Insert", command=lambda: self.show_fields(insert_frame, entity_var.get()))
        insert_button.pack(pady=10)

        back_button = tk.Button(insert_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def show_fields(self, frame, entity):
        frame.destroy()

        fields_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        fields_frame.pack_propagate(False)
        fields_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(fields_frame, text=f"Insert data for {entity}").pack(pady=10)

        # Get the fields for the selected entity
        entity_fields = self.get_entity_fields(entity)

        entries = []
        # Create entry fields for each field in the entity
        for field in entity_fields:
            tk.Label(fields_frame, text=field).pack()
            entry = tk.Entry(fields_frame)
            entry.pack()
            entries.append(entry)

        insert_button = tk.Button(fields_frame, text="Insert", command=lambda: self.insert_callback(
                                                                                                    entries, 
                                                                                                    fields_frame,
                                                                                                    entity, 
                                                                                                    entity_fields, 
                                                                                                    ))
        insert_button.pack(pady=10)

        back_button = tk.Button(fields_frame, text="Back", command=lambda: self.insert_data())
        back_button.pack(pady=10)
    
    # Callback function to retrieve entry values when the "Insert" button is clicked
    def insert_callback(self, entries, fields_frame, entity, entity_fields):
        values = [entry.get() for entry in entries]
        self.insert_entity_data(fields_frame, entity, entity_fields, values)

    def get_entity_fields(self, entity):
        # Add code to retrieve the fields of the selected entity from the database or another source
        # For simplicity, using predefined fields for each entity here
        entity_fields_dict = {
            "Court": ["courtID", "CourtName", "Capacity", "Location"],
            "Championship": ["ChampionshipID", "ChampionshipName", "StartDate", "EndDate", "Description"],
            "Team": ["TeamID", "TeamName", "TeamFoundedDate", "TeamCoachFname", "TeamCoachLname", "CourtOwnedID", "ChampionshipID"],
            "Referee": ["RefereeID", "FirstName", "LastName", "Experience"],
            "Match": ["MatchID", "Date", "Time", "CourtID", "Phase"],
            "Plays": ["HomeTeamID", "GuestTeamID", "MatchID"],
            "Includes": ["ChampionshipID", "MatchID"],
            "Referees": ["RefereeID", "MatchID"],
            "Player": ["PlayerID", "FirstName", "LastName", "DateOfBirth", "Nationality", "Height", "Weight", "Position", "TeamID", "JerseyNumber"],
            "PlayerStats": ["PlayerID", "MatchID", "MinutesPlayed", "RedCards", "YellowCards", "GoalsScored", "Shots", "ShotsOnTarget", "Passes", "Assists", "Offsides", "Tackles"],
            "Position": ["PlayerID", "Position"]
            # Add fields for other entities
        }
        return entity_fields_dict.get(entity, [])
    
    def insert_entity_data(self, frame, entity, entity_fields, values):
        frame.destroy()
        
        new_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        new_frame.pack_propagate(False)
        new_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(new_frame, text=f"Inserting data for {entity}").pack(pady=10)

        # Create a placeholder string for SQL VALUES clause
        values_placeholder = "(" + ", ".join(["?" for _ in values]) + ")"

        # Execute the SQL INSERT statement
        cursor.execute(f"INSERT INTO {entity} ({', '.join(entity_fields)}) VALUES {values_placeholder}", values)
        conn.commit()

        home_button = tk.Button(new_frame, text="Home", command=self.admin_home_page)
        home_button.pack(pady=10)

    def view_entity_data(self, frame, entity):
        frame.destroy()

        fields_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=800)
        fields_frame.pack_propagate(False)
        fields_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(fields_frame, text=f"View data for {entity}").pack(pady=10)

        cursor.execute(f"SELECT * FROM {entity}")
        data = cursor.fetchall()

        # Create labels for the field names at the top
        entity_fields = self.get_entity_fields(entity)
        # Create a Treeview widget
        # Create a Treeview widget
        tree = ttk.Treeview(fields_frame, columns=entity_fields, show="headings")

        # Set up columns
        for field in entity_fields:
            tree.heading(field, text=field)
            tree.column(field, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Insert data rows
        for row in data:
            tree.insert("", "end", values=row)

        # Add the Treeview to the frame
        tree.pack(side=tk.TOP, fill=tk.BOTH)

        back_button = tk.Button(fields_frame, text="Back", command=lambda: self.view_data())
        back_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    conn = sqlite3.connect("Local_Championship.db")
    cursor = conn.cursor()

    root = tk.Tk()
    app = SportsDatabaseGUI(root)
    root.mainloop()