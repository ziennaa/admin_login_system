import csv
import getpass

userdata = [
   {'username':'u1','password':'p1','roll':'1','name':'Arjun','age':'16','email':'u1@gmail.com','phone':''},
    {'username':'u2','password':'p2','roll':'2','name':'Aryan','age':'16','email':'u2@gmail.com','phone':''},
    {'username':'u3','password':'p3','roll':'3','name':'Virat','age':'16','email':'u3@gmail.com','phone':''},
    {'username':'u6','password':'p6','roll':'6','name':'Sam','age':'16','email':'u6@gmail.com','phone':'*******999'},
    {'username':'u7','password':'p15','roll':'7','name':'Sanya','age':'16','email':'u7@gmail.com','phone':'*******977'},
    {'username':'u8','password':'p155','roll':'8','name':'Rohit','age':'16','email':'u8@gmail.com','phone':'*******887'},
    {'username':'u10','password':'p155','roll':'8','name':'Rohit','age':'16','email':'u10@gmail.com','phone':'*******937'},
    {'username':'u11','password':'p1555','roll':'9','name':'Shubman','age':'16','email':'u11@gmail.com','phone':'*******917'},
    {'username':'u12','password':'p155555','roll':'10','name':'Sasha','age':'16','email':'u12@gmail.com','phone':'*******187'},
    {'username':'u13','password':'p14444','roll':'11','name':'Jim','age':'16','email':'u13@gmail.com','phone':'*******957'},
    {'username':'u14','password':'p13343','roll':'12','name':'Mark','age':'16','email':'u14@gmail.com','phone':'*******967'},
    {'username':'u15','password':'p1654','roll':'13','name':'Alex','age':'16','email':'u15@gmail.com','phone':'*******667'},
    {'username':'u16','password':'p13332','roll':'14','name':'Tam','age':'16','email':'u16@gmail.com','phone':'*******217'},
    {'username':'u17','password':'p123','roll':'15','name':'Cam','age':'16','email':'u17@gmail.com','phone':'*******897'},
    {'username':'u18','password':'p1876','roll':'16','name':'Amy','age':'16','email':'u18@gmail.com','phone':'*******677'},
]


with open('students.csv', 'w', newline='') as f:
    heading = ['username', 'password', 'roll', 'name', 'age', 'email', 'phone']
    wr = csv.DictWriter(f, fieldnames=heading)
    wr.writeheader()
    wr.writerows(userdata)


print("User data written successfully to 'students.csv'")


# Creating admin login system
def readuser():
    userdata = []
    with open('students.csv', 'r', newline='') as f:
        read = csv.DictReader(f)
        for i in read:
            userdata.append(i)
    return userdata


def verify(username, password, userdata):
    for j in userdata:
        if j['username'] == username and j['password'] == password:
            return True
    return False


# Main function
def main():
    print("Admin Login System")
    userdata = readuser()
    max_attempts = 3
    count = 0
    while count < max_attempts:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        if verify(username, password, userdata):
            print("Login successful! Welcome", username)
            break
        else:
            print("Login failed. Try again!")
            count = count + 1
    if count == max_attempts:
        print("Reached maximum attempts, exiting.")


main()


# Student Database Management System
student_fields = ['username', 'password', 'roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'


def display_menu():
    print("---------------------------------------")
    print(" Student Database Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database


    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)


    with open(student_database, "a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(student_data)


    print("Data saved successfully")
    input("Press any key to continue")
    return






def view_students():
    global student_fields
    global student_database


    print("--- Student Records ---")


    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)


       
        next(reader)


        for x in student_fields:
            print(f"{x:<10} |", end='')
        print("\n" + "-" * 69)


        for row in reader:
            for item in row:
                print(f"{item:<10} |", end='')
            print("\n")


    input("Press any key to continue")






def search_student():
    global student_fields
    global student_database


    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[2]:
                    print("----- Student Found -----")
                    for field, value in zip(student_fields, row):
                        print(f"{field}: {value}")
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")


def update_student():
    global student_fields
    global student_database


    print("--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[2]:
                    index_student = counter
                    print("Student Found at index ", index_student)
                    student_data = []
                    for field in student_fields:
                        value = input(f"Enter {field}: ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    if index_student is not None:
        with open(student_database, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student information updated successfully")
    else:
        print("Roll No. not found in our database")


    input("Press any key to continue")


def delete_student():
    global student_fields
    global student_database


    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[2]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True


    if student_found is True:
        with open(student_database, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")


    input("Press any key to continue")


while True:
    display_menu()


    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break


print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
















