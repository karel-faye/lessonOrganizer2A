import json

def Ask():
    while True:
        askInput = input("Good Day! \n1. Teacher\n2. Student\n3. Exit\nInput here: ")

        if askInput == "1":
            Intro2()
            break
        elif askInput == "2":
            Intro()    
            break
        elif askInput == "3":
            print("Exiting... Have a nice day!")
            quit()    
            
        else:
            print("Invalid input. Try again.")

def Intro2():
    while True:
        userInput = input("Good Day! \n1. Log In\n2. Sign Up\n3. Exit\nInput here: ")

        if userInput == "1":
            Login2()
            break
        elif userInput == "2":
            SignUp2()    
            break
        elif userInput == "3":
            print("Exiting... Have a nice day!")
            quit()    
            
        else:
            print("Invalid input. Try again.")


def Intro():
    while True:
        userInput = input("Good Day! \n1. Log In\n2. Sign Up\n3. Exit\nInput here: ")

        if userInput == "1":
            Login()
            break
        elif userInput == "2":
            SignUp()    
            break
        elif userInput == "3":
            print("Exiting... Have a nice day!")
            quit()    
            
        else:
            print("Invalid input. Try again.")

def Login2():
    max_attempts = 3  # Limit login attempts to prevent infinite loop

    for attempt in range(max_attempts):
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            # Load the JSON file
            with open("teachers.json", "r") as file:
                teachers = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            teachers = []  # Start with an empty user list if file doesn't exist or is invalid

        # Check if username and password match any user in the list
        for user in teachers:
            if user.get("username") == username and user.get("password") == password:
                print("Login successful!\n")
                YearLevel(username)  # Call the next function with the username
                return  # Exit after successful login

        # If no match is found, prompt for action
        print("Invalid username or password.")
        while True:
            choice = input("Do you want to sign up instead? (y/n): ").strip().lower()
            if choice == "y":
                SignUp2()
                return  # Exit after signing up
            elif choice == "n":
                print("Please try logging in again.")
                break  # Allow retrying login
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    # If maximum attempts reached
    print("Maximum login attempts reached. Returning to the main menu.")
    Intro2()



def Login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Load the JSON file and handle errors gracefully
        try:
            with open("students.json", "r") as file:
                students = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            students = []  # Default to an empty list if the file doesn't exist or is corrupted

        # Verify credentials
        user_found = next((user for user in students if user["username"] == username and user["password"] == password), None)
        
        if user_found:
            print("Login successful!\n")
            YearLevel(username)  # Pass username to keep track of lessons
            return  # Exit the function after successful login

        # If no match is found, prompt the user for next action
        print("Invalid username or password.")
        choice = input("Do you want to sign up instead? (y/n): ").strip().lower()

        if choice == "y":
            SignUp()
            return  # Exit after signing up
        elif choice == "n":
            print("Please try logging in again.")
            Intro()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def SignUp2():
    first_name = input("Enter first name: ").strip()
    surname = input("Enter last name: ").strip()
    username = input("Enter preferred username: ").strip()
    password = input("Enter password: ").strip()

    new_user = {
        "firstName": first_name,
        "surname": surname,
        "username": username,
        "password": password
    }

    try:
        with open("teachers.json", "r") as file:
            teachers = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        teachers = []

    # Check if username already exists
    if any(user["username"] == username for user in teachers):
        print("Username already exists. Please choose another.")
        return

    teachers.append(new_user)

    with open("teachers.json", "w") as file:
        json.dump(teachers, file, indent=4)

    # Initialize user data
    initialize_user_data(username)

    print("Sign-up successful!")
    login_choice = input("Do you want to log in (y/n): ").strip().lower()
    if login_choice == "y":
        Login2()
    elif login_choice == "n":
        Intro2()
    else:
        print("Invalid input. Returning to the main menu.")
        Intro2()


def SignUp():
    first_name = input("Enter first name: ").strip()
    surname = input("Enter last name: ").strip()
    username = input("Enter preferred username: ").strip()
    password = input("Enter password: ").strip()

    new_user = {
        "firstName": first_name,
        "surname": surname,
        "username": username,
        "password": password
    }

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []

    # Check if username already exists
    if any(user["username"] == username for user in students):
        print("Username already exists. Please choose another.")
        return

    students.append(new_user)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    # Initialize user data
    initialize_user_data(username)

    print("Sign-up successful!")
    login_choice = input("Do you want to log in (y/n): ").strip().lower()
    if login_choice == "y":
        Login()
    elif login_choice == "n":
        Intro()
    else:
        print("Invalid input. Returning to the main menu.")
        Intro()


