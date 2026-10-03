from pathlib import Path
import re
import json
BASE_DIR = Path(
    r"C:\Users\Puspita\OneDrive\Documents\Desktop\contract compliance"
)

COMPLIANCE_DIR = BASE_DIR / "data" / "processed" / "compliance"
RISK_DIR = BASE_DIR / "data" / "processed" / "risk"

for file in COMPLIANCE_DIR.glob("*.json"):

 with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)
def count(data):
    pass_no = 0
    fail_no = 0
    review_no =0
    for key,value in data.items():
        status = value["status"]
        if status=="PASS":
            pass_no +=1
        elif status=="FAIL":
            fail_no +=1
        else:
            review_no +=1
    return pass_no,fail_no,review_no


def calculate_score(data):
   pass_no,fail_no,review_no= count(data)
  
   total = pass_no + fail_no

   if total == 0:
        return 0

   score = (pass_no / total) * 100

   return round(score, 2)



def summary(data):
   pass_no, fail_no, review_no = count(data)

   score = calculate_score(data)
   rs = risk(data)
   rr = risk_rate(data)

   manual_review = []

   for key, value in data.items():

        status = value["status"]

        if status == "REVIEW":
            manual_review.append(key)

   result = {
        "pass": pass_no,
        "fail": fail_no,
        "review": review_no,
        "compliance_score": score,
        "manual_review_needed": manual_review,
        "risk_score": rs,
        "risk_rate": rr
    }

   return result





def risk(data):
   
    weight={"PASS":0,
            "FAIL":15,
            "REVIEW":5 }
    risk_score = 0
    for key, value in data.items():
        status = value["status"]

        risk_score += weight[status]

    return risk_score

def risk_rate(data):
    score = risk(data)
    if score>=0 and score<=20:
        rate="LOW"
    elif score>20 and score<=40:
            rate="MEDIUM"
    elif score>40 and score<=70:
            rate="HIGH"
    else:
        rate ="CRITICAL"
    return rate
    
            



if __name__ == "__main__":

    RISK_DIR.mkdir(parents=True, exist_ok=True)

    for json_file in COMPLIANCE_DIR.glob("*_compliance.json"):

        print(f"Processing: {json_file.name}")

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        result = summary(data)

        output_file = RISK_DIR / (
            json_file.stem.replace(
                "_compliance",
                "_risk"
            ) + ".json"
        )

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

        print(f"Created: {output_file.name}")




