from pathlib import Path
import re
clean = Path(r"C:\Users\Puspita\OneDrive\Documents\Desktop\contract compliance\data\processed\cleaned\CARE--Standard_Goods-Vendor-Agreement_clean.txt")
def read_text(path):
    with open(path,"r",encoding="utf-8")as f :
        return f.read()

STANDARD_CLAUSES = [
    "payment_terms",
    "termination",
    "confidentiality",
    "intellectual_property",
    "liability",
    "force_majeure",
    "governing_law",
    "dispute_resolution",
    "scope_of_work",
    "renewal"
]
CLAUSE_PATTERNS = {
    "scope_of_work": [
        r"scope\s+of\s+(?:work|services)",
        r"services\s+to\s+be\s+provided",
        r"description\s+of\s+(?:goods|services)",
        r"deliverables"
    ],

    "payment_terms": [
        r"payment\s+terms?",
        r"terms?\s+of\s+payment",
        r"payment\s+and\s+invoicing",
        r"pricing\s+and\s+payment",
        r"invoicing\s+and\s+payment"
    ],

    "termination": [
        r"termination",
        r"termination\s+of\s+(?:the\s+)?agreement",
        r"termination\s+and\s+suspension"
    ],

    "confidentiality": [
        r"confidentiality",
        r"confidential\s+information",
        r"non[-\s]?disclosure",
        r"confidentiality\s+and\s+non[-\s]?disclosure"
    ],

    "intellectual_property": [
        r"intellectual\s+property",
        r"intellectual\s+property\s+rights?",
        r"ownership\s+of\s+intellectual\s+property",
        r"proprietary\s+rights?"
    ],

    "liability": [
        r"liability",
        r"limitation\s+of\s+liability",
        r"limitation\s+of\s+liabilities",
        r"liabilities"
    ],

    "force_majeure": [
        r"force\s+majeure",
        r"acts?\s+of\s+god",
        r"events?\s+beyond\s+(?:the\s+)?control"
    ],

    "governing_law": [
        r"governing\s+law",
        r"applicable\s+law",
        r"law\s+and\s+jurisdiction",
        r"jurisdiction"
    ],

    "dispute_resolution": [
        r"dispute\s+resolution",
        r"resolution\s+of\s+disputes?",
        r"dispute\s+settlement",
        r"arbitration",
        r"arbitration\s+and\s+dispute\s+resolution"
    ],

    "renewal": [
        r"renewal",
        r"automatic\s+renewal",
        r"extension\s+of\s+(?:the\s+)?agreement"
    ]
}
def extract_clauses(text):
  extracted = {}

  for clause_name, patterns in CLAUSE_PATTERNS.items():

        found = None

        for pattern in patterns:

            full_pattern = (
                pattern
                + r"(.*?)(?=\n\s*\d+[\.\)]\s+|\Z)"
            )

            match = re.search(
                full_pattern,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if match:
                found = match.group(0).strip()
                break

        extracted[clause_name] = found

  return extracted
def standardize_clauses(extracted_clauses):

    standardized = {}

    for clause in STANDARD_CLAUSES:

        if clause in extracted_clauses:
            standardized[clause] = extracted_clauses[clause]

        else:
            standardized[clause] = None

    return standardized


if __name__ == "__main__":

    text = read_text(clean)

    extracted_clauses = extract_clauses(text)

    result = standardize_clauses(extracted_clauses)
    print(result)

    