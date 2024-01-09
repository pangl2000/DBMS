import sqlite3
from tkinter import *
from tkinter import ttk

# Connect to SQLite database
conn = sqlite3.connect("Local_Championship.db")
cursor = conn.cursor()

# Create Tkinter window
root = Tk()
root.title("Database Management System")
root.geometry("800x600")  # Set a larger size for the window

# Stack to keep track of previous states for navigation
state_stack = []

def on_operation_select(event):
    # Function to handle operation selection (View or Insert)
    selected_operation = operation_combobox.get()

    # Clear previous widgets
    clear_widgets()

    if selected_operation == "View":
        create_view_widgets()
    elif selected_operation == "Insert":
        create_insert_widgets()

# Function to push the current state to the stack and call a new state
def push_state(new_state_function):
    state_stack.append(new_state_function)

# Function to handle entity selection for viewing data
def on_view_entity_select(event):
    selected_entity = view_entity_combobox.get()

    # Clear previous widgets
    clear_widgets()

    # Display data for the selected entity
    view_data(selected_entity)

    # Add "Back" button for navigation
    back_button = Button(root, text="Back", command=pop_state)
    back_button.pack()

# Function to handle entity selection for insertion
def on_insert_entity_select(event):
    selected_entity = insert_entity_combobox.get()

    # Clear previous widgets
    clear_widgets()

    # Display entry fields for inserting data into the selected entity
    create_insert_entity_widgets(selected_entity)

    # Add "Back" button for navigation
    back_button = Button(root, text="Back", command=pop_state)
    back_button.pack()

# Function to handle navigation back
def pop_state():
    if state_stack:
        previous_state = state_stack.pop()
        clear_widgets()
        previous_state()

# Function to display data for the selected entity
def view_data(entity):
    cursor.execute(f"SELECT * FROM {entity}")
    data = cursor.fetchall()

    # Display data in a listbox
    listbox = Listbox(root)
    for row in data:
        listbox.insert(END, row)
    listbox.pack()

# Function to create widgets for viewing data
def create_view_widgets():
    global view_entity_combobox

    # Dropdown menu for selecting entity to view
    view_entity_combobox = ttk.Combobox(root, values=["Court", "Team"])  # Add more entities as needed
    view_entity_combobox.set("Select Entity")
    view_entity_combobox.pack()
    view_entity_combobox.bind("<<ComboboxSelected>>", on_view_entity_select)

    # Add "Back" button for navigation
    back_button = Button(root, text="Back", command=pop_state)
    back_button.pack()

# Function to create widgets for inserting data
def create_insert_widgets():
    global insert_entity_combobox

    # Dropdown menu for selecting entity to insert
    insert_entity_combobox = ttk.Combobox(root, values=["Court", "Team"])  # Add more entities as needed
    insert_entity_combobox.set("Select Entity")
    insert_entity_combobox.pack()
    insert_entity_combobox.bind("<<ComboboxSelected>>", on_insert_entity_select)

    # Add "Back" button for navigation
    back_button = Button(root, text="Back", command=pop_state)
    back_button.pack()

# Function to create entry widgets for inserting data into the selected entity
def create_insert_entity_widgets(entity):
    if entity == "Court":
        create_court_widgets_for_insert()
    elif entity == "Team":
        create_team_widgets_for_insert()
    # Add more cases for other entities

# Function to create entry widgets for Court entity insertion
def create_court_widgets_for_insert():
    global court_name_entry, capacity_entry, location_entry

    court_name_label = Label(root, text="Court Name:")
    court_name_entry = Entry(root)

    capacity_label = Label(root, text="Capacity:")
    capacity_entry = Entry(root)

    location_label = Label(root, text="Location:")
    location_entry = Entry(root)

    court_name_label.pack()
    court_name_entry.pack()

    capacity_label.pack()
    capacity_entry.pack()

    location_label.pack()
    location_entry.pack()

    # Button for inserting Court entity
    insert_button = Button(root, text="Insert Court", command=insert_court)
    insert_button.pack()

# Function to create entry widgets for Team entity insertion
def create_team_widgets_for_insert():
    global team_name_entry, coach_fname_entry, coach_lname_entry

    team_name_label = Label(root, text="Team Name:")
    team_name_entry = Entry(root)

    coach_fname_label = Label(root, text="Coach First Name:")
    coach_fname_entry = Entry(root)

    coach_lname_label = Label(root, text="Coach Last Name:")
    coach_lname_entry = Entry(root)

    team_name_label.pack()
    team_name_entry.pack()

    coach_fname_label.pack()
    coach_fname_entry.pack()

    coach_lname_label.pack()
    coach_lname_entry.pack()

    # Button for inserting Team entity
    insert_button = Button(root, text="Insert Team", command=insert_team)
    insert_button.pack()

# Function to insert data into the Court entity
def insert_court():
    court_name = court_name_entry.get()
    capacity = capacity_entry.get()
    location = location_entry.get()

    cursor.execute("INSERT INTO Court (CourtName, Capacity, Location) VALUES (?, ?, ?)", (court_name, capacity, location))
    conn.commit()
    pop_state()

# Function to insert data into the Team entity
def insert_team():
    team_name = team_name_entry.get()
    coach_fname = coach_fname_entry.get()
    coach_lname = coach_lname_entry.get()

    cursor.execute("INSERT INTO Team (TeamName, TeamCoachFname, TeamCoachLname) VALUES (?, ?, ?)", (team_name, coach_fname, coach_lname))
    conn.commit()
    pop_state()

# Function to clear the widgets in the UI
def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

# Dropdown menu for operation selection (View or Insert)
operation_combobox = ttk.Combobox(root, values=["View", "Insert"])
operation_combobox.set("Select Operation")
operation_combobox.pack()
operation_combobox.bind("<<ComboboxSelected>>", on_operation_select)

# Run the Tkinter event loop
root.mainloop()

# Close the database connection when the GUI is closed
conn.close()
