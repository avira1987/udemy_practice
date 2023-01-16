from fpdf import FPDF
import webbrowser
from main import Bill, the_bill
class PDFReport:
    """
        Create a PDF file that contains data about 
        the flatmate such as their names, their due 
        amounts and the period of bill.
    """

    def __init__(self,filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay =str(round(flatmate1.pays(bill=the_bill,co_flatmate=flatmate2),2))
        flatmate2_pay =str(round(flatmate2.pays(bill=the_bill,co_flatmate=flatmate1),2))

        pdf = FPDF(orientation='P', unit='pt',format="A4")
        pdf.add_page()
        
        #Add icon
        pdf.image(name="house.png", w=30, h=30)

        #insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h= 80, txt="Flatmates Bill", border=0, align="C", ln=1)

        #Inser Period Lable and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #Inser name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)

        #Inser name and due amount lable and value
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)