'''
Tests for AmtrakTicket, to ensure they work with test ticket.
'''
import unittest
from amtrak import AmtrakTicket

class TestAmtrakTicketOCR(unittest.TestCase):
    ''' Class for Testing '''
    def test_reservation_number(self):
        ''' Test for reservation number '''
        ticket = AmtrakTicket("ticket.pdf")
        self.assertEqual(ticket.reservation_number(), "366B20")

    def test_origin(self):
        ''' Test for origin statation abbreviation '''
        ticket = AmtrakTicket("ticket.pdf")
        self.assertEqual(ticket.origin(), "LAX")

if __name__ == '__main__':
    unittest.main()
