import pandas as pd
import numpy as np

np.random.seed(42)
n_records = 600

study_hours = np.random.uniform(1, 10, n_records)
attendance = np.random.uniform(60, 100, n_records)
assignments = np.random.randint(0, 11, n_records)
prev_marks = np.random.uniform(40, 100, n_records)
participation = np.random.randint(1, 6, n_records)

# Simple linear relationship with some noise
final_grade = (
    0.3 * study_hours * 10 + 
    0.2 * attendance + 
    2.0 * assignments + 
    0.3 * prev_marks + 
    2.0 * participation + 
    np.random.normal(0, 5, n_records)
)

# Clip to 0-100 range
final_grade = np.clip(final_grade, 0, 100)

df = pd.DataFrame({
    'Study_Hours': np.round(study_hours, 1),
    'Attendance_Percentage': np.round(attendance, 1),
    'Assignments_Completed': assignments,
    'Previous_Semester_Marks': np.round(prev_marks, 1),
    'Class_Participation': participation,
    'Final_Performance_Grade': np.round(final_grade, 1)
})

df.to_csv('student_data.csv', index=False)
print("Dataset created successfully with", n_records, "records.")
