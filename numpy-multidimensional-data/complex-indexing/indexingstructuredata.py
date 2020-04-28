import numpy as np

name = ['Alice', 'Beth', 'Cathy', 'Dorothy']
studentId = [1, 2, 3, 4]
score = [85.4, 90.4, 87.66, 78.9]

# U10: String, i4: Integer, f8: Float
student_data = np.zeros(4, dtype={'names': ('name', 'studentId', 'score'), 'formats': ('U10', 'i4', 'f8')})
print(student_data)

student_data['name'] = name
student_data['studentId'] = studentId
student_data['score'] = score

print(student_data)
print(student_data['name'])
print(student_data[1])
print(student_data[-1]['name'])

# conditions
print(student_data[student_data['score'] > 85]['name'])
