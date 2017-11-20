#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages')  #appends the path for modules to be used
from zdesk import Zendesk, ZendeskError

def menu():

    flag = True

    while flag: #while option is not set i.e: empty option, option that is not in the list, repeat until option is chosen or 3 to exit

        try:  #attempt to get an answer from user
            print("------------------------------------------\nWelcome to the Zendesk Ticket Viewer\n\n"  #displays menu to users
                  "Please enter one of the following options:\n\n   1. Display a single ticket\n   "
                  "2. Display all tickets\n   "
                  "3. Exit\n------------------------------------------")

            selection = str(input("Option: "))  #gets selection from user

            if selection is "1" or selection is "2":  #if user selects 1 or 2
                option(selection) #call option()

            elif selection is "3":  #if user selects 3
                sys.exit()  #exit the program

            else: #if user selects any integer that's not in the list
              print("\nSorry, the option you have selected is invalid, please select from the menu.") #print this statement

        except SyntaxError: #catch error to prevent app from crashing, if user gives empty input or input that is not an integer
            print("\nThe option you have entered is invalid, please try again.") #print this statement

def option(choice):

    if choice == "1": #if user selected 1
      
        ticket_id = str(input("Please enter Ticket #: ")) #get ticket id from user
        print("Searching database...")
      
        try:  #attempt to find ticket with id, ticked_id
          
          ticket = zendesk.ticket_show(id=ticket_id)['ticket']  
          print("\n------------------------------------------" +  
                "\nTicket #" + str(ticket['id']) +  #prints id
                "\nSubject: " + ticket['subject'] + #prints subject
                "\nDescription: " + ticket['description'] + #prints description
                "\nUpdated at: " + str(ticket['updated_at'].split("T")[0]) +  #prints updated_at
                "\n------------------------------------------")
          flag = False

        except ZendeskError:  #if ticket is not found
            print("\nSorry, the ticket # you have entered is invalid, please try again")  #print this statement

    elif choice == "2": #if user selected 2

        ticket_list = zendesk.tickets_list()  #list all tickets available
        tickets = ticket_list['tickets']  #get the 'ticket' section of ticket_list
        print("\n------------------------------------------")

        for ticket in tickets:  #loops through all tickets
            print("Ticket #" + str(ticket['id']) +  #prints id
                  "\nSubject: " + ticket['subject'] + #prints subject
                  "\nDescription: " + ticket['description'] + #prints description
                  "\nUpdated at: " + ticket['updated_at'].split("T")[0] + "\n") #prints updated_at

        print("------------------------------------------")

if __name__ == '__main__':

    print("\nLoading Zendesk Ticket Viewer...")
    box = 42
    sys.stdout.flush()

    for i in range(box):
        time.sleep(0.05)
        sys.stdout.write("▉")
        sys.stdout.flush()

    sys.stdout.write("\n")

    url = 'https://kmcha49.zendesk.com'
    email = 'kmcha49@student.monash.edu'
    pwd = 'BCompSci2015'

    try:  #attempts to initialise Zendesk account
        zendesk = Zendesk(url, email, pwd)  #if successful
        menu() #call menu()

    except ZendeskError:  #if error occurs
        print("Sorry, the API is currently unavailable, please try again later.") #print this statement
