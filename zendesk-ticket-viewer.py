import requests
import sys
import time


def menu():

    flag = True

    while flag:

        try:
            print("------------------------------------------\nWelcome to the Zendesk Ticket Viewer\n"
                  "Please enter one of the following options:\n\n   1. Display a single ticket\n   "
                  "2. Display all tickets\n   "
                  "3. Exit\n------------------------------------------")

            selection = str(input("Option: "))

            if selection is "1" or selection is "2":
                option(selection)

            elif selection is "3":
                sys.exit()

            else:
                print("\nThe option you have entered is invalid, please try again.\n")

        except SyntaxError:

            print("Oops, there was no value entered. Please choose from the options.\n")


def option(choice):

    if choice == "1":

        ticket_id = str(input("Please enter Ticket #: "))
        print()
        tix = data['tickets']

        id_list = []

        for ticket in tix:
            id_list.append(str(ticket['id']))

        if ticket_id in id_list:
            print("------------------------------------------")
            print("Ticket #" + str(ticket_id))
            print("Subject: " + tix[int(ticket_id)-1]['subject'])
            print("Description: " + tix[int(ticket_id)-1]['description'])
            print("Updated at: " + tix[int(ticket_id)-1]['updated_at'].split("T")[0] + "\n")
            print("------------------------------------------\n")

        else:
            print("Sorry, the ticket # is invalid, please try again.\n")

    elif choice == "2":

        ticket_list = data['tickets']

        print("\n------------------------------------------")

        for ticket in ticket_list:
            print("Ticket #" + str(ticket['id']))
            print("Subject: " + ticket['subject'])
            print("Description: " + ticket['description'])
            print("Updated at: " + ticket['updated_at'].split("T")[0] + "\n\n")

        print("------------------------------------------\n")

if __name__ == '__main__':

    print("\nLoading Zendesk Ticket Viewer...")

    toolbar_width = 42

    sys.stdout.flush()

    for i in range(toolbar_width):
        time.sleep(0.05)
        sys.stdout.write("▇")
        sys.stdout.flush()

    sys.stdout.write("\n")

    url = 'https://kmcha49.zendesk.com/api/v2/tickets.json'
    email = 'kmcha49@student.monash.edu'
    pwd = 'BCompSci2015'

    print()
    response = requests.get(url, auth=(email, pwd))

    data = response.json()

    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    else:
        menu()