import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample resume
resume_text = """
My name is Priya Sharma. I am a software engineer with 3 years of experience in Python and NLP.
You can reach me at priya.sharma@gmail.com or +91-9876543210.
I graduated from Delhi University with a B.Tech in Computer Science.
Skills: Python, NLP, Machine Learning, Data Analysis.
"""

# Run NLP pipeline
doc = nlp(resume_text)

# Extract name (first PERSON entity)
name = None
for ent in doc.ents:
    if ent.label_ == "PERSON":
        name = ent.text
        break

# Extract email using regex
email = re.findall(r'\S+@\S+', resume_text)[0]

# Extract phone number using regex
phone = re.findall(r'\+?\d[\d\-]{8,12}\d', resume_text)[0]

# Extract education (ORG or GPE or FAC)
education = []
for ent in doc.ents:
    if ent.label_ in ("ORG", "GPE", "FAC"):
        education.append(ent.text)

# Extract skills manually
skill_keywords = ["Python", "NLP", "Machine Learning", "Data Analysis"]
skills_found = [skill for skill in skill_keywords if skill.lower() in resume_text.lower()]

# Display
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Education:", education)
print("Skills:", skills_found)
