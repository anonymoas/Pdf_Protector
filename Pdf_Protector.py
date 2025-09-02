# So here we are going to create a pdf protector :

import PyPDF2
import sys


def create_password_protected_pdf(input_pdf,output_pdf,password): # function created 
    try:
        with open(input_pdf, 'rb') as pdf_file:                   #  opening the input file and read it 
            pdf_reader = PyPDF2.PdfReader(pdf_file)               # reading the input pdf as pdf_file
            pdf_writer = PyPDF2.PdfWriter()                       

            for page_number in range(len(pdf_reader.pages)):          # checking the pages using the above createdvariable & counting the pages
                pdf_writer.add_page(pdf_reader.pages[page_number])    # adding the pages to the output fie 
            pdf_writer.encrypt(password)                              # encrypting the file with password 

            with open(output_pdf, 'wb') as output_file:              
                pdf_writer.write(output_file)
            print(f"Password-protected PDF saved as {output_pdf}")

    except FileNotFoundError:
        print(f"The file {input_pdf} was not found")
    except PyPDF2.errors.PdfReadError:                                        ## error handling codes'''
        print(f"File {input_pdf} is not a valid PDF")
    except Exception as e:
        print(f"error : {e}")


def run():
    if len(sys.argv) !=2:
        print(f"Usage : python3 ./script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    
    output_pdf = input("Rename your PDF: ")
    password = input("Enter the password: ")

    create_password_protected_pdf(input_pdf,output_pdf,password)

if __name__ == "__main__":
    run()