import json
from pathlib import Path
import re
BASE_DIR = Path(
    r"C:\Users\Puspita\OneDrive\Documents\Desktop\contract compliance"
)

STANDARDIZED_DIR = BASE_DIR / "data" / "processed" / "standard"
COMPLIANCE_DIR = BASE_DIR / "data" / "processed" / "compliance"
results = {
    "payment_terms": {
        "required": True,
        "max_payment_days": 30
    },

    "termination": {
        "required": True
    },

    "confidentiality": {
        "required": True
    },

    "intellectual_property": {
        "required": True
    },

    "liability": {
        "required": True
    },

    "force_majeure": {
        "required": True
    },

    "governing_law": {
        "required": True
    },

    "dispute_resolution": {
        "required": True
    },

    "scope_of_work": {
        "required": True
    },

    "renewal": {
        "required": True
    }
}


def check_payment_terms(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Payment terms clause is missing."
        }

    match = re.search(r'(\d+)\s*(?:calendar\s*)?days?', clause, re.IGNORECASE)

    if not match:
        return {
            "status": "REVIEW",
            "reason": "Payment terms exist, but a payment period could not be identified."
        }

    days = int(match.group(1))

    if days <= 30:
        return {
            "status": "PASS",
            "reason": f"Payment period is {days} days."
        }

    return {
        "status": "FAIL",
        "reason": f"Payment period is {days} days, which exceeds the 30-day requirement."
    }


def check_termination(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Termination clause is missing."
        }

    notice = re.search(
        r'(\d+)\s*(?:calendar\s*)?days?.{0,80}(?:notice|terminate)',
        clause,
        re.IGNORECASE | re.DOTALL
    )

    if notice:
        days = int(notice.group(1))

        return {
            "status": "PASS",
            "reason": f"Termination clause specifies a {days}-day notice period."
        }

    if re.search(r'terminat', clause, re.IGNORECASE):
        return {
            "status": "REVIEW",
            "reason": "Termination clause exists, but a clear notice period was not identified."
        }

    return {
        "status": "FAIL",
        "reason": "No clear termination provision identified."
    }


def check_confidentiality(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Confidentiality clause is missing."
        }

    has_confidential = bool(
        re.search(r'confidential', clause, re.IGNORECASE)
    )

    has_obligation = bool(
        re.search(
            r'(shall|must|required|agree|obligation|disclose|protect|maintain)',
            clause,
            re.IGNORECASE
        )
    )

    if has_confidential and has_obligation:
        return {
            "status": "PASS",
            "reason": "Confidentiality obligations are specified."
        }

    return {
        "status": "REVIEW",
        "reason": "Confidentiality clause exists but its obligations are unclear."
    }


def check_intellectual_property(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Intellectual property clause is missing."
        }

    has_ip = bool(
        re.search(
            r'intellectual\s+property|IP\s+rights?|copyright|ownership',
            clause,
            re.IGNORECASE
        )
    )

    has_ownership = bool(
        re.search(
            r'ownership|owned|assign|assignment|rights|belong',
            clause,
            re.IGNORECASE
        )
    )

    if has_ip and has_ownership:
        return {
            "status": "PASS",
            "reason": "Intellectual property ownership or rights are addressed."
        }

    return {
        "status": "REVIEW",
        "reason": "Intellectual property clause exists but ownership or rights are unclear."
    }



def check_liability(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Liability clause is missing."
        }

    has_liability = bool(
        re.search(r'liabilit', clause, re.IGNORECASE)
    )

    has_limit = bool(
        re.search(
            r'limit|maximum|cap|exclude|excluded|damages',
            clause,
            re.IGNORECASE
        )
    )

    if has_liability and has_limit:
        return {
            "status": "PASS",
            "reason": "Liability and limitation/exclusion provisions are addressed."
        }

    if has_liability:
        return {
            "status": "REVIEW",
            "reason": "Liability is addressed, but a clear limitation or exclusion was not identified."
        }

    return {
        "status": "FAIL",
        "reason": "No clear liability provision identified."
    }


