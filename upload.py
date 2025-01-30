import PyPDF2
import re
import json

def convert_pdf_to_text(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ' '.join(page.extract_text() or '' for page in pdf_reader.pages)
    
    text = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    with open("vault.txt", "a", encoding="utf-8") as vault_file:
        chunk = ""
        for sentence in sentences:
            if len(chunk) + len(sentence) + 1 < 1000:
                chunk += sentence + " "
            else:
                vault_file.write(chunk.strip() + "\n")
                chunk = sentence + " "
        if chunk:
            vault_file.write(chunk.strip() + "\n")
    
    print("PDF content appended to vault.txt")

if __name__ == "__main__":
    pdf_path = input("Enter the PDF file path: ").strip()
    convert_pdf_to_text(pdf_path)
