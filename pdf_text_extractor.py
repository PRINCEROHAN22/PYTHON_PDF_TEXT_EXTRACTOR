import PyPDF2

def extract_text_from_pdf(pdf_path, output_txt_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ''
        for page in reader.pages:
            full_text += page.extract_text() + '\n'

    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(full_text)

# Example usage:
pdf_path = 'sample.pdf'           # Replace with your PDF filename
output_txt_path = 'output.txt'    # Output text file
extract_text_from_pdf(pdf_path, output_txt_path)
print("Text extracted successfully!")