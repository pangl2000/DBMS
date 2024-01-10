import sqlite3
import tkinter as tk
from tkinter import ttk    

class SportsDatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Database Management")
        self.login_frame()

    def login_frame(self):
        login_frame = tk.Frame(self.root)
        login_frame.pack(padx=20, pady=20)

        tk.Label(login_frame, text="Login/Sign-up").pack(pady=10)

        tk.Label(login_frame, text="Username").pack()
        username_entry = tk.Entry(login_frame)
        username_entry.pack()

        tk.Label(login_frame, text="Password").pack()
        password_entry = tk.Entry(login_frame, show="*")
        password_entry.pack()

        login_button = tk.Button(login_frame, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get()))
        login_button.pack(pady=10)

        signup_button = tk.Button(login_frame, text="Sign Up", command=self.signup)
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

        home_frame = tk.Frame(self.root)
        home_frame.pack(padx=20, pady=20)

        tk.Label(home_frame, text="Welcome to Local Championship").pack(pady=10)

        # Add buttons for pages Alpha and Beta
        alpha_button = tk.Button(home_frame, text="Team Ranking", command=self.user_page_alpha)
        alpha_button.pack(pady=10)

        beta_button = tk.Button(home_frame, text="Player Ranking", command=self.user_page_beta)
        beta_button.pack(pady=10)

    def admin_home_page(self):
        self.clear_screen()

        home_frame = tk.Frame(self.root)
        home_frame.pack(padx=20, pady=20)

        tk.Label(home_frame, text="Welcome to Local Championship Database Management").pack(pady=10)

        # Add buttons for pages Alpha and Beta
        alpha_button = tk.Button(home_frame, text="Team Ranking", command=self.page_alpha)
        alpha_button.pack(pady=10)

        beta_button = tk.Button(home_frame, text="Player Ranking", command=self.page_beta)
        beta_button.pack(pady=10)

        view_button = tk.Button(home_frame, text="View data from DB", command=self.view_data)
        view_button.pack(pady=10)

        insert_button = tk.Button(home_frame, text="Insert data to DB", command=self.insert_data)
        insert_button.pack(pady=10)

    def user_page_alpha(self):
        self.clear_screen()

        page_alpha_frame = tk.Frame(self.root)
        page_alpha_frame.pack(padx=20, pady=20)

        tk.Label(page_alpha_frame, text="Team Ranking based on Goals Scored").pack(pady=10)

        # Add code to fetch and display team ranking based on goals scored from the database

        back_button = tk.Button(page_alpha_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

    def user_page_beta(self):
        self.clear_screen()

        page_beta_frame = tk.Frame(self.root)
        page_beta_frame.pack(padx=20, pady=20)

        tk.Label(page_beta_frame, text="Player Ranking based on Goals Scored").pack(pady=10)

        # Add code to fetch and display player ranking based on goals scored from the database

        back_button = tk.Button(page_beta_frame, text="Back", command=self.user_home_page)
        back_button.pack(pady=10)

    def page_alpha(self):
        self.clear_screen()

        page_alpha_frame = tk.Frame(self.root)
        page_alpha_frame.pack(padx=20, pady=20)

        tk.Label(page_alpha_frame, text="Team Ranking based on Goals Scored").pack(pady=10)

        # Add code to fetch and display team ranking based on goals scored from the database

        back_button = tk.Button(page_alpha_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def page_beta(self):
        self.clear_screen()

        page_beta_frame = tk.Frame(self.root)
        page_beta_frame.pack(padx=20, pady=20)

        tk.Label(page_beta_frame, text="Player Ranking based on Goals Scored").pack(pady=10)

        # Add code to fetch and display player ranking based on goals scored from the database

        back_button = tk.Button(page_beta_frame, text="Back", command=self.admin_home_page)
        back_button.pack(pady=10)

    def view_data(self):
        self.clear_screen()

        view_frame = tk.Frame(self.root)
        view_frame.pack(padx=20, pady=20)

        tk.Label(view_frame, text="Local Championship's Data").pack(pady=10)

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

        insert_frame = tk.Frame(self.root)
        insert_frame.pack(padx=20, pady=20)

        tk.Label(insert_frame, text="Insert to Database").pack(pady=10)

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

        fields_frame = tk.Frame(self.root)
        fields_frame.pack(padx=20, pady=20)

        tk.Label(fields_frame, text=f"Insert data for {entity}").pack(pady=10)

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
        
        new_frame = tk.Frame(self.root)
        new_frame.pack(padx=20, pady=20)

        tk.Label(new_frame, text=f"Inserting data for {entity}").pack(pady=10)
        # Add code to retrieve data from entry fields and insert into the database
        # Extract values from entry widgets
        

        # Create a placeholder string for SQL VALUES clause
        values_placeholder = "(" + ", ".join(["?" for _ in values]) + ")"

        # Execute the SQL INSERT statement
        cursor.execute(f"INSERT INTO {entity} ({', '.join(entity_fields)}) VALUES {values_placeholder}", values)
        conn.commit()

        home_button = tk.Button(new_frame, text="Home", command=self.admin_home_page)
        home_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def view_entity_data(self, frame, entity):
        frame.destroy()

        fields_frame = tk.Frame(self.root)
        fields_frame.pack(padx=20, pady=20)

        tk.Label(fields_frame, text=f"View data for {entity}").pack(pady=10)

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

if __name__ == "__main__":
    # Connect to SQLite database
    conn = sqlite3.connect("Local_Championship.db")
    cursor = conn.cursor()  

    root = tk.Tk()
    root.geometry("1400x600")  # Set a larger size for the window
    app = SportsDatabaseGUI(root)
    root.mainloop()