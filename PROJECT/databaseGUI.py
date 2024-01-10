import sqlite3
import tkinter as tk
from tkinter import ttk

class SportsDatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Database Management")

        self.home_page()

    def home_page(self):
        self.clear_screen()

        home_frame = tk.Frame(self.root)
        home_frame.pack(padx=20, pady=20)

        tk.Label(home_frame, text="Welcome to Sports Database Management").pack(pady=10)

        view_button = tk.Button(home_frame, text="View", command=self.view_data)
        view_button.pack(pady=10)

        insert_button = tk.Button(home_frame, text="Insert", command=self.insert_data)
        insert_button.pack(pady=10)

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

        back_button = tk.Button(view_frame, text="Back", command=self.home_page)
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

        back_button = tk.Button(insert_frame, text="Back", command=self.home_page)
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

        home_button = tk.Button(new_frame, text="Home", command=self.home_page)
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

        # Display data in a listbox with scrollbar
        listbox = tk.Listbox(fields_frame, selectmode=tk.SINGLE)
        scrollbar = tk.Scrollbar(fields_frame, orient=tk.VERTICAL, command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)

        for row in data:
            formatted_row = ', '.join(str(value) if value is not None else "None" for value in row)
            listbox.insert(tk.END, formatted_row)
        
        listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        back_button = tk.Button(fields_frame, text="Back", command=lambda: self.view_data())
        back_button.pack(pady=10)

if __name__ == "__main__":
    # Connect to SQLite database
    conn = sqlite3.connect("Local_Championship.db")
    cursor = conn.cursor()  

    root = tk.Tk()
    root.geometry("800x600")  # Set a larger size for the window
    app = SportsDatabaseGUI(root)
    root.mainloop()

    


