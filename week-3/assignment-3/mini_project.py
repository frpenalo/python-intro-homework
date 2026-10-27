day = input("What day is it? ").lower()
time = input("What time of day? ").lower()

if day == "monday" and time == "morning":
    print("Suggestion: Start the week with some Python practice.")

elif day == "monday" and time == "afternoon":
    print("Suggestion: Take a walk after lunch.")

elif day == "monday" and time == "evening":
    print("Suggestion: Relax and watch a movie.")

elif day == "tuesday" and time == "morning":
    print("Suggestion: Study Python for one hour.")

elif day == "tuesday" and time == "afternoon":
    print("Suggestion: Go to the gym.")

elif day == "tuesday" and time == "evening":
    print("Suggestion: Read a book.")

elif day == "saturday" and time == "morning":
    print("Suggestion: Have a good breakfast.")

elif day == "saturday" and time == "afternoon":
    print("Suggestion: Spend time with family.")

elif day == "saturday" and time == "evening":
    print("Suggestion: Watch a movie or try a new recipe.")

elif day != "monday" and day != "tuesday" and day != "saturday":
    print("Sorry, I don't recognize that day.")

else:
    print("Sorry, I don't recognize that time of day.")