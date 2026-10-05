import numpy as np

print("\nTask 1 Array Creation")
data = np.array([10, 20, 30, 40, 50])
print("Data: ",data)
print("Shape: ",data.shape)
print("Size: ",data.size)
print("No of Dim: ",data.ndim)
print("Data type: ",data.dtype)
print("Numeric Operation: ",data*2)

print("\nTask 2 Operators\n")
a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])
print("Add: ",a+b)
print("Sub: ",a-b)
print("Mul: ",a*b)
print("Div: ",a/b)

print("\nTask 3 Student Marks\n")
marks = np.array([
    [80, 75, 90],
    [85, 88, 92],
    [70, 65, 75]
])
print("Shape: ",marks.shape)
print("Sum: ",np.sum(marks))
print("Avg: ",np.average(marks))
print("Max: ",np.max(marks))
print("Min: ",np.min(marks))
print("Avg based on Marks: ",np.mean(marks,axis=0))

print("\nTask 4 Array Reshape\n")
numbers = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Array_Reshape: ",numbers.reshape(3,4))