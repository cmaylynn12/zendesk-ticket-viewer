import sys, time
from zdesk import Zendesk, ZendeskError


def menu():

    flag = True

    while flag:

        print("------------------------------------------\nWelcome to the Zendesk Ticket Viewer\n\n"
              "Please enter one of the following options:\n\n   1. Display a single ticket\n   "
              "2. Display all tickets\n   "
              "3. Exit\n------------------------------------------")

        selection = str(input("Option: "))

        if selection is "1" or selection is "2":
            option(selection)

        elif selection is "3":
            sys.exit()

        else:
            print("\nThe option you have entered is invalid, please try again.")


def option(choice):

    if choice == "1":

        ticket_id = str(input("Please enter Ticket #: "))
        print("Searching database...")

        try:
            ticket = zendesk.ticket_show(id=ticket_id)['ticket']
            print("\n------------------------------------------" +
                  "\nTicket #" + str(ticket['id']) +
                  "\nSubject: " + ticket['subject'] +
                  "\nDescription: " + ticket['description'] +
                  "\nUpdated at: " + str(ticket['updated_at'].split("T")[0]) +
                  "\n------------------------------------------")

        except ZendeskError:
            print("\nSorry, the ticket # you have entered is invalid, please try again")

    elif choice == "2":

        ticket_list = zendesk.tickets_list()
        tickets = ticket_list['tickets']
        print("\n------------------------------------------")

        for ticket in tickets:
            print("Ticket #" + str(ticket['id']) +
                  "\nSubject: " + ticket['subject'] +
                  "\nDescription: " + ticket['description'] +
                  "\nUpdated at: " + ticket['updated_at'].split("T")[0] + "\n")

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

    try:
        zendesk = Zendesk(url, email, pwd)
        menu()

    except ZendeskError:
        print("Sorry, the API is currently unavailable, please try again later.")





