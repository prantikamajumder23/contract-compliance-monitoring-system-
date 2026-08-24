from pathlib import Path
import re
raw = Path(r"C:\Users\Puspita\OneDrive\Documents\Desktop\contract compliance\data\processed\raw")
clean = Path(r"C:\Users\Puspita\OneDrive\Documents\Desktop\contract compliance\data\processed\cleaned")

def read_text(path):
    with open(path,"r",encoding="utf-8")as f :
        return f.read()

def remove_markers(text):
    text=re.sub(r"Page\s+\d+\s+ of\d+","",text,flags=re.IGNORECASE)
    return text
def normalize_spaces(text) :
    text=re.sub(r"[ \t]+"," ",text)
    return text
def normalize_line(text):
    text= re.sub(r"\n\s*\n+","\n\n",text)
    return text
def clean_text(text):
    text=remove_markers(text)
    text=normalize_spaces(text)
    text=normalize_line(text)
    text=text.strip()
    return text
def save(path,text):
    with open(path,"w",encoding="utf-8") as f:
        f.write(text)
def process_contract(path):
    print (f"Preprocessing :{ path.name} ")
    raw_text = read_text(path)
    print(f"Original character :{len(raw_text)}")
    clean_file= clean_text(raw_text)
    print(f"Cleaned characters: {len(clean_file)}")

    output_name = path.stem + "_clean.txt"
    output_path = clean / output_name

    save(output_path, clean_file)

    print(f"Saved: {output_path}")
    print("-" * 50)

def main():
    clean.mkdir(parents=True,exist_ok=True)
    text_files = list(raw.glob("*.txt"))

    print("RAW FOLDER:", raw)
    print("FILES FOUND:", len(text_files))

    for path in text_files:
        print("FOUND:", path)
        process_contract(path)

  


if __name__ == "__main__":
    main()