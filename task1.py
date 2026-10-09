
students = []

def result(p, ai, maths):
    total = p + ai + maths
    per = total / 3

    if per >= 80:
        grade = "A"
    elif per >= 70:
        grade = "B"
    elif per >= 60:
        grade = "C"
    elif per >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, per, grade


# Input 5 students
for i in range(5):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    p = float(input("Python marks: "))
    ai = float(input("AI marks: "))
    maths = float(input("Maths marks: "))

    total, per, grade = result(p, ai, maths)

    students.append({
        "name": name,
        "roll": roll,
        "total": total,
        "percentage": per,
        "grade": grade
    })

# Display results
for s in students:
    print(s)

# Highest percentage
top = max(students, key=lambda s: s["percentage"])
print("Highest Percentage:", top)

# Save results
with open("results.txt", "w") as file:
    for s in students:
        file.write(str(s) + "\n")

    file.write("Highest Marks: " + str(top) + "\n")