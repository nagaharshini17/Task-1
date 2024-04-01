# Task-1
fruits = ["apple", "banana", "orange"] # Create a list of fruits
fruits.append("grape") # Add a new fruit to the list
# Print the modified list
print("List:", fruits)

# Create a dictionary of student information
student = {
    "name": "Alice",
    "age": 18,
    "grade": "A"
}
student["grade"] = "B+" # Modify a value in the dictionary
# Print the updated dictionary
print("Dictionary:", student)

# Create a set of numbers
numbers = {1, 2, 3, 2}  # Sets automatically remove duplicates
numbers.add(2) # Try adding a duplicate element (won't be reflected)
# Print the set (duplicates removed)
print("Set:", numbers)
numbers.remove(1) # Remove an element from the set
# Print the modified set
print("Set after removal:", numbers)
