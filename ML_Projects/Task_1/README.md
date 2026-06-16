# Student Academic Performance Prediction

This project predicts a student's final grade based on several academic features.

## Project Structure
- `student_data.csv`: Custom generated dataset with 600 records.
- `generate_data.py`: Script used to create the synthetic dataset.
- `preprocess.py`: Data analysis and visualization script.
- `train_model.py`: Script to train and evaluate the Linear Regression model.
- `student_model.pkl`: The trained model file.
- `correlation_heatmap.png`: Feature correlation visualization.
- `grade_distribution.png`: Target variable distribution plot.

## Features Used
1. Study Hours Per Day
2. Attendance Percentage
3. Assignments Completed
4. Previous Semester Marks
5. Class Participation

## Model Performance
- **Mean Squared Error (MSE)**: 23.34
- **R2 Score**: 0.84

## How to Run
1. Generate data: `python3 generate_data.py`
2. Analyze data: `python3 preprocess.py`
3. Train model: `python3 train_model.py`
