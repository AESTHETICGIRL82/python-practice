def calculate_sem5_gpa():
    # Inputs
    cgpa_4 = float(input("Enter CGPA after 4 semesters: "))
    credits_4 = float(input("Enter total credits after 4 semesters: "))

    cgpa_5 = float(input("Enter CGPA after 5 semesters: "))
    credits_5 = float(input("Enter total credits after 5 semesters: "))

    sem5_credits = credits_5 - credits_4

    if sem5_credits <= 0:
        print("Invalid credit values.")
        return

    # Calculate GPA of semester 5
    total_points_4 = cgpa_4 * credits_4
    total_points_5 = cgpa_5 * credits_5

    sem5_points = total_points_5 - total_points_4
    sem5_gpa = sem5_points / sem5_credits

    print(f"\nGPA of Semester 5 is: {sem5_gpa:.2f}")


calculate_sem5_gpa()
# / always returns float.
# 2.5 // 2 = 1.0 Since one number is float → result will be float.
# int+float = float
# 2.5 + 2 = 4.5 Since one number is float → result will be float.
# 2.5 * 2 = 5.0 Since one number is float → result will be float.
# 2.5 - 2 = 0.5 Since one number is float → result will be float.
# 2.5 ** 2 = 6.25 Since one number is float → result will be float.
# 5 **2 = 25 Since both numbers are int → result will be int.
# index
# P  r  o  g  r  a  m  m  i  n  g
# 0  1  2  3  4  5  6  7  8  9 10
# -11                ...        -1
def square(x):
    return x*x

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def average(s):
    return sum(s)/len(s)

    

