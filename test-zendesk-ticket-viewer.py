ztv = __import__("zendesk-ticket-viewer")

import unittest

class testZendeskTicketViewer(unittest.TestCase):

	def test_display_one_ticket(self):
		
		symbol = zendesk-ticket-viewer.display_one_ticket()
		
#if menu selection 1, 2 or 3, call single ticket
#if menu selection = !, print error statement
#if menu selection > 3, print error statement

#if display ticket id valid, print ticket
#if display ticket id not valid, print error statement
#if display ticket id excepts KeyError, print error statement

#if show another ticket, Y, ask for new ticket id
#if show another ticket, N, go back to main menu
#if show another ticket, !, print error statement
#if show another ticket, 1, print error statement

#if url, email and password incorrect, print API unavailable or authentication failed statement
#if url, email and password correct, print authentication successful and load menu
if __name__ == "__main__":
	unittest.main()