def check_force_majeure(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Force majeure clause is missing."
        }

    has_event = bool(
        re.search(
            r'force\s+majeure|act[s]?\s+of\s+god|beyond.*control',
            clause,
            re.IGNORECASE
        )
    )

    has_effect = bool(
        re.search(
            r'liable|liability|delay|suspend|terminate|excuse|relief',
            clause,
            re.IGNORECASE
        )
    )

    if has_event and has_effect:
        return {
            "status": "PASS",
            "reason": "Force majeure events and their contractual effect are addressed."
        }

    return {
        "status": "REVIEW",
        "reason": "Force majeure clause exists but its effect on contractual obligations is unclear."
    }


def check_governing_law(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Governing law clause is missing."
        }

    has_law = bool(
        re.search(
            r'governed|governing\s+law|laws?\s+of|applicable\s+law',
            clause,
            re.IGNORECASE
        )
    )

    if has_law:
        return {
            "status": "PASS",
            "reason": "Governing law is specified."
        }

    return {
        "status": "REVIEW",
        "reason": "Clause exists but the governing law is unclear."
    }


def check_dispute_resolution(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Dispute resolution clause is missing."
        }

    has_mechanism = bool(
        re.search(
            r'arbitration|court|mediation|conciliation|dispute\s+resolution',
            clause,
            re.IGNORECASE
        )
    )

    if has_mechanism:
        return {
            "status": "PASS",
            "reason": "A dispute resolution mechanism is specified."
        }

    return {
        "status": "REVIEW",
        "reason": "Dispute resolution clause exists but no clear mechanism was identified."
    }


def check_scope_of_work(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Scope of work clause is missing."
        }

    has_scope = bool(
        re.search(
            r'provide|deliver|supply|services|goods|deliverables|scope',
            clause,
            re.IGNORECASE
        )
    )

    if has_scope:
        return {
            "status": "PASS",
            "reason": "Goods, services, or deliverables are addressed."
        }

    return {
        "status": "REVIEW",
        "reason": "Scope of work clause exists but the actual obligations are unclear."
    }

def check_renewal(clause):
    if not clause:
        return {
            "status": "FAIL",
            "reason": "Renewal clause is missing."
        }

    has_renewal = bool(
        re.search(
            r'renew|renewal|extension|extend|automatically',
            clause,
            re.IGNORECASE
        )
    )

    if has_renewal:
        return {
            "status": "PASS",
            "reason": "Renewal or extension terms are addressed."
        }

    return {
        "status": "REVIEW",
        "reason": "Renewal clause exists but its conditions are unclear."
    }


def check_contract(clauses):

    results = {}

    results["payment_terms"] = check_payment_terms(
        clauses.get("payment_terms")
    )

    results["termination"] = check_termination(
        clauses.get("termination")
    )

    results["confidentiality"] = check_confidentiality(
        clauses.get("confidentiality")
    )

    results["intellectual_property"] = check_intellectual_property(
        clauses.get("intellectual_property")
    )

    results["liability"] = check_liability(
        clauses.get("liability")
    )

    results["force_majeure"] = check_force_majeure(
        clauses.get("force_majeure")
    )

    results["governing_law"] = check_governing_law(
        clauses.get("governing_law")
    )

    results["dispute_resolution"] = check_dispute_resolution(
        clauses.get("dispute_resolution")
    )

    results["scope_of_work"] = check_scope_of_work(
        clauses.get("scope_of_work")
    )

    results["renewal"] = check_renewal(
        clauses.get("renewal")
    )

    return results


if __name__ == "__main__":

    
    COMPLIANCE_DIR.mkdir(parents=True, exist_ok=True)

    # Find every standardized JSON file
    for json_file in STANDARDIZED_DIR.glob("*_standard.json"):

        print(f"\nChecking: {json_file.name}")

        # Read standardized clauses
        with open(json_file, "r", encoding="utf-8") as f:
            clauses = json.load(f)

        # Run all 10 compliance checks
        results = check_contract(clauses)

        # Create output filename
        output_file = COMPLIANCE_DIR / (
            json_file.stem.replace(
                "_standard",
                "_compliance"
            ) + ".json"
        )

        # Save compliance results
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)

        print(f"Saved: {output_file.name}")