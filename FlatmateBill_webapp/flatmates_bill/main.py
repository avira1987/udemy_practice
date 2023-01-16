# from flatmates_bill import Flat
# from reports import PDFReport
import Flat
    



the_bill = Flat.Bill(120, period= "April 2021")
john = Flat.Flatmate(name= "Joun",days_in_house=20)
mary = Flat.Flatmate(name="mary", days_in_house= 25)

print("John to pay:",john.pays(bill=the_bill, co_flatmate= mary))
print("Mary to pay:",mary.pays(bill=the_bill, co_flatmate=john))

# pdf_report =PDFReport(filename="report1.pdf")
# pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)