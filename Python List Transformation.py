# Task 1:
# Given the list of grades:

# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and print the 
# sorted list.

# Answer:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print("Sorted grades in descending order:", sorted_grades)

# Task 2:
# Calculate the average grade and print it.

# Answer:
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)
