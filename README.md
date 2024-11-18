**Budget Tracker Web App**

**Screenshots**
1- The GUI
![image](https://github.com/user-attachments/assets/da3cb1c3-a639-4ce1-acce-0b82caa7044f)

3- Budget set
![image](https://github.com/user-attachments/assets/8f7a635a-34a9-4350-afdf-fbcc32989733)

4- Adding expenses
![image](https://github.com/user-attachments/assets/f86f80fe-797a-4381-a443-db9e603a5bea)


**Overview**
The Budget Tracker is a simple and intuitive web application designed to help you manage your monthly budget and track expenses effectively. Built with a Python Flask backend and a responsive HTML/CSS/JavaScript frontend, it allows users to set a budget, add expenses, view a detailed expense table, and receive helpful savings advice based on their spending.

**Features**
Set Monthly Budget: Define your monthly budget and track your remaining balance.
Add Expenses: Record expenses by providing a date, amount, category, and description.
Dynamic Updates: Automatically updates the remaining budget and provides savings advice.
View Expense Table: Displays a detailed table of all recorded expenses.
Savings Advice: Get real-time suggestions based on your spending.

**Technologies Used**
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
Styling: Bootstrap for responsiveness and custom CSS
Date Picker: Integrated using HTML <input type="date">

**Getting Started**
1- Prerequisites
Python 3.x installed on your system.
Pip (Python package installer) installed.

2- Installation
Clone this repository:
git clone https://github.com/your-username/budget-tracker.git
cd budget-tracker

Install the required Python packages:
pip install flask

3-Run the Application
Start the Flask server:
python app.py

Open your browser and navigate to:
http://127.0.0.1:5000


**Project Structure**
budget-tracker/
│
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Frontend HTML file
├── static/
│   ├── styles.css         # Custom CSS for styling
│   └── script.js          # JavaScript for frontend functionality
└── README.md              # Project documentation


**How to Use**
Set Budget: Click the Set Monthly Budget button to input your monthly budget.
Add Expense:
Fill in the date, amount, category, and description fields.
Click Add Expense to save the record.
View Expenses: Check the Expense Table for a detailed list of your recorded expenses.
Savings Advice: See real-time advice below your remaining budget.

**Contributing**
Feel free to fork this repository and submit pull requests. Contributions to enhance functionality or fix bugs are welcome.

**License**
This project is licensed under the MIT License.
