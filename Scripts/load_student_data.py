import pandas as pd

# Load the Excel file
def load_student_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
def chatbot_response(query, df):
    query = query.lower().strip()  # Convert the query to lowercase and remove any leading/trailing whitespace.

    # Check for "active students" based on the 'Status' column, looking for 'A'
    if "active student" in query:
        active_students = df[df['Status'].str.upper() == 'A']  # Filter the DataFrame for rows where 'Status' is 'A'
        return format_students(active_students)  # Format the filtered DataFrame and return the result

    else:
        return "Sorry, I didn’t understand that. Try asking about 'active students'!"
def format_students(df):
    if df.empty:
        return "No students found matching that criteria."  # Return this message if the DataFrame is empty.

    result = "Here are the students:\n"
    for index, row in df.iterrows():  # Iterate over each row in the DataFrame.
        result += (
            f"StudentID: {row['StudentID']}, "
            f"StudentNumber: {row['StudentNumber']}, "
            f"Grade: {row['Grade']}, "
            f"Status: {row['Status']}, "
            f"EnrollmentCode: {row['EnrollmentCode']} - {row['EnrollmentCodeDescription']}\n"
        )
    return result  # Return the formatted string.


# Format the student data into a readable string
def format_students(df):
    if df.empty:
        return "No students found matching that criteria."
    result = "Here are the students:\n"
    for index, row in df.iterrows():
        result += f"ID: {row['ID']}, Name: {row['Name']}, Gender: {row['Gender']}, Status: {row['Status']}, Grade: {row['Grade']}\n"
    return result


# Main chatbot loop
def run_chatbot():
    file_path = "students.xlsx"  # Update this if your file name/path is different
    student_data = load_student_data(file_path)

    if student_data is None:
        print("Chatbot cannot start due to file error.")
        return

    print(
        "Hello! I’m your student data chatbot. Ask me about students (e.g., 'give me active students' or 'give me female students'). Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

    response = chatbot_response(user_input, student_data)
    print("Chatbot:", response)

# Start the chatbot
    if __name__ == "__main__":
        run_chatbot()