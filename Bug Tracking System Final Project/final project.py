import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='sql',
    host='localhost',
    database='bds'
)

cursor = cnx.cursor()

print("                ********* ~Bug Tracking System~ *********               ")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. Manager Panel")
        print("3. Employee Panel")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin_module()
        elif choice == '2':
            manager_panel()
        elif choice == '3':
            employee_panel()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def admin_module():
    while True:
        print("\nAdmin Module:")
        print("1. Manager")
        print("2. Employee")
        print("3. View All Projects")
        print("4. View Bug Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager_module()
        elif choice == '2':
            employee_module()
        elif choice == '3':
            view_all_projects()
        elif choice == '4':
            view_bug_reports()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manager_module():
    while True:
        print("\nManager Module:")
        print("1. Add Manager Account")
        print("2. View Manager Account")
        print("3. Delete Manager")
        print("4. Update Manager Details")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_manager_account()
        elif choice == '2':
            view_manager_account()
        elif choice == '3':
            delete_manager()
        elif choice == '4':
            update_manager_details()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_manager_account():
    empCode = input("Enter manager empCode: ")
    empName = input("Enter manager name: ")
    empEmail = input("Enter manager email: ")
    empPassword = input("Enter manager password: ")
    gender = input("Enter manager gender: ")
    DOB = input("Enter manager DOB: ")
    mobileNo = input("Enter manager mobile number: ")
    Role = "Manager"

    query = "INSERT INTO Employee (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role))
    cnx.commit()
    print("Manager account added successfully.")

def view_manager_account():
    query = "SELECT * FROM Employee WHERE Role = 'Manager'"
    cursor.execute(query)
    managers = cursor.fetchall()
    if managers:
        print("\nManagers:")
        for manager in managers:
            print(f"empCode: {manager[0]}, Name: {manager[1]}, Email: {manager[2]}, Role: {manager[7]}")
    else:
        print("No managers found.")

def delete_manager():
    empCode = input("Enter manager empCode to delete: ")
    query = "DELETE FROM Employee WHERE empCode = %s AND Role = 'Manager'"
    cursor.execute(query, (empCode,))
    cnx.commit()
    print("Manager deleted successfully.")

def update_manager_details():
    empCode = input("Enter manager empCode to update: ")
    empName = input("Enter new name (leave blank to keep current): ")
    empEmail = input("Enter new email (leave blank to keep current): ")
    empPassword = input("Enter new password (leave blank to keep current): ")
    gender = input("Enter new gender (leave blank to keep current): ")
    DOB = input("Enter new DOB (leave blank to keep current): ")
    mobileNo = input("Enter new mobile number (leave blank to keep current): ")

    query = "UPDATE Employee SET "
    if empName:
        query += "empName = %s, "
    if empEmail:
        query += "empEmail = %s, "
    if empPassword:
        query += "empPassword = %s, "
    if gender:
        query += "gender = %s, "
    if DOB:
        query += "DOB = %s, "
    if mobileNo:
        query += "mobileNo = %s, "
    query = query.rstrip(', ') + " WHERE empCode = %s AND Role = 'Manager'"
    values = []
    if empName:
        values.append(empName)
    if empEmail:
        values.append(empEmail)
    if empPassword:
        values.append(empPassword)
    if gender:
        values.append(gender)
    if DOB:
        values.append(DOB)
    if mobileNo:
        values.append(mobileNo)
    values.append(empCode)
    cursor.execute(query, values)
    cnx.commit()
    print("Manager details updated successfully.")

def employee_module():
    while True:
        print("\nEmployee Module:")
        print("1. Add Employee Account")
        print("2. View Employee's Account")
        print("3. Delete Employee Account")
        print("4. Update Employee Details")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee_account()
        elif choice == '2':
            view_employee_account()
        elif choice == '3':
            delete_employee_account()
        elif choice == '4':
            update_employee_details()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_employee_account():
    empCode = input("Enter employee empCode: ")
    empName = input("Enter employee name: ")
    empEmail = input("Enter employee email: ")
    empPassword = input("Enter employee password: ")
    gender = input("Enter employee gender: ")
    DOB = input("Enter employee DOB: ")
    mobileNo = input("Enter employee mobile number: ")
    Role = "Employee"

    query = "INSERT INTO Employee (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role))
    cnx.commit()
    print("Employee account added successfully.")

def view_employee_account():
    query = "SELECT * FROM Employee WHERE Role = 'Employee'"
    cursor.execute(query)
    employees = cursor.fetchall()
    if employees:
        print("\nEmployees:")
        for employee in employees:
            print(f"empCode: {employee[0]}, Name: {employee[1]}, Email: {employee[2]}, Role: {employee[7]}")
    else:
        print("No employees found.")

def delete_employee_account():
    empCode = input("Enter employee empCode to delete: ")
    query = "DELETE FROM Employee WHERE empCode = %s AND Role = 'Employee'"
    cursor.execute(query, (empCode,))
    cnx.commit()
    print("Employee deleted successfully.")

def update_employee_details():
    empCode = input("Enter employee empCode to update: ")
    empName = input("Enter new name (leave blank to keep current): ")
    empEmail = input("Enter new email (leave blank to keep current): ")
    empPassword = input("Enter new password (leave blank to keep current): ")
    gender = input("Enter new gender (leave blank to keep current): ")
    DOB = input("Enter new DOB (leave blank to keep current): ")
    mobileNo = input("Enter new mobile number (leave blank to keep current): ")

    query = "UPDATE Employee SET "
    if empName:
        query += "empName = %s, "
    if empEmail:
        query += "empEmail = %s, "
    if empPassword:
        query += "empPassword = %s, "
    if gender:
        query += "gender = %s, "
    if DOB:
        query += "DOB = %s, "
    if mobileNo:
        query += "mobileNo = %s, "
    query = query.rstrip(', ') + " WHERE empCode = %s AND Role = 'Employee'"
    values = []
    if empName:
        values.append(empName)
    if empEmail:
        values.append(empEmail)
    if empPassword:
        values.append(empPassword)
    if gender:
        values.append(gender)
    if DOB:
        values.append(DOB)
    if mobileNo:
        values.append(mobileNo)
    values.append(empCode)
    cursor.execute(query, values)
    cnx.commit()
    print("Employee details updated successfully.")
def view_all_projects():
    query = "SELECT * FROM Project"
    cursor.execute(query)
    projects = cursor.fetchall()
    if projects:
        print("\nProjects:")
        for project in projects:
            print(f"ID: {project[0]}, Name: {project[1]}, Start Date: {project[2]}, End Date: {project[3]}, Description: {project[4]}")
    else:
        print("No projects found.")
def view_bug_reports():
    query = "SELECT * FROM BugReport"
    cursor.execute(query)
    bug_reports = cursor.fetchall()
    if bug_reports:
        print("\nBug Reports:")
        for bug_report in bug_reports:
            print(f"Bug No: {bug_report[0]}, Bug Code: {bug_report[1]}, Project ID: {bug_report[2]}, TCode: {bug_report[3]}, EGode: {bug_report[4]}, Status: {bug_report[5]}, Bug Description: {bug_report[6]}")
    else:
        print("No bug reports found.")
pass

def manager_panel():
    while True:
        print("\nManager Panel:")
        print("1. Update Profile")
        print("2. Manage Project")
        print("    1. Add Project")
        print("    2. View All Projects")
        print("    3. Delete Project")
        print("    4. Update Project")
        print("3. Bug's")
        print("    1. Add New Bug")
        print("    2. View All Bug's")
        print("    3. Update Bug")
        print("    4. Delete Bug")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            update_profile()
        elif choice == '2':
            manage_project()
        elif choice == '3':
            manage_bugs()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def update_profile():
    managerID = int(input("Enter manager ID to update: "))
    query = "SELECT * FROM Employee WHERE empCode = %s AND Role = 'Manager'"
    cursor.execute(query, (managerID,))
    manager_exists = cursor.fetchone()
    if manager_exists:
        empName = input("Enter new name (leave blank to keep current): ") or manager_exists[1]
        empEmail = input("Enter new email (leave blank to keep current): ") or manager_exists[2]
        empPassword = input("Enter new password (leave blank to keep current): ") or manager_exists[3]
        gender = input("Enter new gender (leave blank to keep current): ") or manager_exists[4]
        DOB = input("Enter new DOB (leave blank to keep current): ") or manager_exists[5]
        mobileNo = input("Enter new mobile number (leave blank to keep current): ") or manager_exists[6]

        query = "UPDATE Employee SET "
        values = []
        update_fields = []
        if empName != manager_exists[1]:
            update_fields.append("empName = %s")
            values.append(empName)
        if empEmail != manager_exists[2]:
            update_fields.append("empEmail = %s")
            values.append(empEmail)
        if empPassword != manager_exists[3]:
            update_fields.append("empPassword = %s")
            values.append(empPassword)
        if gender != manager_exists[4]:
            update_fields.append("gender = %s")
            values.append(gender)
        if DOB != manager_exists[5]:
            update_fields.append("DOB = %s")
            values.append(DOB)
        if mobileNo != manager_exists[6]:
            update_fields.append("mobileNo = %s")
            values.append(mobileNo)

        if update_fields:
            query += ", ".join(update_fields) + " WHERE empCode = %s AND Role = 'Manager'"
            values.append(managerID)
            cursor.execute(query, tuple(values))
            cnx.commit()
            print("Manager profile updated successfully.")
        else:
            print("No changes made.")
    else:
        print("Manager not found.")
        
def manage_project():
    while True:
        print("\nManage Project:")
        print("1. Add Project")
        print("2. View All Projects")
        print("3. Delete Project")
        print("4. Update Project")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_project()
        elif choice == '2':
            view_all_projects()
        elif choice == '3':
            delete_project()
        elif choice == '4':
            update_project()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_project():
    projectName = input("Enter project name: ")
    startDate = input("Enter start date: ")
    endDate = input("Enter end date: ")
    projectDec = input("Enter project description: ")

    query = "SELECT * FROM Project WHERE projectName = %s"
    cursor.execute(query, (projectName,))
    project_exists = cursor.fetchone()
    if project_exists:
        print("Project name already exists. Please enter a unique project name.")
    else:
        try:
 
            query = "SELECT COALESCE(MAX(projectID), 0) + 1 FROM Project"
            cursor.execute(query)
            projectID = cursor.fetchone()[0]

            query = "INSERT INTO Project (projectID, projectName, SDate, EDate, projectDec) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (projectID, projectName, startDate, endDate, projectDec))
            cnx.commit()
            print("Project added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def view_all_projects():
    query = "SELECT * FROM Project"
    cursor.execute(query)
    projects = cursor.fetchall()
    if projects:
        print("\nProjects:")
        for project in projects:
            print(f"ID: {project[0]}, Name: {project[1]}, Start Date: {project[2]}, End Date: {project[3]}, Description: {project[4]}")
    else:
        print("No projects found.")


def delete_project():
    projectID = int(input("Enter project ID to delete: "))
    try:
        query = "SELECT * FROM Project WHERE projectID = %s"
        cursor.execute(query, (projectID,))
        project_exists = cursor.fetchone()
        if project_exists:
            confirm = input("Are you sure you want to delete this project? (yes/no): ")
            if confirm.lower() == "yes":

                query = "DELETE FROM bugreport WHERE projectID = %s"
                cursor.execute(query, (projectID,))

                query = "DELETE FROM Project WHERE projectID = %s"
                cursor.execute(query, (projectID,))
                cnx.commit()
                print("Project deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Project not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
def update_project():
    projectID = int(input("Enter project ID to update: "))
    query = "SELECT projectName, SDate, EDate, projectDec FROM project WHERE projectID = %s"
    cursor.execute(query, (projectID,))
    project_exists = cursor.fetchone()
    if project_exists:
        projectName = input("Enter new name (leave blank to keep current): ") or project_exists[0]
        SDate = input("Enter new start date (leave blank to keep current): ") or project_exists[1]
        EDate = input("Enter new end date (leave blank to keep current): ") or project_exists[2]
        projectDec = input("Enter new description (leave blank to keep current): ") or project_exists[3]

        query = "UPDATE project SET "
        values = []
        update_fields = []
        if projectName!= project_exists[0]:
            update_fields.append("projectName = %s")
            values.append(projectName)
        if SDate!= project_exists[1]:
            update_fields.append("SDate = %s")
            values.append(SDate)
        if EDate!= project_exists[2]:
            update_fields.append("EDate = %s")
            values.append(EDate)
        if projectDec!= project_exists[3]:
            update_fields.append("projectDec = %s")
            values.append(projectDec)

        if update_fields:
            query += ", ".join(update_fields) + " WHERE projectID = %s"
            values.append(projectID)
            cursor.execute(query, tuple(values))
            cnx.commit()
            print("Project details updated successfully.")
        else:
            print("No changes made.")
    else:
        print("Project not found.")
        
def manage_bugs():
    while True:
        print("\nManage Bugs:")
        print("1. Add New Bug")
        print("2. View All Bug's")
        print("3. Update Bug")
        print("4. Delete Bug")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_bug()
        elif choice == '2':
            view_all_bugs()
        elif choice == '3':
            update_bug()
        elif choice == '4':
            delete_bug()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_bug():
    bugCode = input("Enter bug code: ")
    projectID = int(input("Enter project ID: "))
    TCode = int(input("Enter TCode: "))
    EGode = int(input("Enter EGode: "))
    status = input("Enter status (pending/resolved): ")
    bugDes = input("Enter bug description: ")

    query = "SELECT * FROM project WHERE projectID = %s"
    cursor.execute(query, (projectID,))
    project_exists = cursor.fetchone()
    if project_exists:
  
        query = "SELECT MAX(bugNo) FROM bugreport"
        cursor.execute(query)
        max_bug_no = cursor.fetchone()[0]
        if max_bug_no is None:
            bugNo = 1
        else:
            bugNo = max_bug_no + 1

        query = "INSERT INTO bugreport (bugNo, bugCode, projectID, TCode, EGode, status, bugDes) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (bugNo, bugCode, projectID, TCode, EGode, status, bugDes))
        cnx.commit()
        print("Bug report added successfully.")
    else:
        print("Project ID does not exist. Please enter a valid project ID.")

def view_all_bugs():
    query = "SELECT * FROM bugreport"
    cursor.execute(query)
    bug_reports = cursor.fetchall()
    if bug_reports:
        print("\nBug Reports:")
        for bug_report in bug_reports:
            print(f"Bug No: {bug_report[0]}, Bug Code: {bug_report[1]}, Project ID: {bug_report[2]}, TCode: {bug_report[3]}, EGode: {bug_report[4]}, Status: {bug_report[5]}, Bug Description: {bug_report[6]}")
    else:
        print("No bug reports found.")

def update_bug():
    bugNo = int(input("Enter bug number to update: "))
    query = "SELECT * FROM bugreport WHERE bugNo = %s"
    cursor.execute(query, (bugNo,))
    bug_report = cursor.fetchone()
    if bug_report:
        print("Current bug report:")
        print(f"Bug No: {bug_report[0]}, Bug Code: {bug_report[1]}, Project ID: {bug_report[2]}, TCode: {bug_report[3]}, EGode: {bug_report[4]}, Status: {bug_report[5]}, Bug Description: {bug_report[6]}")
        
        bugCode = input("Enter new bug code (or press enter to keep current): ") or bug_report[1]
        projectID = int(input("Enter new project ID (or press enter to keep current): ") or bug_report[2])
        TCode = int(input("Enter new TCode (or press enter to keep current): ") or bug_report[3])
        EGode = int(input("Enter new EGode (or press enter to keep current): ") or bug_report[4])
        status = input("Enter new status (or press enter to keep current): ") or bug_report[5]
        bugDes = input("Enter new bug description (or press enter to keep current): ") or bug_report[6]
        
        query = "SELECT * FROM project WHERE projectID = %s"
        cursor.execute(query, (projectID,))
        project_exists = cursor.fetchone()
        if project_exists:
            query = "UPDATE bugreport SET bugCode = %s, projectID = %s, TCode = %s, EGode = %s, status = %s, bugDes = %s WHERE bugNo = %s"
            cursor.execute(query, (bugCode, projectID, TCode, EGode, status, bugDes, bugNo))
            cnx.commit()
            print("Bug report updated successfully.")
        else:
            print("Project ID does not exist. Please enter a valid project ID.")
    else:
        print("Bug report not found.")
        
def delete_bug():
    bugNo = int(input("Enter bug number to delete: "))
    query = "SELECT br.bugNo, br.bugCode, p.projectName, br.TCode, br.EGode, br.status, br.bugDes " \
            "FROM bugreport br " \
            "INNER JOIN project p ON br.projectID = p.projectID " \
            "WHERE br.bugNo = %s"
    cursor.execute(query, (bugNo,))
    bug_report = cursor.fetchone()
    if bug_report:
        print("Bug report to be deleted:")
        print(f"Bug No: {bug_report[0]}, Bug Code: {bug_report[1]}, Project Name: {bug_report[2]}, TCode: {bug_report[3]}, EGode: {bug_report[4]}, Status: {bug_report[5]}, Bug Description: {bug_report[6]}")
        
        confirm = input("Are you sure you want to delete this bug report? (yes/no): ")
        if confirm.lower() == "yes":
            query = "DELETE FROM bugreport WHERE bugNo = %s"
            cursor.execute(query, (bugNo,))
            cnx.commit()
            print("Bug report deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Bug report not found.")
pass

def employee_panel():
    while True:
        print("\nEmployee Panel:")
        print("1. Update Profile")
        print("2. Add Bug's Report")
        print("3. Update Bug status")
        print("4. View Bug's")
        print("5. Bug Detail's")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            update_profile()
        elif choice == '2':
            add_bug_report()
        elif choice == '3':
            update_bug_status()
        elif choice == '4':
            view_bugs()
        elif choice == '5':
            bug_details()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def update_profile():
    empCode = input("Enter employee empCode to update: ")
    empName = input("Enter new name (leave blank to keep current): ")
    empEmail = input("Enter new email (leave blank to keep current): ")
    empPassword = input("Enter new password (leave blank to keep current): ")
    gender = input("Enter new gender (leave blank to keep current): ")
    DOB = input("Enter new DOB (leave blank to keep current): ")
    mobileNo = input("Enter new mobile number (leave blank to keep current): ")

    query = "UPDATE Employee SET "
    if empName:
        query += "empName = %s, "
    if empEmail:
        query += "empEmail = %s, "
    if empPassword:
        query += "empPassword = %s, "
    if gender:
        query += "gender = %s, "
    if DOB:
        query += "DOB = %s, "
    if mobileNo:
        query += "mobileNo = %s, "
    query = query.rstrip(', ') + " WHERE empCode = %s AND Role = 'Employee'"
    values = []
    if empName:
        values.append(empName)
    if empEmail:
        values.append(empEmail)
    if empPassword:
        values.append(empPassword)
    if gender:
        values.append(gender)
    if DOB:
        values.append(DOB)
    if mobileNo:
        values.append(mobileNo)
    values.append(empCode)
    cursor.execute(query, values)
    cnx.commit()
    print("Employee details updated successfully.")

def add_bug_report():
    bugNo = int(input("Enter bug number: "))
    bugCode = input("Enter bug code: ")
    projectID = int(input("Enter project ID: "))
    TCode = int(input("Enter TCode: "))
    EGode = int(input("Enter EGode: "))
    status = input("Enter status (pending/resolved): ")
    bugDes = input("Enter bug description: ")

    query = "INSERT INTO bugreport (bugNo, bugCode, projectID, TCode, EGode, status, bugDes) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (bugNo, bugCode, projectID, TCode, EGode, status, bugDes))
    cnx.commit()
    print("Bug report added successfully.")
def update_bug_status():
    bugCode = input("Enter bug code to update: ")
    status = input("Enter new status: ")

    query = "UPDATE bugreport SET status = %s WHERE bugCode = %s"
    cursor.execute(query, (status, bugCode))
    cnx.commit()
    print("Bug status updated successfully.")

def view_bugs():
    query = "SELECT * FROM BugReport"
    cursor.execute(query)
    bug_reports = cursor.fetchall()
    if bug_reports:
        print("\nBug Reports:")
        for bug_report in bug_reports:
            print(f"Bug Code: {bug_report[0]}, Project ID: {bug_report[1]}, TCode: {bug_report[2]}, EGode: {bug_report[3]}, Status: {bug_report[4]}, Bug Description: {bug_report[5]}")
    else:
        print("No bug reports found.")

def bug_details():
    bugCode = input("Enter bug code to view details: ")
    query = "SELECT * FROM BugReport WHERE bugCode = %s"
    cursor.execute(query, (bugCode,))
    bug_report = cursor.fetchone()
    if bug_report:
        print(f"\nBug Code: {bug_report[0]}, Project ID: {bug_report[1]}, TCode: {bug_report[2]}, EGode: {bug_report[3]}, Status: {bug_report[4]}, Bug Description: {bug_report[5]}")
    else:
        print("No bug report found.")
pass

main_menu()
cnx.close()
