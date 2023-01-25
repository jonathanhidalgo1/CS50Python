from fpdf import FPDF
from PIL import Image

def main():
    text = input("name: ")
    create_pdf(text)
    
def create_pdf(text):   

    #create the PDF
    pdf = FPDF(orientation="portrait")
    #add a page
    pdf.add_page()
    # get the image
    img = Image.open("shirtificate.png")
    # resize the image and position it
    img = img.crop((0, 0, 593, 592)).resize((520, 520))
    pdf.image(img, x=15, y=65)
    #set font and size of first text
    pdf.set_font("Times", size=36)
    # create text to de center of the page
    pdf.cell(0, 40, txt="CS50 SHIRTIFICATE", new_x="LMARGIN", new_y="NEXT", align='C')
    #set font and size of second text
    pdf.set_font("Times", size=20)
    # set color
    pdf.set_text_color(255, 255, 255)
    # create text to de center of the page
    # here is where the user will custom the PDF
    pdf.cell(0, 130, txt=f"{text} took CS50", new_x="LMARGIN", new_y="NEXT", align='C')

    #save file
    pdf.output("pdf-with-image.pdf")
    
main()


