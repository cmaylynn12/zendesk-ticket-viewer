#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages')  #appends the path for modules to be used
from zdesk import Zendesk, ZendeskError

class ZendeskTicketViewer():

  def __init__(self, url, email, password): 

    self.url, self.email, self.password = url, email, password #initalises with url, email and password
    self.zendesk = Zendesk(self.url, self.email, self.password) #Zendesk account
    self.tickets_list = self.zendesk.tickets_list()['tickets']  #get key: ticket of tickets_list
  
  def display_all_tickets(self):  #displays all tickets available in the Zendesk account
    
    if len(self.tickets_list) > 0:  #continue only if there exist a ticket
      print("------------------------------------------\n")
      for ticket in self.tickets_list:  #loop through all tickets and prints id, subject, description and updated_at
        print("Ticket #" + str(ticket['id']) + "\n" + "Subject: " + ticket['subject'] + "\n" + "Description: " + ticket['description'] + "\n" + "Updated at: " + ticket['updated_at'].split("T")[0] + "\n")
      print("------------------------------------------")

    else:
      print("There are currently no tickets available") #if no ticket is available, print this

  def display_one_ticket(self): #displays one ticket with a specific ticket_id, supplied by the user

    flag = True

    while flag:
        
      ticket_id = input("Please enter Ticket #: ")  #gets ticket_id from user

      try:
        if ticket_id == "B" or ticket_id == "b":  #if B, return to main menu
          main()
        
        else:
          ticket = self.zendesk.ticket_show(id=ticket_id)['ticket'] #obtain the ticket portion of tickets_list and print the ticket_id, subject, description and updated_at
          print("------------------------------------------\n")
          print("Ticket #" + str(ticket['id']) + "\n" + "Subject: " + ticket['subject'] + "\n" + "Description: " + ticket['description'] + "\n" + "Updated at: " + ticket['updated_at'].split("T")[0] + "\n")
          print("------------------------------------------")

          repeat_flag = True
          
          while repeat_flag:

            repeat = input("View another ticket? (Y/N): ")  #obtain yes or no to displaying another ticket

            if repeat == "Y" or repeat == "y":  #if user selects yes, ask for ticket_id again
              repeat_flag = False

            elif repeat == "N" or repeat == "n":  #else if user selects no, go back to main menu
              main()

            else:
              print("\nThe option you have selected is invalid, please enter Y or N.\n")  #else prompt user to enter only Y and N

      except KeyError:  #catches error if symbol is considered a key and cannot be found, prevents the application from crashing
        print("\nThe Ticket # you have entered is invalid, please try again or enter B to return to the main menu.\n")

      except ZendeskError:  #catches error if the key is not in tickets_list, prevents the application from crashing 
        print("\nThe Ticket # you have entered is invalid, please try again or enter B to return to the main menu.\n")

def main():

  flag = True

  while flag: #while no desired input is obtained

    #ask user for a selection from the menu
    option = str(input("------------------------------------------\nWelcome to the Zendesk Ticket Viewer\n\nPlease enter one of the following options:\n\n   1. Display a single ticket\n   2. Display all tickets\n   3. Exit\n------------------------------------------\nOption: "))

    if option == "1": #if user selects 1
      auth.display_one_ticket() #call function to display one ticket

    elif option == "2": #if user selects 2
      auth.display_all_tickets()  #call function to display all tickets

    elif option == "3": #if user selects 3
      sys.exit()  #exit the application

    else:
      print("\nSorry, the option you have selected is invalid, please select from the menu.") #if user selects something that is not in the menu, prompt user to enter only 1, 2 or 3

if __name__ == "__main__":

  try:
    auth = ZendeskTicketViewer("https://" + str(sys.argv[1]) + ".zendesk.com", sys.argv[2], sys.argv[3]) #calls the ZendeskTicketViewer class
    #if authentication is successful, do this
    print("\nAuthentication Successful.\nLoading Zendesk Ticket Viewer...")
    sys.stdout.flush()

    for _ in range(42):  #performs loading bar
      time.sleep(0.05)
      sys.stdout.write("▉")
      sys.stdout.flush()

    sys.stdout.write("\n")
    main()

  except ZendeskError:  #if authentication failed, print this
    print("\nSorry, the API is currently unavailable or the authentication failed. Please try again later.\n")
