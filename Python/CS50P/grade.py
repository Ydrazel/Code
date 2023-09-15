score = int(input("Score: "))

if 90 <= score <= 100: # score >= 90:
    print("Grade: A")
elif 80 <= score < 90: # score >= 80:
    print("Grade: B")
elif 70 <= score < 80: # score >= 70:
    print("Grade: C")
elif 60 <= score < 70: # score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
