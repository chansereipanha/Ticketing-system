from ticket import *

Help_Desk = Ticket()


def menu():

    Help_Desk.set_data()


    while True:
        menu = input("""
    Select:
    1. Add a ticket 
    2. List all ticket
    3. Respond to a ticket
    4. Statistics 
    5. Display a ticket information
    Choose: """)
        if menu == "1":
            Help_Desk.add_ticket()


        elif menu == "2":
            Help_Desk.list_all_ticket()

        elif menu == "3":
            Help_Desk.resolve_ticket()
        
        elif menu == "4":
            Help_Desk.statistic()
        
        elif menu == "5":
            Help_Desk.opening_a_ticket()




if __name__ == "__main__":
    menu()
