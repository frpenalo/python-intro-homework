students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Find the top scorer
highest_score = 0
top_student = ""

for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_student = student["name"]


# Calculate the class average
total = 0

for student in students:
    total = total + student["score"]

average = total / len(students)


# Find all unique subjects
subjects = set()

for student in students:
    subjects.add(student["subject"])


# Find students who scored above 75
high_scorers = []

for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])


# Print the results
print(f"Top scorer: {top_student} ({highest_score})")
print(f"Class average: {average}")
print(f"Subjects offered: {subjects}")
print(f"High scorers: {high_scorers}")