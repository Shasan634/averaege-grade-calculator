import os

# Define the path to the file in your Documents folder
file_path = os.path.expanduser("~/Documents/AverageCalc/grades.txt")

def load_courses():
    courses = []
    
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                course_name, credit_hours, mark = line.strip().split(',')
                courses.append({
                    "name": course_name,
                    "credit_hours": float(credit_hours),
                    "mark": float(mark)
                })
    return courses

def save_courses(courses):
    with open(file_path, "w") as file:
        for course in courses:
            file.write(f"{course['name']},{course['credit_hours']},{course['mark']}\n")

def calculate_required_average():
    # Total credit hours needed to graduate
    total_credit_hours = 99
    
    # Load existing courses from file
    courses = load_courses()
    
    # If there are existing courses, display them
    if courses:
        print("\nExisting courses:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course['name']}: {course['credit_hours']} credit hours, mark: {course['mark']}")
    else:
        print("\nNo existing courses found.")
    
    # Input the number of new courses to add
    num_new_courses = int(input("\nEnter the number of new courses to add: "))
    
    # Input the details for each new course
    for i in range(num_new_courses):
        course_name = input(f"Enter the name of course {i+1}: ")
        credit_hours = float(input(f"Enter the credit hours for {course_name}: "))
        mark = float(input(f"Enter the mark achieved for {course_name}: "))
        
        # Add the new course to the list
        courses.append({
            "name": course_name,
            "credit_hours": credit_hours,
            "mark": mark
        })
    
    # Save the updated courses to the file
    save_courses(courses)
    
    # Calculate total completed credit hours and weighted score
    total_completed_credit_hours = 0
    total_weighted_score = 0
    
    for course in courses:
        total_completed_credit_hours += course["credit_hours"]
        total_weighted_score += course["credit_hours"] * course["mark"]
    
    # Input the desired average at the end of university
    desired_avg = float(input("\nEnter your desired average at the end of university: "))
    
    # Remaining credit hours
    remaining_credit_hours = total_credit_hours - total_completed_credit_hours
    
    # Calculate the required average for remaining courses
    if remaining_credit_hours > 0:
        total_score_needed = total_credit_hours * desired_avg
        score_needed_in_remaining_courses = total_score_needed - total_weighted_score
        required_avg_in_remaining_courses = score_needed_in_remaining_courses / remaining_credit_hours
        
        print("\nYou have completed", total_completed_credit_hours, "credit hours so far.")
        print(f"To achieve your desired average of {desired_avg}, you need to score an average of "
              f"{required_avg_in_remaining_courses:.2f} in the remaining {remaining_credit_hours} credit hours.")
    else:
        current_avg = total_weighted_score / total_completed_credit_hours
        print(f"\nYou have already completed all required credit hours. Your current average is {current_avg:.2f}.")
        if current_avg >= desired_avg:
            print(f"Congratulations! You have already achieved your desired average of {desired_avg}.")
        else:
            print(f"You have not achieved your desired average of {desired_avg}. You may need to retake some courses.")

# Run the program
calculate_required_average()