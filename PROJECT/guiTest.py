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
            entries.append()

        cursor.execute("INSERT INTO {} {} VALUES {}".format(entity, entity_fields, entries))
        conn.commit()

        insert_button = tk.Button(fields_frame, text="Insert", command=lambda: self.insert_entity_data(entity))
        insert_button.pack(pady=10)

        back_button = tk.Button(fields_frame, text="Back", command=lambda: self.insert_data())
        back_button.pack(pady=10)

    def get_entity_fields(self, entity):
        # Add code to retrieve the fields of the selected entity from the database or another source
        # For simplicity, using predefined fields for each entity here
        entity_fields_dict = {
            "Court": ["CourtName", "Capacity", "Location"],
            "Championship": ["ChampionshipName", "StartDate", "EndDate", "Description"],
            # Add fields for other entities
        }
        return entity_fields_dict.get(entity, [])

    def insert_entity_data(self, entity):
        # Add code to retrieve data from entry fields and insert into the database
        print(f"Inserting data for {entity}")

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

        # Display data in a listbox
        listbox = tk.Listbox(root)
        for row in data:
            listbox.insert(tk.END, row)
        listbox.pack()

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

    


