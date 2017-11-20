# Zendesk Ticket Viewer
Zendesk is a customer service tool that allows the creation and management of support tickets. The Zendesk Ticket Viewer displays ticket information from a Zendesk account. Tickets are the means of communication between Zendesk Support Agents and end users. This applications provides easy usage with its simple and learnable interface.
## Requirements
The Zendesk Ticket Viewer works on Python 3. Tested on Python 3.4.1.
### Installation
The request package is required for authentications and requests purposes
```
pip install requests
```
Zdesk
```
pip install zdesk
```
## Getting Started
### Instructions
#### How to set up on command-line
##### Enter the following line into the terminal
```
$ git clone https://github.com/cmaylynn12/zendesk-ticket-viewer.git
```
##### Followed by this line which will bring up the menu 
```
python3 zendesk-ticket-viewer.py
```
#### How to use
##### Select from options 1, 2 or 3
```
Welcome to the Zendesk Ticket Viewer

Please enter one of the following options:

   1. Display a single ticket
   2. Display all tickets
   3. Exit
------------------------------------------
Option: 
```
##### Option 1: Displays a single ticket
```
Please enter Ticket #: 3
------------------------------------------

Ticket #3
Subject: Query
Description: Hi I need help with a query.
Updated at: 2017-11-18

------------------------------------------
View another ticket? (Y/N): 
```
##### Option 2: Displays all tickets
```
------------------------------------------

Ticket #1
Subject: Sample ticket: Meet the ticket
Description: Hi Kimberley,

Emails, chats, voicemails, and tweets are captured in Zendesk Support as tickets. Start typing above to respond and click Submit to send. To test how an email becomes a ticket, send a message to support@kmcha49.zendesk.com.

Curious about what your customers will see when you reply? Check out this video:
https://demos.zendesk.com/hc/en-us/articles/202341799

Updated at: 2017-11-18

Ticket #2
Subject: Bro
Description: Bro?
Updated at: 2017-11-18

Ticket #3
Subject: Query
Description: Hi I need help with a query.
Updated at: 2017-11-18
.
.
.
------------------------------------------
```
##### Option 3: Exit the application
## Quickstart
```python
auth = ZendeskTicketViewer({your url}, {your email}, {your password})
main()
```
## Examples
##### Initialising Menu
```python
flag = True
while flag:

try:
  option = str(input("------------------------------------------\nWelcome to the Zendesk Ticket Viewer\n\nPlease enter one of the following options:\n\n   1. Display a single ticket\n   2. Display all tickets\n   3. Exit\n------------------------------------------\nOption: "))

	if option == "1":
	  auth.display_one_ticket()

  elif option == "2":
	  auth.display_all_tickets()

	elif option == "3":
		sys.exit()

	else:
		print("\nSorry, the option you have selected is invalid, please select from the menu.")
```
##### Displaying a single ticket (Option: 1)
```python
flag = True
while flag:
ticket_id = input("Please enter Ticket #: ")

  try:
	  if ticket_id == "B":
		  main()
				
		else:
			ticket = self.zendesk.ticket_show(id=ticket_id)['ticket']
			print("------------------------------------------\n")
			print("Ticket #" + str(ticket['id']) + "\n" + "Subject: " + ticket['subject'] + "\n" + "Description: " + ticket['description'] + "\n" + "Updated at: " + ticket['updated_at'].split("T")[0] + "\n")
			print("------------------------------------------")

			repeat_flag = True
					
			while repeat_flag:

			  repeat = input("View another ticket? (Y/N): ")

				if repeat == "Y" or repeat == "y":
				  repeat_flag = False

				elif repeat == "N" or repeat == "n":
					main()

				else:
					print("\nThe option you have selected is invalid, please enter Y or N.\n")

except KeyError:
  print("\nThe Ticket # you have entered is invalid, please try again or enter B to return to the main menu.\n")

except ZendeskError:
  print("\nThe Ticket # you have entered is invalid, please try again or enter B to return to the main menu.\n")
```
##### Displaying all tickets (Option: 2)
```python
if len(self.tickets_list) > 0:
  print("------------------------------------------\n")
	for ticket in self.tickets_list:
	  print("Ticket #" + str(ticket['id']) + "\n" + "Subject: " + ticket['subject'] + "\n" + "Description: " + ticket['description'] + "\n" + "Updated at: " + ticket['updated_at'].split("T")[0] + "\n")
  print("------------------------------------------")

else:
  print("There are currently no tickets available")
```
##### Exit (Option: 3)
```python
sys.exit()  #simply exit if user has selected Option: 3
```
## Contributors
- Kimberley May Lynn Chan <cmaylynn12@gmail.com>
## Built with
* Python 3.4
* Sublime Text 3
## Acknowledgements
[zdesk](https://github.com/fprimex/zdesk) - fprimex 