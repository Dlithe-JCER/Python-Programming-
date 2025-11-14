import os

FILE = "students.txt"

# ----------------- CREATE -----------------
def create_student():
    try:
        roll = input("Enter Roll Number: ").strip()
        name = input("Enter Name: ").strip()
        marks = input("Enter Marks: ").strip()

        # Validate
        if not roll.isdigit():
            raise ValueError("Roll number must be numeric.")
        if not marks.isdigit():
            raise ValueError("Marks must be numeric.")

        with open(FILE, "a") as f:
            f.write(f"{roll},{name},{marks}\n")

        print("Record Added Successfully!")

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Unexpected Error occurred:", e)


# ----------------- READ / DISPLAY -----------------
def read_students():
    try:
        if not os.path.exists(FILE):
            print("No records found!")
            return

        with open(FILE, "r") as f:
            data = f.readlines()

        if not data:
            print("The file is empty. No records found.")
            return

        print("\n--- Student Records ---")
        for line in data:
            try:
                roll, name, marks = line.strip().split(",")
                print(f"Roll: {roll} | Name: {name} | Marks: {marks}")
            except ValueError:
                print("Skipping invalid record:", line.strip())
        print("-----------------------\n")

    except Exception as e:
        print("Error reading the file:", e)


# ----------------- UPDATE -----------------
def update_student():
    try:
        roll_to_update = input("Enter Roll No to Update: ").strip()

        if not os.path.exists(FILE):
            print("File does not exist. No records found.")
            return

        with open(FILE, "r") as f:
            lines = f.readlines()

        updated_lines = []
        found = False

        for line in lines:
            try:
                roll, name, marks = line.strip().split(",")
            except ValueError:
                continue  # skip bad lines

            if roll == roll_to_update:
                found = True
                print("Record Found!")

                new_name = input("Enter New Name: ").strip()
                new_marks = input("Enter New Marks: ").strip()

                if not new_marks.isdigit():
                    raise ValueError("Marks must be numeric.")

                updated_lines.append(f"{roll},{new_name},{new_marks}\n")
            else:
                updated_lines.append(line)

        if not found:
            print("Roll Number Not Found!")
            return

        with open(FILE, "w") as f:
            f.writelines(updated_lines)

        print("Record Updated Successfully!")

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Unexpected Error occurred:", e)


# ----------------- DELETE -----------------
def delete_student():
    try:
        roll_to_delete = input("Enter Roll No to Delete: ").strip()

        if not os.path.exists(FILE):
            print("File does not exist. No records found.")
            return

        with open(FILE, "r") as f:
            lines = f.readlines()

        updated_lines = []
        found = False

        for line in lines:
            try:
                roll, name, marks = line.strip().split(",")
            except ValueError:
                continue  # skip invalid lines

            if roll == roll_to_delete:
                found = True
                print("Record Deleted!")
                continue  # skip this record

            updated_lines.append(line)

        if not found:
            print("Roll Number Not Found!")
            return

        with open(FILE, "w") as f:
            f.writelines(updated_lines)

        print("Record Deleted Successfully!")

    except Exception as e:
        print("Unexpected Error:", e)


# ----------------- MAIN MENU -----------------
def main():
    while True:
        try:
            print("""
===== Student CRUD Menu =====
1. Add Student
2. Display Students
3. Update Student
4. Delete Student
5. Exit
""")

            choice = input("Enter your choice: ")

            if choice == "1":
                create_student()
            elif choice == "2":
                read_students()
            elif choice == "3":
                update_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                print("Exiting Program...")
                break
            else:
                print("Invalid Choice! Try Again.")

        except KeyboardInterrupt:
            print("\nProgram interrupted by user!")
            break
        except Exception as e:
            print("An unexpected error occurred in main menu:", e)


# Run the program
main()
