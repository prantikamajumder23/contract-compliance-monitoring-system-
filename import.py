from pypdf import PdfReader
from pathlib import Path
pdf_path=r"C:\Users\Puspita\OneDrive\Documents\Desktop\contract compliance\data\contracts\CARE--Standard_Goods-Vendor-Agreement.pdf"
def pdf_validate(pdf_path):
  path=Path(pdf_path)
  if not path.exists():
    print("pdf does not exist")
    return False
  if path.suffix.lower()!= ".pdf":
     print(" this file is not a pdf ")
     return False
  try:
   reader = PdfReader(pdf_path)
  except Exception:
    print("pdf cannot be opened")
    return False
  if len(reader.pages) ==0:
    print(" empty pdf ")
    return False
  print("pdf is valid ")
  print("pages:",len( reader.pages))
  return True

def extract_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    full_text = ""

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text:
           
            full_text += text + "\n"
        else:
            print(f"Page {page_number}: NO TEXT")

    return full_text


if pdf_validate(pdf_path):
  text = extract_pdf(pdf_path)
  print("Characters extracted:", len(text))
  print("\nExtracted Text:\n")
  print(text[:2000])
  print("Characters extracted:", len(text))
  output = r"C:\Users\Puspita\OneDrive\Documents\Desktop\contract compliance\data\processed\CARE--Standard_Goods-Vendor-Agreement.txt"
  with open(output,"w",encoding="utf-8") as f:
    print("Characters extracted:", len(text))
    f.write(text)
  print(" text saved successfully")

