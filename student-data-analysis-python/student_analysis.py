# Student Data Analysis Program
# Using Python, NumPy, and Pandas

import pandas as pd
import numpy as np

# -----------------------------
# Creating Dataset of 20 Students
# -----------------------------

data = {
    "Name": [
        "Aman", "Rahul", "Priya", "Sam", "Arjun",
        "Karan", "Pooja", "Anjali", "Rohit", "Sneha",
        "Vikas", "Meena", "Sahil", "Nisha", "Deepak",
        "Riya", "Mohit", "Kavya", "Aditya", "Simran"
    ],
    
    "Age": [
        18, 19, 20, 18, 21,
        20, 19, 18, 21, 20,
        19, 18, 22, 20, 21,
        19, 20, 18, 21, 19
    ],
    
    "Marks": [
        85, 78, 92, 67, 88,
        74, 95, 81, 69, 90,
        76, 84, 58, 91, 72,
        86, 80, 77, 94, 83
    ],
    
    "Attendance": [
        90, 85, 98, 70, 92,
        80, 99, 88, 75, 95,
        82, 89, 65, 97, 78,
        91, 84, 87, 96, 90
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# -----------------------------
# Display Dataset
# -----------------------------

print("\n===== STUDENT DATASET =====")
print(df)

# -----------------------------
# NumPy Analysis
# -----------------------------

marks_array = np.array(df["Marks"])

average_marks = np.mean(marks_array)
highest_marks = np.max(marks_array)
lowest_marks = np.min(marks_array)

print("\n===== MARKS ANALYSIS =====")
print("Average Marks :", round(average_marks, 2))
print("Highest Marks :", highest_marks)
print("Lowest Marks  :", lowest_marks)

# -----------------------------
# Topper Details
# -----------------------------

topper = df[df["Marks"] == highest_marks]

print("\n===== TOPPER DETAILS =====")
print(topper)

# -----------------------------
# Lowest Scorer Details
# -----------------------------

lowest_student = df[df["Marks"] == lowest_marks]

print("\n===== LOWEST SCORER =====")
print(lowest_student)

# -----------------------------
# Student Filtering
# -----------------------------

print("\n===== STUDENTS WITH MARKS >= 85 =====")
high_scorers = df[df["Marks"] >= 85]
print(high_scorers)

# -----------------------------
# Attendance Analysis
# -----------------------------

avg_attendance = np.mean(df["Attendance"])

print("\n===== ATTENDANCE ANALYSIS =====")
print("Average Attendance :", round(avg_attendance, 2), "%")

print("\nStudents with Attendance Below 80%")
low_attendance = df[df["Attendance"] < 80]
print(low_attendance)

# -----------------------------
# Grade Assignment
# -----------------------------

def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Marks"].apply(assign_grade)

print("\n===== STUDENT REPORT WITH GRADES =====")
print(df)

# -----------------------------
# Summary
# -----------------------------

print("\n===== SUMMARY =====")
print(f"Total Students : {len(df)}")
print(f"Average Marks  : {average_marks:.2f}")
print(f"Highest Marks  : {highest_marks}")
print(f"Lowest Marks   : {lowest_marks}")
print(f"Average Attendance : {avg_attendance:.2f}%")