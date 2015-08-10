'''
AmtrakTicket parses the information in the PDF recived from Amtrak after
book a trip. It uses pypdfocr_gs from pypdfocr wrap ghost script to
convert PDFs to JPGS. Teseract is used for OCR.

USAGE:
    ticket = AmtrakTicket("ticket.pdf")
    ticket.reservation_number() # "366B20"

def test_origin(self):
    ticket = AmtrakTicket("ticket.pdf")
    ticket.origin() # "LAX"
'''
import glob
import pytesseract
from PIL import Image
from pypdfocr_gs import PyGs

class AmtrakTicket(object):
    ''' Parse info from Amtrak Ticket PDFs '''
    def __init__(self, file_name):
        self.file_name = file_name
        ghost_script = PyGs({})
        img = ghost_script.make_img_from_pdf(self.file_name)
        _, pages_glob = img
        pages = glob.glob(pages_glob)
        self.image = Image.open(pages[0])

    def reservation_number(self):
        ''' Returns the reservation number of a ticket '''
        section = self.image.crop((1968, 470, 2200, 545))
        return pytesseract.image_to_string(section)

    def origin(self):
        ''' Returns the abbreviated station name of a ticket '''
        section = self.image.crop((120, 580, 340, 750))
        return pytesseract.image_to_string(section)

if __name__ == '__main__':
    ticket = AmtrakTicket("ticket.pdf")
    print ticket.origin()
    print ticket.reservation_number()
