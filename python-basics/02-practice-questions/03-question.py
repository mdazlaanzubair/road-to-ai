# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

subjects = [
    "English",
    "Mathematics",
    "Physics",
    "Chemistry",
]


def getUserInput(subjects):
    marks = []

    name = input(f"Enter your fullname: ")

    for subject in subjects:
        while True:
            try:
                score = input(f"Enter your marks in {subject} out of 100: ")
                score = float(score)  # Try to convert the input to a float
                marks.append({
                    "title": subject,
                    "score": round(score, 2)
                })
                if score < 0 or score > 100:
                    raise ValueError("Marks should be between 0 and 100.")
                break  # If conversion is successful, exit the loop
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")

    return (name, marks)


def calculateAndDisplay(name, marks):
    print(f"Student Name: {name}")

    marksObtained = float(0)
    for mark in marks:
        marksObtained += mark["score"]
        print(f"Marks in {mark["title"]}: {mark["score"]}")

    percentage = round((marksObtained / 400) * 100, 2)
    gpa = round(percentage / 25, 2)
    print(f"Total marks obtained: {marksObtained}/400")
    print(f"Percentage: {percentage}%", end=" | ")
    print(f"Grade Point Average (GPA): {gpa}", end=" | ")

    if (percentage >= 90):
        print(f"Grade: A")
    elif (percentage >= 80 and percentage < 90):
        print(f"Grade: B")
    elif (percentage >= 70 and percentage < 80):
        print(f"Grade: C")
    elif (percentage >= 60 and percentage < 70):
        print(f"Grade: D")
    elif (percentage >= 35 and percentage < 60):
        print(f"Grade: E")
    else:
        print(f"Grade: F (Fail)")


(name, marks) = getUserInput(subjects)

calculateAndDisplay(name.capitalize(), marks)