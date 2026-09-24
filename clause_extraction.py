from pathlib import Path
import re
clean = Path(r"C:\Users\Puspita\OneDrive\Documents\Desktop\contract compliance\data\processed\cleaned\CARE--Standard_Goods-Vendor-Agreement_clean.txt")
def read_text(path):
    with open(path,"r",encoding="utf-8")as f :
        return f.read()

clause_names = {

    "governing_law": [
        "governing law",
        "applicable law",
        "choice of law",
        "law and jurisdiction",
        "jurisdiction",
        "governing law and jurisdiction",
        "applicable laws",
        "legal jurisdiction"
    ],

    "scope_of_work": [
        "scope of work",
        "scope of services",
        "scope of service",
        "services",
        "description of services",
        "services to be provided",
        "work to be performed",
        "statement of work",
        "sow",
        "project scope",
        "deliverables",
        "description of work",
        "work scope"
    ],

    "payment_terms": [
        "payment terms",
        "payment",
        "payments",
        "payment conditions",
        "payment provisions",
        "fees and payment",
        "fees and expenses",
        "fees",
        "pricing",
        "pricing terms",
        "compensation",
        "compensation and payment",
        "consideration",
        "billing",
        "billing and payment",
        "invoicing",
        "invoice and payment",
        "price and payment",
        "commercial terms"
    ],

    "termination": [
        "termination",
        "termination clause",
        "termination rights",
        "termination and cancellation",
        "cancellation",
        "cancellation and termination",
        "termination of agreement",
        "termination of contract",
        "ending the agreement",
        "expiration and termination"
    ],

    "confidentiality": [
        "confidentiality",
        "confidential information",
        "confidentiality obligations",
        "confidentiality and non-disclosure",
        "non-disclosure",
        "non-disclosure agreement",
        "nda",
        "protection of confidential information",
        "confidential information and disclosure",
        "secrecy and confidentiality"
    ],

    "intellectual_property": [
        "intellectual property",
        "intellectual property rights",
        "ip rights",
        "ip ownership",
        "ownership of intellectual property",
        "ownership of ip",
        "proprietary rights",
        "copyright",
        "patents and intellectual property",
        "intellectual property ownership",
        "work product",
        "ownership of work product",
        "rights in work product"
    ],

    "liability": [
        "liability",
        "limitation of liability",
        "limitation on liability",
        "liability limitations",
        "liability and indemnification",
        "indemnity",
        "indemnification",
        "indemnities",
        "damages and liability",
        "responsibility and liability",
        "limits of liability",
        "exclusion of liability",
        "exclusion of damages",
        "limitation of damages"
    ],

    "force_majeure": [
        "force majeure",
        "force majeure events",
        "acts of god",
        "events beyond control",
        "events beyond the parties' control",
        "unforeseen events",
        "excusable delay",
        "delay due to circumstances beyond control",
        "hardship and force majeure"
    ],

    "renewal": [
        "renewal",
        "renewal terms",
        "renewal and extension",
        "extension",
        "term and renewal",
        "automatic renewal",
        "renewal and expiration",
        "contract extension",
        "extension of agreement",
        "extension of contract"
    ],

    "dispute_resolution": [
        "dispute resolution",
        "resolution of disputes",
        "dispute settlement",
        "dispute management",
        "disputes",
        "settlement of disputes",
        "arbitration",
        "arbitration and dispute resolution",
        "mediation",
        "mediation and arbitration",
        "claims and disputes",
        "dispute resolution and arbitration",
        "negotiation and dispute resolution"
    ]
}

def find_clause( names):
    text = read_text(clean)

    for name in names:
        match = re.search(
            rf"{re.escape(name)}(.*?)(?=\n\s*\d+\)\s*[A-Z][A-Z ]*:\s*|$)",
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            return match.group(1).strip()
            
    return None

def extract_all_clause_names():
    results ={}
    for name in clause_names:
        result= find_clause(clause_names)
        results[name] = result
      


extract_all_clause_names()