def initialize_user_data(username):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if username not in data:
        data[username] = {}  # Initialize an empty structure for the new user

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    

def YearLevel(username):
    # Load lessons data for the user
    user_data = load_lessons_for_user(username)

    while True:
        try:
            yearLevel = int(input(
                "Choose year level: \n1. First Year\n2. Second Year\n3. Third Year\n4. Fourth Year\n5. Go back\n6. Exit\nInput here: "))
            if yearLevel == 1:
                FirstYear(username, "First Year", user_data)
            elif yearLevel == 2:
                SecondYear(username, "Second Year", user_data)
            elif yearLevel == 3:
                ThirdYear(username, "Third Year", user_data)
            elif yearLevel == 4:
                FourthYear(username, "Fourth Year", user_data)
            elif yearLevel == 5:
                Intro()
            elif yearLevel == 6:
                print("Exiting... Have a nice day!")
                quit()
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def load_lessons_from_file2():
    try:
        with open('teachers.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dictionary if no file is found or data is corrupt


def load_lessons_from_file():
    try:
        with open('students.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dictionary if no file is found or data is corrupt

def save_lessons_to_file(username, year_level, semester, subject, lessons):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Navigate through user-specific hierarchy
    user_data = data.setdefault(username, {})
    year_data = user_data.setdefault(year_level, {})
    semester_data = year_data.setdefault(semester, {})
    semester_data[subject] = lessons

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)








def manage_subjects(username, year_level, semester, subjects, subject_lessons):
    while True:
        print("\nSubjects:")
        for idx, subject in enumerate(subjects, 1):
            print(f"{idx}. {subject}")

        print("10. Go Back")
        print("11. Exit")
        choice = input("Select a subject to manage lessons: ")

        if choice == "11":
            print("Exiting... Have a nice day!")
            quit()

        if choice == "10":
            return

        try:
            subject_index = int(choice) - 1
            if subject_index not in range(len(subjects)):
                print("Invalid subject number.")
                continue
            selected_subject = subjects[subject_index]

            # Ensure the subject exists in the lessons structure
            if selected_subject not in subject_lessons:
                subject_lessons[selected_subject] = []

            # Call manage_lessons with all necessary arguments
            manage_lessons(username, year_level, semester, selected_subject)
        except ValueError:
            print("Please enter a valid number.")


def load_lessons_for_user(username):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

    return data.get(username, {})



def manage_lessons(username, year_level, semester, subject):
    # Load user-specific data
    user_data = load_lessons_for_user(username)
    year_data = user_data.setdefault(year_level, {})
    semester_data = year_data.setdefault(semester, {})
    lessons = semester_data.get(subject, [])

    while True:
        print(f"\nManaging lessons for {subject}:")
        if lessons:
            for idx, lesson in enumerate(lessons, 1):
                print(f"{idx}. {lesson}")
        else:
            print("- No lessons yet.")

        print("\nOptions:")
        print("1. Add Lesson")
        print("2. Remove Lesson")
        print("3. Go Back")
        print("4. Exit")
        action = input("Choose an option: ")

        if action == "1":
            new_lesson = input("Enter the lesson to add: ")
            if new_lesson in lessons:
                print("Lesson already exists.")
            else:
                lessons.append(new_lesson)
                print(f"Lesson '{new_lesson}' added successfully.")
                save_lessons_to_file(username, year_level, semester, subject, lessons)

        elif action == "2":
            try:
                for idx, lesson in enumerate(lessons, 1):
                    print(f"{idx}. {lesson}")
                lesson_index = int(input("Enter the number of the lesson to remove: ")) - 1
                if lesson_index not in range(len(lessons)):
                    print("Invalid lesson number.")
                    continue
                removed_lesson = lessons.pop(lesson_index)
                print(f"Lesson '{removed_lesson}' removed successfully.")
                save_lessons_to_file(username, year_level, semester, subject, lessons)
                return
            
            except ValueError:
                print("Please enter a valid number.")

        elif action == "3":
            return
        
        if action == "4":
            print("Exiting... Have a nice day!")
            quit()


        else:
            print("Invalid option. Try again.")



def FirstYear(username, year_level, user_data):
    while True:
        try:
            sem = int(input(
                "1. First Semester \n2. Second Semester\n3. Go back\n4. Exit\nInput here: "))
            if sem == 1:
                manage_subjects(username, year_level, "First Semester", [
                    "Multimedia",
                    "Introduction to Computing",
                    "Computer Programming 1 (Lec)",
                    "Computer Programming 1 (Lab)",
                    "Mathematics in the Modern World",
                    "Readings in Philippine History",
                    "The Entrepreneurial Mind",
                    "PATHFit 1",
                    "National Service Training Program 1"
                ], user_data)
            elif sem == 2:
                manage_subjects(username, year_level, "Second Semester", [
                    "Digital Logic Design",
                    "Discrete Mathematics",
                    "Computer Programming 2 (Lec)",
                    "Computer Programming 2 (Lab)",
                    "Purposive Communication",
                    "Science, Technology, and Society",
                    "Understanding the Self",
                    "Gender and Society with Peace Studies",
                    "PATHFit 2",
                    "National Service Training Program 2"
                ], user_data)
            elif sem == 3:
                YearLevel(username)
                return
            elif sem == 4:
                print("Exiting... Have a nice day!")
                quit()
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def SecondYear(username, year_level, user_data):
    while True:
        try:
            sem = int(input(
                "1. First Semester \n2. Second Semester\n3. Go back\n4. Exit\nInput here: "))
            if sem == 1:
                manage_subjects(username, year_level, "First Semester", [
                    "Ethics",
                    "Environmental Science",
                    "Life and Works of Rizal",
                    "Quantitative Methods (Modeling & Simulation)",
                    "Data Structures and Algorithms (Lec)",
                    "Data Structures and Algorithms (Lab)",
                    "Object-Oriented Programming",
                    "Web Systems and Technologies",
                    "PATHFit 3",
                ], user_data)
            elif sem == 2:
                manage_subjects(username, year_level, "Second Semester", [
                    "The Contemporary World",
                    "Integrative Programming and Technologies 1",
                    "Networking 1",
                    "Information Management (Lec)",
                    "Information Management (Lab)",
                    "Platform Technologies",
                    "ASP.NET",
                    "PATHFit 4"
                ], user_data)
            elif sem == 3:
                YearLevel(username)
                return
            elif sem == 4:
                print("Exiting... Have a nice day!")
                quit()
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def ThirdYear(username, year_level, user_data):
    while True:
        try:
            sem = int(input("1. First Semester \n2. Second Semester\n3. Go back\n4. Exit\nInput here: "))
            if sem == 1:
                manage_subjects(username, year_level, "First Semester", [
                    "Functional English",
                    "Networking 2 (Lec)",
                    "Networking 2 (Lab)",
                    "Systems Integration and Architecture 1",
                    "Introduction to Human Computer Interaction",
                    "Database Management Systems",
                    "Applications Development and Emerging Technologies"
                ], user_data)

            elif sem == 2:
                manage_subjects(username, year_level, "Second Semester", [
                    "Art Appreciation",
                    "People and the Earth's Ecosystems",
                    "Capstone Project and Research 1",
                    "Social and Professional Issues",
                    "Information Assurance and Security 1 (Lec)",
                    "Information Assurance and Security 1 (Lab)",
                    "iOS Mobile Application Development Cross-Platform",
                    "Technology and the Application of the Internet of Things"
                ], user_data)

            elif sem == 3:
                YearLevel(username)
                return
            elif sem == 4:
                print("Exiting... Have a nice day!")
                quit()
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def FourthYear(username, year_level, semester, subject_lessons):
    sem = int(input("1. First Semester \n2. Second Semester\n3. Go back\n4. Exit\nInput here: "))
    if sem == 1:
        manage_subjects(username, year_level, "First Semester", [
            "Information Assurance and Security 2 (Lec)",
            "Information Assurance and Security 2 (Lab)",
            "Systems Administration and Maintenance",
            "Capstone Project and Research 2",
            "Systems Integration and Architecture 2",
            "Cross-Platform Script Development Technology"
        ], subject_lessons)

    elif sem == 2:
        manage_subjects(username, year_level, "Second Semester", [
            "On the Job Training"
        ], subject_lessons)

    elif sem == 3:
        YearLevel(username)  # Pas username to go back to the Year Level selection
        return

    elif sem == 4:
        print("Exiting... Have a nice day!")
        quit()

    else:
        print("Invalid input. Try again.")


Ask()
