import psycopg
from psycopg import rows
def connect_db():
    return psycopg.connect(
        host="localhost",
        port="5432",
        dbname="postgres",
        user="postgres",
        password="Sunflower1"
    )

print("Connected to database")

# function that returns all students in database
def getAllStudents():
    # establishes connection to database
    with connect_db() as conn:
        # cursor for this function
        with conn.cursor() as cur:
            sql = "SELECT * FROM students"
            # sends SELECT query to postgres
            cur.execute(sql)
            students = cur.fetchall()

            for student in students:
                print(student)

        # closes the cursor for this func
        cur.close()

# function that adds a new student to database
def addStudent(first_name, last_name, email, enrollment_date):
    with connect_db() as conn:
        with conn.cursor() as cur:
            sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
            data = (first_name, last_name, email, enrollment_date)

            # sends INSERT INTO query to postgres along with the data that needs to be added
            cur.execute(sql, data)
            print("Student added successfully")

        # sends changes to the database
        conn.commit()
        cur.close()


# function that updates the email of the given student
def updateStudentEmail(student_id, new_email):
    with connect_db() as conn:
        with conn.cursor() as cur:
            sql = "UPDATE students SET email = %s WHERE student_id = %s"

            # sends UPDATE query connected to the specified student id to postgres along with the new email that
            # needs to be added
            cur.execute(sql, (new_email, student_id))
            print(f"Student updated successfully: {cur.rowcount}")

        conn.commit()
        cur.close()


# function that deletes the information of the given student
def deleteStudent(student_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            sql = "DELETE FROM students WHERE student_id = %s"

            # sends DELETE query connected to the specified student id to postgres
            cur.execute(sql, (student_id,))
            print("Student was deleted successfully.")

        conn.commit()
        cur.close()


def main():
    while True:

        print("Select one of the options below:\n"
              "1. Add a student\n"
              "2. Update a student's email\n"
              "3. Delete a student\n"
              "4. Return all students\n"
              "5. Close Program")

        option = int(input("Enter your choice: "))

        if option == 1:
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            email = input("Enter student's email: ")
            enrollment_date = input("Enter your student's enrollment date: ")
            addStudent(first_name, last_name, email, enrollment_date)

        elif option == 2:
            student_id = str(input("Enter the student's id: "))
            if student_id.isnumeric():
                new_email = str(input("Enter the new email address: "))
                updateStudentEmail(student_id, new_email)

        elif option == 3:
            student_id = str(input("Enter the student's id: "))
            if student_id.isnumeric():
                deleteStudent(student_id)

        elif option == 4:
            print("Students: ")
            getAllStudents()

        elif option == 5:
            print("Exiting Program...")
            break

        else:
            print("Invalid input entered")

if __name__ == "__main__":
    main()

