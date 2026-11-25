import spacy

nlp = spacy.load("en_core_web_sm")

text = "Dr. Ravi works at Apollo Hospital in Chennai on 25 November 2026."

doc = nlp(text)

print("Extracted Entities:")

for ent in doc.ents:
    print(ent.text, "-", ent.label_,
          "Position:", ent.start_char, "-", ent.end_char)
