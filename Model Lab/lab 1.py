import re

text = """Patient ID: P12345, Appointment on 25-11-2026
at 10:30 AM. Patient has fever and cough."""

patterns = {
    "Patient ID": r'P\d+',
    "Date": r'\d{2}-\d{2}-\d{4}',
    "Time": r'\d{1,2}:\d{2}\s?(AM|PM)'
}

for key, pattern in patterns.items():
    print(key, ":", re.findall(pattern, text))

keywords = ["fever", "cough", "diabetes"]

found = [word for word in keywords if word in text.lower()]

print("Medical Keywords:", found)
