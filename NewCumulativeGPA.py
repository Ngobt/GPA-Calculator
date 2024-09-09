import re

symbols = r'^-?\d*\.?\d+$'

MIN_GPA = 0.0
MAX_GPA = 4.0

MIN_CREDITS = 0
MAX_CREDITS = 18


def find_semesterGPA():
    while True:
        old_semesterGPA = input(f"Please type in your semester GPA ({MIN_GPA} - {MAX_GPA}): ")
        if re.match(symbols, old_semesterGPA):
            old_semesterGPA = float(old_semesterGPA)
            if MIN_GPA <= old_semesterGPA <= MAX_GPA:
                break
            else:
                print("Please type a GPA between 0.0 - 4.0")
        else:
            print("Invalid Input")  
    return old_semesterGPA


def find_semesterCredits():
    while True:
        old_semesterCredits = input(f"Please type in your semester credits ({MIN_CREDITS} - {MAX_CREDITS}): ")
        if old_semesterCredits.isdigit():
            old_semesterCredits = int(old_semesterCredits)
            if MIN_CREDITS <= old_semesterCredits <= MAX_CREDITS:
                break
            else:
                print("Your credits have to be between ({MIN_CREDITS} - {MAX_CREDITS})")
        else:
            print("Invalid Input")
    return old_semesterCredits


def old_cumulativeGPA():
    while True:
        old_cumulativeGPA = input("Please type in your cumulative GPA (0.0 - 4.0): ")
        if re.match(symbols, old_cumulativeGPA) and old_cumulativeGPA > 0:
            old_cumulativeGPA = float(old_cumulativeGPA)
            break
        else:
                print("Please type a GPA between 0.0 - 4.0")
    return old_cumulativeGPA


def old_cumulativeCredit():
    while True:
        old_cumulativeCredit = input("Please type in your total amount of credits taken: ")
        if old_cumulativeCredit.isdigit():
            old_cumulativeCredit = int(old_cumulativeCredit)
            break
        else:
            print("Invalid Input")
    return old_cumulativeCredit


def calculate_new_cumulativeGPA(semesterGPA, semesterCredits, cumulativeGPA, cumulativeCredit):
    semester_score = semesterGPA * semesterCredits
    cumulative_score = cumulativeGPA * cumulativeCredit
    total_score = semester_score + cumulative_score
    new_cumulativeGPA = total_score / (semesterCredits + cumulativeCredit)
    
    return new_cumulativeGPA

        
def main():
    semesterGPA = find_semesterGPA()
    semesterCredits = find_semesterCredits()
    cumulativeGPA = old_cumulativeGPA()
    cumulativeCredit = old_cumulativeCredit()
    calculated_new_cumulativeGPA = calculate_new_cumulativeGPA(semesterGPA, semesterCredits, cumulativeGPA, cumulativeCredit)
    
    print(f"\nYour Semester GPA: {semesterGPA} \nYour Semester Credit Hours: {semesterCredits}")
    print()
    print(f"\nYour Cumulative GPA: {cumulativeGPA} \nYour Cumulative Credit Hours: {cumulativeCredit}")
    print()
    print(f"Your New Cumulative GPA is {calculated_new_cumulativeGPA:0.2f}")

main()