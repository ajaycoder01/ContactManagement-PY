📇 Contact Management System

A simple, menu-driven Contact Management System built using Python that allows users to manage their contacts through a command-line interface. The application uses a JSON file to store contact information permanently, so the data remains available even after the program is closed.

✨ Features
```
Add Contact: Add a new contact with a name, phone number, email address, and category.
View All Contacts: Display all saved contacts with their details.
Search Contacts: Search contacts by name, phone number, email address, or category.
Filter by Category: View contacts belonging to a specific category, such as Family, Friends, Work, or Other.
Update Contact: Modify existing contact details using the contact ID.
Delete Contact: Remove a contact after confirmation.
Phone Number Validation: Accept only valid 10-digit Indian mobile numbers starting with 6, 7, 8, or 9.
Email Validation: Check the email address format before saving.
Duplicate Detection: Prevent duplicate phone numbers and email addresses.
Automatic ID Generation: Assign a unique ID to each newly added contact.
JSON File Storage: Save contact information in a JSON file for persistent storage.
```
🛠️ Technologies Used
```
Programming Language: Python 3
Data Storage: JSON
Modules: json, os, and re
Interface: Command-Line Interface (CLI)
```
📂 Project Structure
```
Contact-Management-System/
│
├── contact_management.py   # Main Python application
├── contacts.json           # Stores contact information
└── README.md               # Project documentation

```
The contacts.json file is created when contacts are saved if it does not already exist. It can also be created manually with an empty JSON array ([]).

⚙️ Requirements
Python 3.8 or later recommended.
A terminal or command prompt.
A code editor such as Visual Studio Code or PyCharm (optional).

No external Python libraries are required. The application uses Python's built-in modules.

🚀 Installation and Setup
Step 1: Clone or Download the Project

Download the project files or clone the repository:

git clone <your-repository-url>


Navigate to the project directory:

cd Contact-Management-System


Replace <your-repository-url> with your actual Git repository URL.

Step 2: Run the Application

Execute the following command in your terminal:

python contact_management.py


If your system uses python3 to run Python, use:

python3 contact_management.py

Step 3: Start Managing Contacts

After running the program, the main menu appears in the terminal. Enter the number corresponding to the operation you want to perform.
```
🖥️ Application Menu
=============================================
       CONTACT MANAGEMENT SYSTEM
=============================================
1. Add Contact
2. View All Contacts
3. Search Contact
4. Filter by Category
5. Update Contact
6. Delete Contact
7. Exit
=============================================
Enter your choice:

Menu Options
Option	Operation	Description
1	Add Contact	Add a new contact
2	View All Contacts	Display all saved contacts
3	Search Contact	Find contacts using a keyword
4	Filter by Category	Display contacts from a selected category
5	Update Contact	Modify an existing contact
6	Delete Contact	Delete a contact after confirmation
7	Exit	Close the application
```

✅ Validation Rules
Phone Number
Must contain exactly 10 digits.
Must start with a digit from 6 to 9.
Must not contain spaces, letters, or special characters.

Example: 9870043200

Email Address
Must contain a valid-looking email format.
Must include an @ symbol and a domain extension.
Duplicate email addresses are not allowed, regardless of letter case.

Example: abc@gmail.com

Contact Name
Cannot be empty.
Leading and trailing spaces are removed.
Duplicate Contacts

The application checks for duplicate phone numbers and email addresses before saving a new contact or updating an existing one.

🔍 Search and Filter Examples

Search contacts: Enter a name, phone number, email address, or category. The program displays contacts containing the entered keyword.

Filter by category: Enter a category such as friends, family, work, or other to display matching contacts.

Category matching is case-insensitive.


👨‍💻 Author

Name: Ajay Yadav

Project: Contact Management System

Language: Python
