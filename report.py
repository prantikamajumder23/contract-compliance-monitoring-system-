import subprocess
import sys
import json
from pathlib import Path


BASE_DIR = Path(__file__).parent

COMPLIANCE_DIR = BASE_DIR / "data" / "processed" / "compliance"
RISK_DIR = BASE_DIR / "data" / "processed" / "risk"
REPORT_DIR = BASE_DIR / "data" / "processed" / "reports"


def generate_report(compliance_data, risk_data, contract_name):

    report = []

    report.append("=" * 50)
    report.append("       CONTRACT COMPLIANCE REPORT")
    report.append("=" * 50)

    report.append("")
    report.append(f"Contract: {contract_name}")

    report.append("")
    report.append("COMPLIANCE SUMMARY")
    report.append("-" * 40)

    report.append(f"PASS       : {risk_data['pass']}")
    report.append(f"FAIL       : {risk_data['fail']}")
    report.append(f"REVIEW     : {risk_data['review']}")
    report.append(f"COMPLIANCE : {risk_data['compliance_score']}%")

    report.append("")
    report.append("RISK SUMMARY")
    report.append("-" * 40)

    report.append(f"RISK SCORE : {risk_data['risk_score']}")
    report.append(f"RISK RATE  : {risk_data['risk_rate']}%")

    report.append("")
    report.append("MANUAL REVIEW REQUIRED")
    report.append("-" * 40)

    if risk_data["manual_review_needed"]:
        for clause in risk_data["manual_review_needed"]:
            report.append(f"- {clause}")
    else:
        report.append("None")

    report.append("")
    report.append("CLAUSE RESULTS")
    report.append("-" * 40)

    for clause, result in compliance_data.items():

        status = result["status"]
        reason = result["reason"]

        report.append("")
        report.append(f"{clause}")
        report.append(f"Status : {status}")
        report.append(f"Reason : {reason}")

    report.append("")
    report.append("=" * 50)

    return "\n".join(report)


def main():

    # Run the complete pipeline

    subprocess.run(
        [sys.executable, "import.py"],
        check=True,
        cwd=BASE_DIR
    )

    subprocess.run(
        [sys.executable, "clean.py"],
        check=True,
        cwd=BASE_DIR
    )

    subprocess.run(
        [sys.executable, "standardize.py"],
        check=True,
        cwd=BASE_DIR
    )

    subprocess.run(
        [sys.executable, "check_compliance.py"],
        check=True,
        cwd=BASE_DIR
    )

    subprocess.run(
        [sys.executable, "risk_score.py"],
        check=True,
        cwd=BASE_DIR
    )

    # Create report folder

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    # Find risk files

    for risk_file in RISK_DIR.glob("*_risk.json"):

        contract_name = risk_file.stem.replace("_risk", "")

        compliance_file = COMPLIANCE_DIR / (
            contract_name + "_compliance.json"
        )

        # Read risk data

        with open(risk_file, "r", encoding="utf-8") as f:
            risk_data = json.load(f)

        # Read compliance data

        with open(compliance_file, "r", encoding="utf-8") as f:
            compliance_data = json.load(f)

        # Generate report

        report = generate_report(
            compliance_data,
            risk_data,
            contract_name
        )

        # Save report

        output_file = REPORT_DIR / (
            contract_name + "_report.txt"
        )

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"Report created: {output_file.name}")


if __name__ == "__main__":
    main()