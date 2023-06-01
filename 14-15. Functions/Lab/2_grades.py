def evaluate_grade(grade):
    if grade >= 5.50:
        return "Excellent"
    elif grade >= 4.50:
        return "Very Good"
    elif grade >= 3.50:
        return "Good"
    elif grade >= 3.00:
        return "Poor"
    else:
        return "Fail"


input_grade = float(input())

print(evaluate_grade(input_grade))
