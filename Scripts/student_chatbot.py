import pandas as pd
from flask import Flask, request, render_template

# Load the Excel file
def load_student_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# Chatbot logic to process queries
def chatbot_response(query, df):
    query = query.lower().strip()

    if "active student" in query and "from entity" in query:
        try:
            entity_part = query.split("from entity")[1].strip()
            entity_value = entity_part.split()[0]
            active_students = df[(df['Status'].str.upper() == 'A') & (df['Entity'].astype(str).str.strip() == entity_value)]
            if active_students.empty:
                return f"No active students found for entity {entity_value}."
            return format_students(active_students)
        except IndexError:
            return "Please specify an entity (e.g., 'give me active students from entity 0011')."
        except Exception as e:
            return f"Error processing entity query: {e}"

    elif "active student" in query:
        active_students = df[df['Status'].str.upper() == 'A']
        if active_students.empty:
            return "No active students found."
        return format_students(active_students)

    else:
        return "Sorry, I didn’t understand that. Try asking about 'active students' or 'active students from entity <value>'!"

# Format the student data into a readable string
def format_students(df):
    if df.empty:
        return "No students found matching that criteria."
    result = "Here are the students:\n"
    for index, row in df.iterrows():
        result += (
            f"StudentID: {row['StudentID']}, "
            f"StudentNumber: {row['StudentNumber']}, "
            f"Grade: {row['Grade']}, "
            f"Status: {row['Status']}, "
            f"Entity: {row['Entity']}, "
            f"EnrollmentCode: {row['EnrollmentCode']} - {row['EnrollmentCodeDescription']}\n"
        )
    return result

# Initialize Flask app
app = Flask(__name__)

# Load student data once when the app starts
file_path = "students.xlsx"  # Update this if your file name/path is different
student_data = load_student_data(file_path)

# Check if data loaded successfully
if student_data is None:
    print("Chatbot cannot start due to file error.")
    exit()

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_query = request.form['query']  # Get the query from the form
        response = chatbot_response(user_query, student_data)
    return render_template('index.html', response=response)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)