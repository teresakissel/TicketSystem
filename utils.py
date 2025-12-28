import json # imports json files
import os # checks if a file exists

FILE_NAME = "tickets.json"  # Sets constant file name

def load_tickets(): # Defines function that will return a list of tickets
  if not os.path.exists(FILE_Name): # Checks if file exists
    return [] # Returns an empty list if it does not exist

    with open(FILE_NAME, "r") as file: # Opens file in read mode
      return json.load(file) # Reads data, converts to Python list, returns it to program

def save_tickets(): # Accepts tickets
  with open(FILE_NAME, "w") as file: # Opens file in write mode and can override data
    json.dump(tickets, file, indent=4) # Converts Python data to json, writes it to the file, and makes it human readable

def create_tickets(): # Add a new ticket
  ticket_id = len(tickets) + 1 # Assigns an ID to each ticket

customer = input("Enter customer name: ") # Collects ticket details, user input
issue_type = input("Enter issue type: ")
priority = input("Enter priority (Low/Medium/High): ")

ticket = { # Stores individual ticket as a dictionary
  "id": ticket_id,
  "customer": customer,
  "issue_type": issue_type,
  "priority": priority,
  "status": "Open:
}
tickets.append(ticket) # Adds ticket to list
print("Ticket created successfully.") # Provides confirmation message to user

def display_tickets(): # Checks all tickets
  if not tickets: # Checks if it is empty
    print("No tickets available.") # Responds to user
    return # Exits

for ticket in tickets: # Loops through each ticket
  print(f"ID: {ticket['id']} | " # Provides output to user
        f"Customer: {ticket['customer']} | "
        f"Issue: {ticket['issue_type']} | "
        f"Priority: {ticket['priority']} | "
        f"Status: {ticket['status']}")
def update_ticket_status(tickets): # Update an existing tickets status
  ticket_id = input("Enter ticket ID to update: ") # gathers input

for ticket in tickets: # Find a match
  if str(ticket["id"]) == ticket_id: # Convert ID to string
    new_status = input("Enter new status (Open/In Progress/Resolved): ") # Take user input
    ticket["status"] = new_status # Replace ticket status
    print("Ticket updated successfully") # Provide confirmation to user
    return # Exit function after completion
print("Ticket not found") # Returned if no match is found

