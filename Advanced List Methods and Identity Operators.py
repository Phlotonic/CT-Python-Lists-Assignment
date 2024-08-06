# Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]
# Find out if Alice submitted their assignment and 
# attended class. 
# HINT: How might the in keyword be of use here? 
# And how can you check to see if Alice is in both 
# submitted and attended in one if statement?

# Answer: Use the in keyword to check if “Alice” is present 
# in both lists in one if statement:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted their assignment and attended class.")
else:
    print("Alice did not submit their assignment or did not attend class.")
