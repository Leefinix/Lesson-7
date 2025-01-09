print("Enter you're marks in the 5 subjects: ")
Maths = int(input("Maths: "))
Science = int(input("Science: "))
History = int(input("History:"))
Geography = int(input("Geography: "))
English = int(input("English: "))

tot = Maths+Science+History+Geography+English
avg = tot/5

if avg >= 91 and avg <= 100:
    print("You're grade is A+")
elif avg >= 81 and avg <= 90:
    print("You're grade is A")
elif avg >= 71 and avg <= 80:
    print("You're grade is B+")
elif avg >= 61 and avg <= 70:
    print("You're grade is B")
elif avg >= 51 and avg <= 60:
    print("You're grade is C+")
elif avg >= 41 and avg <= 50:
    print("You're grade is C")
elif avg >= 31 and avg <= 40:
    print("You're grade is D+")
elif avg >= 21 and avg <= 30:
    print("You're grade is D")
elif avg >= 11 and avg <= 20:
    print("You're grade is F")
elif avg >= 0 and avg <= 10:
    print("You're grade is F-")
else:
    print("Enter a valid input!")