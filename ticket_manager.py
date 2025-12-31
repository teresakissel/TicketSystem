from utils import load_tickets, save_tickets, create_tickets, display_tickets, update_ticket_status
def main():
  tickets = load_tickets(tickets)

  while True:
    print("n=== Banking Support Ticket System ===")
    print("1. Create Support Ticket")
    print("2. View All Tickets")
    print("3. Update Ticket Status")
    print("4. Exit")

    choice = input("Enter Selection: ")

    if choice == "1":
      create_tickets(tickets)
    elif choice == "2":
      display_tickets(tickets)
    elif choice == "3":
      update_ticket_status(tickets)
    elif choice == "4":
      save_tickets(tickets)
      print("Exiting system. Tickets saved.")
      break
    else:
      print("Invalid Selection. Try again.")

if __name__ == "__main__":
  main()
  
