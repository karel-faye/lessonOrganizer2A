# Lesson Organizer

The Lesson Management System is a Python-based application designed to help users manage educational content. It provides features such as secure user authentication, lesson organization by year level and semester, and data persistence through JSON files. This system is ideal for students and educators who want a straightforward tool for lesson planning.
### Key Features
1.User Authentication: Secure sign-up and log-in functionality.
2.Lesson Management: Add, view, and delete lessons categorized by year level, semester, and subject.
3.Data Storage: JSON-based data storage for portability and simplicity.

## How to Use
### Prerequisites
1.Install Python 3.6 or higher.
2.Ensure your system supports JSON file operations.

### Setting Up
1.Clone this repository using the command: 
git clone <repository-url>
2.Navigate to the project directory: 
cd <project-directory>
3.Verify the presence of the following essential files: 
 
main.py: The core application script.
users.json: Stores user authentication details (auto-generated if missing).
data.json: Stores user lesson data (auto-generated if missing).

### Running the Application
1.Execute the application by running: 
python main.py

2.Follow the prompts to: 
Sign up or log in.
Manage lessons categorized by year level, semester, and subject.

## Features

### Authentication
Sign Up: Create an account with a unique username and password.
Log In: Access your account using valid credentials.
Password Storage: Plain-text storage (consider implementing encryption for enhanced security).

### Lesson Management
Navigate through year levels and semesters.
Add lessons to specific subjects.
Remove lessons as needed.

### Year Level and Semester Navigation
Supports four academic year levels, each with two semesters:
1.First Year
2.Second Year
3.Third Year
4.Fourth Year

Each semester contains predefined subjects, allowing users to organize lessons effectively.

## Project Structure

### Files

main.py: Contains the main application logic.
users.json: Stores user credentials in the following format: 
{
  "username": "password"
}
data.json: Stores lesson data, organized as: 
{
  "<username>": {
    "<year_level>": {
      "<semester>": {
        "<subject>": [
          "Lesson 1",
          "Lesson 2"
        ]
      }
    }
  }
}

### Directory Layout
/: Root directory containing all essential files.
Add directories for logs or additional modules as the project grows.

## Maintenance

### Feature Enhancements
Extend functionality by updating manage_subjects or manage_lessons functions.
Introduce new JSON fields while maintaining backward compatibility.
Bug Fixes
Handle exceptions for invalid inputs or corrupted files.
Test for edge cases, such as login failures or missing data.
Data Management
Regularly back up users.json and data.json to prevent data loss.
Avoid manual edits to JSON files to ensure data integrity.

### Future Improvements
1.Security: Encrypt passwords using hashing algorithms.
2.User Interface: Develop a GUI for enhanced usability.
3.Collaboration: Enable multi-user access with data synchronization.
4.Localization: Add support for multiple languages to broaden accessibility.

## Summary

The Lesson Management System is a beginner-friendly, Python-based project designed to assist with educational planning. Its simplicity, coupled with modular design, makes it suitable for personal use and a strong foundation for further development. Contributions are welcome to enhance its capabilities and usability.

