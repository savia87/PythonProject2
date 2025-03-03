# Student Data Chatbot
A Python-based chatbot that queries student data from an Excel file via a Flask web interface.

## Features
- Query active students (Status='A').
- Filter active students by entity (e.g., 'give me active students from entity 0011').

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Add a `students.xlsx` file with columns: StudentID, StudentNumber, Grade, Status, Entity, etc.
3. Run: `python student_chatbot.py`
4. Open `http://127.0.0.1:5000/` in a browser.

## Files
- `student_chatbot.py`: Backend logic and Flask app
- `templates/index.html`: Web interface
- `requirements.txt`: Python dependencies