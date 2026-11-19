midterm_score = float(input("Please enter the midterm score: "))
final_score = float(input("Please enter the final score: "))
average = 0.4 * midterm_score + 0.6 * final_score

print(f"Average: {average:.2f}")

if average >= 80:
    print("Excellent!")
elif average >= 60:
    print("Passed")
else:
    print("failed")
    