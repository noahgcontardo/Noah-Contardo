import pandas as pd
import os

# Set file paths
input_file = r"C:\Users\User\Desktop\python practice\Pre_Assessment_Results_Analysis.xlsx"
output_file = r"C:\Users\User\Desktop\python practice\Assessment_Results_Output.xlsx"

# Check if input file exists
if not os.path.exists(input_file):
    raise FileNotFoundError(f"File not found: {input_file}")

# Load the Excel file
xls = pd.ExcelFile(input_file)
df = pd.read_excel(xls, sheet_name="Data")

# Identify columns
feedback_columns = [col for col in df.columns if col.startswith("Feedback -")]
points_columns = [col for col in df.columns if col.startswith("Points -")]

# Ensure points and feedback columns align correctly
if len(points_columns) != len(feedback_columns):
    raise ValueError("Mismatch between Points and Feedback columns. Check column names!")

# Initialize counts for overall summary
category_counts = {"S": 0, "H": 0, "N": 0}
correct_counts = {"S": 0, "H": 0, "N": 0}

# Initialize list for per-student results
student_results = []

# Process each student (row-wise analysis)
for index, row in df.iterrows():
    student_counts = {"S": 0, "H": 0, "N": 0}
    student_correct = {"S": 0, "H": 0, "N": 0}

    for points_col, feedback_col in zip(points_columns, feedback_columns):
        feedback_value = str(row[feedback_col]) if pd.notna(row[feedback_col]) else ""
        points_value = int(row[points_col]) if pd.notna(row[points_col]) else 0

        for category in ["S", "H", "N"]:
            if category in feedback_value:
                student_counts[category] += 1
                if points_value == 1:
                    student_correct[category] += 1

    # Compute per-student accuracy
    student_ratios = {
        category: (student_correct[category] / student_counts[category] * 100) if student_counts[category] > 0 else 0
        for category in ["S", "H", "N"]
    }

    # Append student results
    student_results.append([
        index + 1,  # Student number (assuming row index represents a student)
        student_counts["S"], student_correct["S"], student_ratios["S"],
        student_counts["H"], student_correct["H"], student_ratios["H"],
        student_counts["N"], student_correct["N"], student_ratios["N"]
    ])

    # Update overall summary counts
    for category in ["S", "H", "N"]:
        category_counts[category] += student_counts[category]
        correct_counts[category] += student_correct[category]

# Compute overall category ratios
category_ratios = {
    category: (correct_counts[category] / category_counts[category] * 100) if category_counts[category] > 0 else 0
    for category in ["S", "H", "N"]
}

# Create DataFrame for summary output
summary_df = pd.DataFrame({
    "Category": ["S", "H", "N"],
    "Total Questions": [category_counts["S"], category_counts["H"], category_counts["N"]],
    "Correct Answers": [correct_counts["S"], correct_counts["H"], correct_counts["N"]],
    "Accuracy (%)": [category_ratios["S"], category_ratios["H"], category_ratios["N"]]
})

# Create DataFrame for per-student breakdown
student_df = pd.DataFrame(student_results, columns=[
    "Student #", 
    "Total S", "Correct S", "Accuracy S (%)",
    "Total H", "Correct H", "Accuracy H (%)",
    "Total N", "Correct N", "Accuracy N (%)"
])

# Save results to a new Excel file (both summary and student breakdown)
with pd.ExcelWriter(output_file, mode="w") as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    student_df.to_excel(writer, sheet_name="Student Breakdown", index=False)

print(f"Results successfully saved to: {output_file}")
