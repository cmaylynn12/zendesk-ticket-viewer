# Zendesk Ticket Viewer

Zendesk is a customer service tool that allows the creation and management of support tickets. The Zendesk Ticket Viewer displays ticket information from a Zendesk account. Tickets are the means of communication between Zendesk Support Agents and end users. 

## Getting Started

## Quickstart
```python
import sys, time
from zdesk import Zendesk

url = {your url}
email = {your email}
password = {your password}

try:
  zendesk = Zendesk(url, email, pwd)  #authenticates with url, email and password
  menu()

except ZendeskError:  #if there is an error, assume API is unavailable
  print("Sorry, the API is currently unavailable, please try again later.")
```
## Examples
##### Initialising Menu
```python
def menu():

    flag = True

    while flag:
        #prints the title and lists available actions, in this case option 1, 2 and 3
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
```
##### Displaying a single ticket (Option: 1)
```python
ticket_id = str(input("Please enter Ticket #: ")) #asks for a specific ticket ID
print("Searching database...")

  try:
    ticket = zendesk.ticket_show(id=ticket_id)['ticket'] #accesses the ticket, ticket_id
    print("\n------------------------------------------" +
          "\nTicket #" + str(ticket['id']) +  #prints id
          "\nSubject: " + ticket['subject'] + #prints subject
          "\nDescription: " + ticket['description'] + #prints description
          "\nUpdated at: " + str(ticket['updated_at'].split("T")[0]) +  #prints updated_at
          "\n------------------------------------------")

  except ZendeskError:  #if ticket_id does not exist, print this
    print("\nSorry, the ticket # you have entered is invalid, please try again")
```
##### Displaying all tickets (Option: 2)
```python
ticket_list = zendesk.tickets_list()
tickets = ticket_list['tickets']  #accesses the ticket section in ticket list
print("\n------------------------------------------")

  for ticket in tickets:  #goes through all available tickets
    print("Ticket #" + str(ticket['id']) +  #prints id
    "\nSubject: " + ticket['subject'] + #prints subject
    "\nDescription: " + ticket['description'] + #print description
    "\nUpdated at: " + ticket['updated_at'].split("T")[0] + "\n") #prints updated_at

  print("------------------------------------------")
```
##### Exit (Option: 3)
```python
sys.exit()  #simply exit if user has selected Option: 3
```

## Contributors

- Kimberley May Lynn Chan <cmaylynn12@gmail.com>

---

## Requirements

---

## Built with
Python 3.4

PyCharm

Sublime Text 3

---

## License and Copyright