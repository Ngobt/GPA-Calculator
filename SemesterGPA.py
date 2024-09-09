MAX_CREDIT = 5
MIN_CREDIT = 1

gradeCredit = {'A': 4, 
               'B': 3, 
               'C': 2, 
               'D': 1, 
               'F': 0}

total_classes = []
total_credits = []
total_grades = []


def get_user_classes():
    while True:
        user_classes = input("Enter your Class: ")
        if user_classes != "q":
            total_classes.append(user_classes)
        else:
            break
        
    return total_classes

def get_user_credits():
    i = 0
    for i in range(len(total_classes)):
        user_credits = input(f"Enter credit hours for {total_classes[i]}: ")
        if user_credits.isdigit():
            user_credits = int(user_credits)
            if MIN_CREDIT <= user_credits <= MAX_CREDIT:
                total_credits.append(user_credits)
                i += 1
            else:
                print(f"Credit hours have to be between ({MIN_CREDIT} - {MAX_CREDIT})")
        else:
            print(f"Credit hours have to be an integer")
        
    return total_credits


def get_user_grades():
    i = 0
    for i in range(len(total_classes)):
        user_grades = input(f"Enter grade for {total_classes[i]}: ").upper()
        if user_grades in gradeCredit:
            user_grades = gradeCredit[user_grades]
            total_grades.append(user_grades)
            i += 1
        else:
            print(f"Your grade letter has to be one of these letters: ({gradeCredit})")
        
    return total_grades


def calculate_new_gpa(user_classes, user_credits, user_grades):
    total_value = []
    i = 0
    
    for i in range(len(total_classes)):
        total_value.append(total_grades[i] * total_credits[i])
        i += 1
    
    total_sum = sum(total_value)
    total_credit_hours = sum(total_credits)
    
    new_gpa = total_sum / total_credit_hours
    
    return new_gpa



def main():
    user_classes = get_user_classes()
    user_credits = get_user_credits()
    user_grades = get_user_grades()
    user_gpa = calculate_new_gpa(user_classes, user_credits, user_grades)
    
    print(f"\nSemester GPA: {user_gpa:0.2f}")
    
main()