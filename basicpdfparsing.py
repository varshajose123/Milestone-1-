import fitz  

def parse_pdf(file_path):
    pdf_document = fitz.open(file_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        images = page.get_images(full=True)
        print(f"Page {page_num + 1}")
        print("Text:\n", text)
        print("Images:\n", images)

if __name__ == "__main__":
    parse_pdf("sample.pdf")
