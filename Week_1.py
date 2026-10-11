
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Create the dataset
data = pd.DataFrame({
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "Exam_Score": [35, 40, 48, 52, 60, 67, 74, 82, 88, 94]
})

# 2. Inspect the data using Pandas
print("STUDENT DATASET")
print(data)

print("\nDataset shape:", data.shape)
print("\nDataset information:")
data.info()

print("\nAverage values:")
print(data.mean())

# 3. Separate features (X) and target (y)
X = data[["Study_Hours", "Attendance"]]
y = data["Exam_Score"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# 4. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 5. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict scores for the test data
predictions = model.predict(X_test)

print("\nACTUAL SCORES:")
print(y_test.to_numpy())

print("\nPREDICTED SCORES:")
print(np.round(predictions, 2))

# 7. Evaluate the model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMODEL EVALUATION")
print("Mean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 3))

# 8. Predict for a new student
new_student = pd.DataFrame({
    "Study_Hours": [7],
    "Attendance": [82]
})

predicted_score = model.predict(new_student)

print("\nNEW STUDENT")
print("Study hours:", new_student["Study_Hours"].iloc[0])
print("Attendance:", new_student["Attendance"].iloc[0], "%")
print("Predicted exam score:", round(predicted_score[0], 2))
