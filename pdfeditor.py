import os
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_folder):
    with open(input_pdf_path, "rb") as input_pdf:
        pdf_reader = PdfReader(input_pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            output_pdf_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)
            print(f"Saved {output_pdf_path}")

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PdfWriter()
    for pdf in pdf_list:
        with open(pdf, "rb") as f:
            pdf_reader = PdfReader(f)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
    with open(output_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)
    print(f"Merged PDFs saved as {output_path}")

def rotate_pdf(input_pdf_path, output_path, rotation_angle=90):
    with open(input_pdf_path, "rb") as input_pdf:
        pdf_reader = PdfReader(input_pdf)
        pdf_writer = PdfWriter()
        for page in pdf_reader.pages:
            page.rotate(rotation_angle)
            pdf_writer.add_page(page)
        with open(output_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)
    print(f"Rotated PDF saved as {output_path}")

def extract_text_from_pdf(input_pdf_path):
    with open(input_pdf_path, "rb") as input_pdf:
        pdf_reader = PdfReader(input_pdf)
        text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    print("\nExtracted Text:\n")
    print(text)

def encrypt_pdf(input_pdf_path, output_path, password):
    pdf_writer = PdfWriter()
    with open(input_pdf_path, "rb") as input_pdf:
        pdf_reader = PdfReader(input_pdf)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        pdf_writer.encrypt(password)
        with open(output_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)
    print(f"Encrypted PDF saved as {output_path}")

def decrypt_pdf(input_pdf_path, output_path, password):
    with open(input_pdf_path, "rb") as input_pdf:
        pdf_reader = PdfReader(input_pdf)
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(password)
        pdf_writer = PdfWriter()
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        with open(output_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)
    print(f"Decrypted PDF saved as {output_path}")

def compress_pdf(input_pdf_path, output_path):
    with open(input_pdf_path, "rb") as input_pdf:
        pdf_reader = PdfReader(input_pdf)
        pdf_writer = PdfWriter()
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        with open(output_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)
    print(f"Compressed PDF saved as {output_path}")

def main():
    print("PDF Utility Program")
    print("1. Split PDF")
    print("2. Merge PDFs")
    print("3. Rotate PDF")
    print("4. Extract Text from PDF")
    print("5. Encrypt PDF")
    print("6. Decrypt PDF")
    print("7. Compress PDF")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        input_pdf_path = input("Enter the path of the PDF to split: ")
        output_folder = input("Enter the output folder: ")
        split_pdf(input_pdf_path, output_folder)

    elif choice == "2":
        pdf_list = input("Enter the paths of PDFs to merge (comma-separated): ").split(",")
        output_path = input("Enter the output PDF path: ")
        merge_pdfs(pdf_list, output_path)

    elif choice == "3":
        input_pdf_path = input("Enter the path of the PDF to rotate: ")
        output_path = input("Enter the output PDF path: ")
        angle = int(input("Enter rotation angle (90, 180, 270): "))
        rotate_pdf(input_pdf_path, output_path, angle)

    elif choice == "4":
        input_pdf_path = input("Enter the path of the PDF to extract text from: ")
        extract_text_from_pdf(input_pdf_path)

    elif choice == "5":
        input_pdf_path = input("Enter the path of the PDF to encrypt: ")
        output_path = input("Enter the output PDF path: ")
        password = input("Enter the password: ")
        encrypt_pdf(input_pdf_path, output_path, password)

    elif choice == "6":
        input_pdf_path = input("Enter the path of the encrypted PDF: ")
        output_path = input("Enter the output PDF path: ")
        password = input("Enter the password: ")
        decrypt_pdf(input_pdf_path, output_path, password)

    elif choice == "7":
        input_pdf_path = input("Enter the path of the PDF to compress: ")
        output_path = input("Enter the output PDF path: ")
        compress_pdf(input_pdf_path, output_path)

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
