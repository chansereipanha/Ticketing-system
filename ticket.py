
class Ticket:


        
        def set_data(self):
                self.ticket_list_closed = []
                self.ticket_list_open = []
                self.ticket_counter = 2000
                self.num_of_open_ticket = 0
                self.status = ""
                self.num_of_closed_ticket = 0
                self.response = ""
                self.ticket_list = []
                self.status_open = "Open"
                self.status_closed = "Closed"


        def add_ticket(self):
                self.staff_id = input("Please enter your Staff ID: ")
                self.name = input("Please enter your name: ")
                self.email = input("Please enter your email: ")
                self.desc_of_issue = input("Please tell us what issues you need help with: ")
                self.x = self.status.replace("", "Open")

                

                self.ticket_counter += 1


                self.ticket_list_open.append(f"""
        --------{self.ticket_counter}---------------------
        Staff ID: {self.staff_id}
        Name: {self.name}
        Email: {self.email} 
        Description: {self.desc_of_issue}
        Status: {self.x}
        Response: {self.response}
        -------------------------------------------------
        """)
                
                if self.desc_of_issue == "Password Change":
                
                        self.new_password = self.staff_id[:2]+ self.name[:3]
                        print("Your new password is: ", self.new_password)
                        self.ticket_list_closed.append(self.desc_of_issue == "Password Change")
                        self.ticket_list_open.remove(self.desc_of_issue == "Password Change")

                        


                
        def list_all_ticket(self):
                self.ticket_list =  self.ticket_list_open + self.ticket_list_closed
                for ticket in self.ticket_list:
                        print(ticket)
        

        def resolve_ticket(self):
                self.ticket_list_open_len = len(self.ticket_list_open)
                self.ticket_list_closed_len = len(self.ticket_list_closed)




                if self.ticket_list_open_len == 1:
                        self.ticket_selector = input("""There is currently 1 ticket available. Would you like to respond to it?(y/n)     
        Answer: """)
                        if self.ticket_selector.lower() == "y":
                                print(self.ticket_list_open[0])
                                self.response_answer = input("Respond: ")
                        
                        submit_response = input("""Would you like to submit your response?(y/n)
        Answer: """)    
                        if submit_response == "y":

                                self.ticket_list_closed.append(self.ticket_list_open[0])
                        
                                self.ticket_list_open.remove(self.ticket_list_open[0])
                                
                        
                        
                elif self.ticket_list_open_len > 1:
                        self.ticket_selector = int(input(f"Which ticket from 1 to {self.ticket_list_open_len} would you like to respond to: "))
                        self.ticket_selector -= 1
                        self.response_ticket = self.ticket_list_open[self.ticket_selector]
                        print(self.response_ticket)
                        self.response = input("Respond: ")
                        submit_response = input("""Would you like to submit your response?(y/n)
        Answer: """)    
                        if submit_response == "y":
                                self.ticket_list_closed.append(self.response_ticket)
                                self.ticket_list_open.remove(self.response_ticket)
                elif self.ticket_list_open_len <1:
                        print("There are currently no tickets to respond to")

                        

        def statistic(self):
                self.ticket_list_open_len = len(self.ticket_list_open)
                self.ticket_list_closed_len = len(self.ticket_list_closed)
                self.ticket_list =  self.ticket_list_open + self.ticket_list_closed
                self.ticket_list_len = len(self.ticket_list)
                ticket_statistic_option = input("""
        Which tickets statistic would you like to see?
        1. Open tickets
        2. Closed tickets
        3. Tickets Created
        Answer: """)
                if ticket_statistic_option == "1":
                        print(f"There are currently {self.ticket_list_open_len} open tickets available")
                elif ticket_statistic_option == "2":
                        print(f"There currently {self.ticket_list_closed_len} ticket closed")
                elif ticket_statistic_option == "3":
                        print(f"There currently {self.ticket_list_len} ticket created")
                else:
                        print("Please select option 1 or option 2")

        def opening_a_ticket(self):
                self.ticket_list_open_len = len(self.ticket_list_open)
                self.ticket_list_closed_len = len(self.ticket_list_closed)
                self.ticket_list =  self.ticket_list_open + self.ticket_list_closed
                self.ticket_list_len = len(self.ticket_list)


                if self.ticket_list_len == 1:
                        ticket_selector1 = input("""There is currently 1 ticket available. Would you like to check it?(y/n)     
Answer: """)
                        if ticket_selector1.lower() == "y":
                                for ticket in self.ticket_list:
                                        print(ticket)
                if self.ticket_list_len > 1:
                        for ticket in self.ticket_list:
                                print(ticket)
                        self.ticket_selector2 = int(input(f"Which ticket from 1 to {self.ticket_list_len} would you like to respond to: "))
                        self.ticket_selector2 -= 1
                        self.ticket_preview = self.ticket_list[self.ticket_selector2]
                        print(self.ticket_preview)





        

