def student_marks_lookup():
    marks_dict = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 90,
        "Evan": 88
    }

    name = input("Enter the student's name: ")
    if name in marks_dict:
        print(f"{name}'s marks are: {marks_dict[name]}")
    else:
        print(f"Student '{name}' not found.")

if __name__ == "__main__":
    student_marks_lookup()
