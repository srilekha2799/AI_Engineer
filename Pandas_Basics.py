import pandas as pd

students = pd.DataFrame({
    "Name": ["Sri", "Anu", "Ravi", "Kiran", "Meena"],
    "Age": [20, 21, 20, 22, 21],
    "Python": [85, 90, 78, 95, 88],
    "AI": [90, 85, 80, 92, 89]
})

print("\nDataFrame\n")
print(students)

print("\nExploring DataFrame\n")
print("Shape: ",students.shape)
print("Info: ",students.info())
print("Describe: ",students.describe())
print("Head: ",students.head(2))
print("Tail: ",students.tail(2))
print("Columns: ",students.columns)

print("\nRetriving Columns\n")
print("Single: ",students["Python"])
print("Multiple: ",students[["Name","Python"]])

print("\nFiltering\n")
print(students[students["AI"]>85])

print("\nAverage\n")
print("AI: ",students["AI"].mean)
print("Python: ",students["Python"].mean)

print("\nAdding new Column\n")
students["Passed"] = students["AI"]>=40
print(students)

print("\nSorting\n")
print(students.sort_values("AI", ascending = False))

print("\nMultiple Conditions\n")
print(students[(students["AI"]>85) & (students["Python"]>85)])