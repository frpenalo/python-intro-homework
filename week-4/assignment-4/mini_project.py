students = [
    {"name": "Jazmin", "score": 82, "subject": "Python"},
    {"name": "Sara", "score": 88, "subject": "Data"},
    {"name": "Francisco", "score": 95, "subject": "Web"},
    {"name": "Mia", "score": 79, "subject": "Python"},
    {"name": "Eli", "score": 84, "subject": "Data"},
    {"name": "Emma", "score": 67, "subject": "Web"},
    {"name": "Luis", "score": 72, "subject": "Python"},
    {"name": "Ana", "score": 83, "subject": "Data"}
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