student = {
    "name": "Francisco",
    "grade": 90,
    "subjects": ["Math", "Python", "English"]
}

for key, value in student.items():
    print(key, value)

student["graduated"] = False

print(student)