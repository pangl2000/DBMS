import sqlite3
import tkinter as tk
from tkinter import ttk

class SportsDatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Database Management")
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use the clam theme for a modern look
        self.root.geometry("1400x600")  # Set window size
        self.login_frame()

    def set_style(self, widget, background, foreground, font_size=10):
        self.style.configure(widget, background=background, foreground=foreground, font=("Helvetica", font_size, "bold"))

    def login_frame(self):
        login_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        home_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

    def admin_home_page(self):
        self.clear_screen()

        home_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        view_button = ttk.Button(home_frame, text="View data from DB", command=self.view_data)
        view_button.pack(pady=10)

        insert_button = ttk.Button(home_frame, text="Insert data to DB", command=self.insert_data)
        insert_button.pack(pady=10)

    def user_page_alpha(self):
        self.clear_screen()

        page_alpha_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        page_beta_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

            button = tk.Button(inner_frame, text="View Stats", command=lambda pid=player_id: self.user_show_player_details(pid, 
                                                                                                                           player_info))
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

        player_stats_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        group_stage_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
        group_stage_frame.pack_propagate(False)
        group_stage_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(group_stage_frame, text="Group Stage Information").pack(pady=10)

        # Add code for group stage information display

        back_button = tk.Button(group_stage_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

    def user_page_knockout_stage(self):
        self.clear_screen()

        knockout_stage_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
        knockout_stage_frame.pack_propagate(False)
        knockout_stage_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(knockout_stage_frame, text="Knockout Stage Information").pack(pady=10)

        # Add code for knockout stage information display

        back_button = tk.Button(knockout_stage_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

    def admin_page_alpha(self):
        self.clear_screen()

        page_alpha_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        page_beta_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

            button = tk.Button(inner_frame, text="View Stats", command=lambda pid=player_id: self.admin_show_player_details(pid, 
                                                                                                                            player_info))
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

        player_stats_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        group_stage_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
        group_stage_frame.pack_propagate(False)
        group_stage_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(group_stage_frame, text="Group Stage Information").pack(pady=10)

        # Add code for group stage information display

        back_button = tk.Button(group_stage_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def admin_page_knockout_stage(self):
        self.clear_screen()

        knockout_stage_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
        knockout_stage_frame.pack_propagate(False)
        knockout_stage_frame.pack(padx=20, pady=20)

        self.set_style("TLabel", "#3498db", "white", 14)  # Larger label style
        ttk.Label(knockout_stage_frame, text="Knockout Stage Information").pack(pady=10)

        # Add code for knockout stage information display

        back_button = tk.Button(knockout_stage_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def view_data(self):
        self.clear_screen()

        view_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        insert_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        fields_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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
            "Match": ["MatchID", "Date", "Time", "CourtID"],
            "Plays": ["HomeTeamID", "GuestTeamID", "MatchID"],
            "Includes": ["ChampionshipID", "MatchID"],
            "Referees": ["RefereeID", "MatchID"],
            "Player": ["PlayerID", "FirstName", "LastName", "DateOfBirth", "Nationality", "Height", "Weight", "Position", "TeamID", "JerseyNumber", "MatchID"],
            "PlayerStats": ["PlayerID", "MatchID", "MinutesPlayed", "RedCards", "YellowCards", "GoalsScored", "Shots", "ShotsOnTarget", "Passes", "Assists", "Offsides", "Tackles"],
            "Position": ["PlayerID", "Position"]
            # Add fields for other entities
        }
        return entity_fields_dict.get(entity, [])
    
    def insert_entity_data(self, frame, entity, entity_fields, values):
        frame.destroy()
        
        new_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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

        fields_frame = tk.Frame(self.root, bg="#3498db", width=1400, height=600)
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