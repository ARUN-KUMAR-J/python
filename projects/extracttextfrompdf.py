import PyPDF2

with open('D:/resume/RESUME.pdf','rb') as f:
    pdfreader=PyPDF2.PdfReader(f)
    num_pages=len(pdfreader.pages)
    print(f'Number of pages: {num_pages}')
    for i in range(num_pages):
        page=pdfreader.pages[i]
        text=page.extract_text()
        print(text)